#!/usr/bin/env python3
"""Sync LaTeX cite keys using DOI-based mapping between old and current bib.

Usage:
  python -m scripts.cite.sync_cite_keys \
      --bib bibliography.bib \
      --old-bib-ref HEAD:bibliography.bib \
      --files main.tex sections/**/*.tex \
      --yes
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ENTRY_SPLIT_RE = re.compile(r"(?=^@\w+\{)", re.MULTILINE)
ENTRY_KEY_RE = re.compile(r"^@\w+\{\s*([^,\s]+)\s*,", re.MULTILINE)
DOI_FIELD_RE = re.compile(
    r"\bdoi\s*=\s*(?:\{([^}]*)\}|\"([^\"]*)\")",
    re.IGNORECASE | re.DOTALL,
)
CITE_RE = re.compile(r"\\([A-Za-z]*cite[A-Za-z*]*)\s*((?:\[[^\]]*\]\s*)*)\{([^}]*)\}")


def _normalize_doi(doi: str) -> str:
    value = doi.strip().lower()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    value = re.sub(r"[\s\]\[{}]+$", "", value)
    value = re.sub(r"[\.,;:]+$", "", value)
    while value.endswith(")") and "(" not in value:
        value = value[:-1]
    return value


def _doi_to_key_map(bib_text: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for entry in ENTRY_SPLIT_RE.split(bib_text):
        if not entry.startswith("@"):
            continue
        key_match = ENTRY_KEY_RE.search(entry)
        doi_match = DOI_FIELD_RE.search(entry)
        if not key_match or not doi_match:
            continue
        key = key_match.group(1).strip()
        doi = _normalize_doi((doi_match.group(1) or doi_match.group(2) or ""))
        if doi.startswith("10."):
            mapping[doi] = key
    return mapping


def _rewrite_cites(text: str, key_map: dict[str, str]) -> tuple[str, int]:
    replacements = 0

    def _replace(match: re.Match[str]) -> str:
        nonlocal replacements
        command = match.group(1)
        options = match.group(2)
        keys_blob = match.group(3)

        keys = [k.strip() for k in keys_blob.split(",")]
        rewritten: list[str] = []
        changed = False
        for key in keys:
            new_key = key_map.get(key, key)
            rewritten.append(new_key)
            if new_key != key:
                changed = True
        if changed:
            replacements += 1
        return f"\\{command}{options}{{{', '.join(rewritten)}}}"

    return CITE_RE.sub(_replace, text), replacements


def _expand_files(patterns: list[str]) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()
    for pattern in patterns:
        if any(ch in pattern for ch in "*?[]"):
            for path in Path.cwd().glob(pattern):
                if path.is_file() and path not in seen:
                    files.append(path)
                    seen.add(path)
        else:
            path = Path(pattern)
            if path.is_file() and path not in seen:
                files.append(path)
                seen.add(path)
    return sorted(files)


def _read_git_ref(ref: str) -> str:
    result = subprocess.run(
        ["git", "show", ref],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git show failed for {ref}")
    return result.stdout


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync cite keys using DOI mapping from git bib snapshot.")
    parser.add_argument("--bib", required=True, help="Current bibliography file path")
    parser.add_argument("--old-bib-ref", required=True, help="Git ref to old bib, e.g. HEAD:bibliography.bib")
    parser.add_argument("--files", nargs="+", required=True, help="Files or glob patterns to rewrite")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation")
    args = parser.parse_args()

    bib_path = Path(args.bib)
    if not bib_path.exists():
        print(f"Error: bibliography file not found: {bib_path}", file=sys.stderr)
        sys.exit(1)

    files = _expand_files(args.files)
    if not files:
        print("Error: no files matched --files", file=sys.stderr)
        sys.exit(1)

    old_text = _read_git_ref(args.old_bib_ref)
    new_text = bib_path.read_text(encoding="utf-8")

    old_map = _doi_to_key_map(old_text)
    new_map = _doi_to_key_map(new_text)

    key_map: dict[str, str] = {}
    for doi, old_key in old_map.items():
        new_key = new_map.get(doi)
        if new_key and new_key != old_key:
            key_map[old_key] = new_key

    if not key_map:
        print("No key remapping detected from old bib to current bib.")
        return

    print(f"Detected {len(key_map)} key remaps.")

    if not args.yes:
        answer = input("Apply cite-key rewrites? [y/N] ").strip().lower()
        if answer not in {"y", "yes"}:
            print("Aborted.")
            return

    file_changes = 0
    total_replacements = 0
    for file_path in files:
        original = file_path.read_text(encoding="utf-8")
        rewritten, replacements = _rewrite_cites(original, key_map)
        if rewritten != original:
            file_path.write_text(rewritten, encoding="utf-8")
            file_changes += 1
        total_replacements += replacements

    print(f"Updated files: {file_changes}")
    print(f"Cite-command replacements: {total_replacements}")


if __name__ == "__main__":
    main()
