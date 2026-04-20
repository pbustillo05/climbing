#!/usr/bin/env python3
"""Rekey a bibliography to alpha-style keys and update cite commands.

Usage:
  python -m scripts.cite.rekey_alpha_keys \
      --bib bibliography.bib \
      --files main.tex sections/**/*.tex \
      --yes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from .fetch_bibtex import make_alpha_key

ENTRY_SPLIT_RE = re.compile(r"(?=^@\w+\{)", re.MULTILINE)
ENTRY_KEY_RE = re.compile(r"^(@\w+\{)\s*([^,\s]+)\s*,", re.MULTILINE)
CITE_RE = re.compile(r"\\([A-Za-z]*cite[A-Za-z*]*)\s*((?:\[[^\]]*\]\s*)*)\{([^}]*)\}")


def _field_value(entry: str, field: str) -> str:
    pattern = re.compile(
        rf"\b{field}\s*=\s*(?:\{{([^}}]*)\}}|\"([^\"]*)\")",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(entry)
    if not match:
        return ""
    return (match.group(1) or match.group(2) or "").strip()


def _family_from_author(author: str) -> str:
    cleaned = author.replace("{", "").replace("}", "")
    cleaned = cleaned.replace("\\", " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if not cleaned:
        return ""
    if "," in cleaned:
        return cleaned.split(",", 1)[0].strip()
    parts = cleaned.split()
    return parts[-1] if parts else ""


def _alpha_key_for_entry(entry: str) -> str:
    authors_field = _field_value(entry, "author")
    year_field = _field_value(entry, "year")
    authors = [a.strip() for a in authors_field.split(" and ") if a.strip()]
    families = [_family_from_author(author) for author in authors]
    return make_alpha_key(families, year_field)


def _unique_key(desired: str, used_lower: set[str]) -> str:
    if desired.lower() not in used_lower:
        return desired
    suffix_ord = ord("a")
    while f"{desired}{chr(suffix_ord)}".lower() in used_lower:
        suffix_ord += 1
    return f"{desired}{chr(suffix_ord)}"


def _rekey_bib_text(text: str) -> tuple[str, dict[str, str], int]:
    parts = ENTRY_SPLIT_RE.split(text)
    out_parts: list[str] = []
    mapping: dict[str, str] = {}
    used_lower: set[str] = set()
    changed = 0

    for part in parts:
        if not part.startswith("@"):
            out_parts.append(part)
            continue

        key_match = ENTRY_KEY_RE.search(part)
        if not key_match:
            out_parts.append(part)
            continue

        old_key = key_match.group(2)
        desired = _alpha_key_for_entry(part)
        new_key = _unique_key(desired, used_lower)
        used_lower.add(new_key.lower())
        mapping[old_key] = new_key

        if new_key != old_key:
            part = ENTRY_KEY_RE.sub(rf"\1{new_key},", part, count=1)
            changed += 1

        out_parts.append(part)

    return "".join(out_parts), mapping, changed


def _rewrite_cite_keys(text: str, mapping: dict[str, str]) -> tuple[str, int]:
    replacements = 0

    def _replace(match: re.Match[str]) -> str:
        nonlocal replacements
        command = match.group(1)
        options = match.group(2)
        keys_blob = match.group(3)

        original_keys = [k.strip() for k in keys_blob.split(",")]
        rewritten_keys: list[str] = []
        changed_here = False

        for key in original_keys:
            rewritten = mapping.get(key, key)
            rewritten_keys.append(rewritten)
            if rewritten != key:
                changed_here = True

        if changed_here:
            replacements += 1

        return f"\\{command}{options}{{{', '.join(rewritten_keys)}}}"

    return CITE_RE.sub(_replace, text), replacements


def _expand_files(patterns: list[str]) -> list[Path]:
    resolved: list[Path] = []
    seen: set[Path] = set()
    for pattern in patterns:
        if any(ch in pattern for ch in "*?[]"):
            for path in Path.cwd().glob(pattern):
                if path.is_file() and path not in seen:
                    resolved.append(path)
                    seen.add(path)
        else:
            path = Path(pattern)
            if path.is_file() and path not in seen:
                resolved.append(path)
                seen.add(path)
    return sorted(resolved)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rekey bibliography entries to alpha-style keys.")
    parser.add_argument("--bib", required=True, help="Path to bibliography.bib")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Files or glob patterns to update cite commands in (e.g. sections/**/*.tex)",
    )
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()

    bib_path = Path(args.bib)
    if not bib_path.exists():
        print(f"Error: bibliography file not found: {bib_path}", file=sys.stderr)
        sys.exit(1)

    tex_files = _expand_files(args.files)
    if not tex_files:
        print("Error: no files matched --files patterns.", file=sys.stderr)
        sys.exit(1)

    original_bib = bib_path.read_text(encoding="utf-8")
    rewritten_bib, mapping, entry_changes = _rekey_bib_text(original_bib)
    mapped_changes = {old: new for old, new in mapping.items() if old != new}

    if mapped_changes:
        print(f"Rekeying {len(mapped_changes)} bibliography entries:")
        for old, new in sorted(mapped_changes.items()):
            print(f"  {old} -> {new}")
    else:
        print("No bibliography keys required rekeying.")

    if not args.yes:
        answer = input("\nApply bibliography and citation updates? [y/N] ").strip().lower()
        if answer not in {"y", "yes"}:
            print("Aborted.")
            return

    if mapped_changes:
        bib_path.write_text(rewritten_bib, encoding="utf-8")

    file_changes = 0
    cite_replacements_total = 0
    for file_path in tex_files:
        original = file_path.read_text(encoding="utf-8")
        rewritten, cite_replacements = _rewrite_cite_keys(original, mapping)
        if rewritten != original:
            file_path.write_text(rewritten, encoding="utf-8")
            file_changes += 1
        cite_replacements_total += cite_replacements

    if mapped_changes:
        print(f"Updated bibliography: {bib_path}")
    print(f"Updated files: {file_changes}")
    print(f"Cite-command replacements: {cite_replacements_total}")


if __name__ == "__main__":
    main()
