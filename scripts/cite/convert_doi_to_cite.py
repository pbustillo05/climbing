#!/usr/bin/env python3
r"""Convert DOI references in TeX files to \cite{key} commands.

This script uses DOI->bibkey mappings from bibliography.bib.

Usage:
  python -m scripts.cite.convert_doi_to_cite \
      --bib bibliography.bib \
      --files sections/09_weekly_integration.tex sections/10_supplements.tex sections/11_injury_management.tex sections/12_recovery.tex \
      --yes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOI_HREF_RE = re.compile(r"\\href\{https?://doi\.org/([^}]+)\}\{[^}]*\}", re.IGNORECASE)
DOI_TAG_RE = re.compile(
    r"DOI\s*[:~]\s*(10\.[0-9]{4,9}/[-._;()/:A-Za-z0-9]*[A-Za-z0-9])([\),\].;:]*)",
    re.IGNORECASE,
)

# Known correction where manuscript used an unresolved DOI variant.
DOI_ALIASES = {
    "10.1007/s00421-007-0552-4": "10.1007/s00421-007-0552-2",
}


def _normalize_doi(doi: str) -> str:
    value = doi.strip().lower()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    value = re.sub(r"[\s\]\[{}]+$", "", value)
    value = re.sub(r"[\.,;:]+$", "", value)
    while value.endswith(")") and "(" not in value:
        value = value[:-1]
    return DOI_ALIASES.get(value, value)


def _doi_map_from_bib(bib_path: Path) -> dict[str, str]:
    text = bib_path.read_text(encoding="utf-8")
    entries = re.split(r"(?=^@\w+\{)", text, flags=re.MULTILINE)
    mapping: dict[str, str] = {}

    for entry in entries:
        if not entry.startswith("@"):
            continue
        key_match = re.search(r"^@\w+\{\s*([^,\s]+)\s*,", entry, re.MULTILINE)
        doi_match = re.search(
            r"\bdoi\s*=\s*(?:\{([^}]*)\}|\"([^\"]*)\")",
            entry,
            re.IGNORECASE | re.DOTALL,
        )
        if not key_match or not doi_match:
            continue

        key = key_match.group(1).strip()
        raw_doi = (doi_match.group(1) or doi_match.group(2) or "").strip()
        normalized = _normalize_doi(raw_doi)
        if normalized.startswith("10."):
            mapping[normalized] = key

    return mapping


def _expand_files(file_args: list[str]) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()
    for item in file_args:
        if any(ch in item for ch in "*?[]"):
            for path in Path.cwd().glob(item):
                if path.is_file() and path not in seen:
                    files.append(path)
                    seen.add(path)
        else:
            path = Path(item)
            if path.is_file() and path not in seen:
                files.append(path)
                seen.add(path)
    return sorted(files)


def _convert_text(text: str, doi_to_key: dict[str, str]) -> tuple[str, int, set[str]]:
    replacements = 0
    unresolved: set[str] = set()

    def _replace_href(match: re.Match[str]) -> str:
        nonlocal replacements
        doi = _normalize_doi(match.group(1))
        key = doi_to_key.get(doi)
        if not key:
            unresolved.add(doi)
            return match.group(0)
        replacements += 1
        return f"\\cite{{{key}}}"

    def _replace_doi_tag(match: re.Match[str]) -> str:
        nonlocal replacements
        doi = _normalize_doi(match.group(1))
        trailing = match.group(2) or ""
        key = doi_to_key.get(doi)
        if not key:
            unresolved.add(doi)
            return match.group(0)
        replacements += 1
        return f"\\cite{{{key}}}{trailing}"

    text = DOI_HREF_RE.sub(_replace_href, text)
    text = DOI_TAG_RE.sub(_replace_doi_tag, text)
    return text, replacements, unresolved


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert DOI references to cite commands.")
    parser.add_argument("--bib", required=True, help="Path to bibliography.bib")
    parser.add_argument("--files", nargs="+", required=True, help="TeX files or glob patterns")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()

    bib_path = Path(args.bib)
    if not bib_path.exists():
        print(f"Error: bibliography file not found: {bib_path}", file=sys.stderr)
        sys.exit(1)

    tex_files = _expand_files(args.files)
    if not tex_files:
        print("Error: no files matched --files.", file=sys.stderr)
        sys.exit(1)

    doi_to_key = _doi_map_from_bib(bib_path)

    pending: dict[Path, tuple[str, int, set[str]]] = {}
    total_replacements = 0
    unresolved_all: set[str] = set()

    for file_path in tex_files:
        original = file_path.read_text(encoding="utf-8")
        converted, count, unresolved = _convert_text(original, doi_to_key)
        if converted != original:
            pending[file_path] = (converted, count, unresolved)
        total_replacements += count
        unresolved_all.update(unresolved)

    print(f"Planned DOI->cite replacements: {total_replacements}")
    if unresolved_all:
        print("Unresolved DOIs:")
        for doi in sorted(unresolved_all):
            print(f"  {doi}")

    if not pending:
        print("No file changes needed.")
        return

    if not args.yes:
        answer = input("Apply changes to files? [y/N] ").strip().lower()
        if answer not in {"y", "yes"}:
            print("Aborted.")
            return

    for file_path, (new_text, _count, _unresolved) in pending.items():
        file_path.write_text(new_text, encoding="utf-8")

    print(f"Updated files: {len(pending)}")


if __name__ == "__main__":
    main()
