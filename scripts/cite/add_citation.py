#!/usr/bin/env python3
"""Add a citation to a .bib file.

Workflow:
  1. Parse DOI or arXiv ID from --doi / --arxiv
  2. Fetch BibTeX (CrossRef for DOI, arXiv API for arXiv IDs)
  3. Generate canonical key (LastnameYear)
  4. Check for duplicate DOI / key in target .bib
  5. Print entry and ask user to confirm before writing

Usage:
    python -m bourbakia.cite.add_citation --bib refs.bib --doi 10.1007/...
    python -m bourbakia.cite.add_citation --bib refs.bib --arxiv 2301.07041
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from .fetch_bibtex import fetch_crossref, format_bibtex, make_alpha_key, normalize_doi


# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------

def _fetch_arxiv(arxiv_id: str) -> str:
    """Return a BibTeX entry for an arXiv paper (using the arXiv API)."""
    arxiv_id = arxiv_id.strip().removeprefix("arxiv:").removeprefix("arXiv:")
    url = f"https://export.arxiv.org/api/query?id_list={urllib.parse.quote(arxiv_id)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "BourbakIA/0.1 (https://github.com/bourbakia/bourbakia)"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        xml = resp.read().decode()

    # Minimal XML parsing without external deps
    def _tag(tag: str) -> str:
        m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", xml, re.DOTALL)
        return m.group(1).strip() if m else ""

    title = re.sub(r"\s+", " ", _tag("title").replace("\n", " ")).strip()
    published = _tag("published")[:4]  # year
    authors_raw = re.findall(r"<author>\s*<name>(.*?)</name>", xml, re.DOTALL)

    def _fmt_author(name: str) -> str:
        parts = name.strip().split()
        if len(parts) >= 2:
            return f"{parts[-1]}, {' '.join(parts[:-1])}"
        return name.strip()

    authors = " and ".join(_fmt_author(a) for a in authors_raw) or "Unknown"
    families = [name.strip().split()[-1] for name in authors_raw if name.strip()]
    key = make_alpha_key(families, published)

    return (
        f"@misc{{{key},\n"
        f"  author       = {{{authors}}},\n"
        f"  title        = {{{title}}},\n"
        f"  year         = {{{published}}},\n"
        f"  eprint       = {{{arxiv_id}}},\n"
        f"  archivePrefix = {{arXiv}},\n"
        f"}}"
    )


# ---------------------------------------------------------------------------
# .bib duplicate detection
# ---------------------------------------------------------------------------

_DOI_RE = re.compile(r"doi\s*=\s*\{([^}]+)\}", re.IGNORECASE)
_KEY_RE = re.compile(r"@\w+\{([^,\s]+)", re.IGNORECASE)
_EPRINT_RE = re.compile(r"eprint\s*=\s*\{([^}]+)\}", re.IGNORECASE)


def _load_bib_keys_and_dois(bib_path: Path) -> tuple[set[str], set[str], set[str]]:
    """Return (cite_keys, dois, eprints) from an existing .bib file."""
    if not bib_path.exists():
        return set(), set(), set()
    text = bib_path.read_text(encoding="utf-8")
    keys = {m.lower() for m in _KEY_RE.findall(text)}
    dois = {m.strip().lower() for m in _DOI_RE.findall(text)}
    eprints = {m.strip().lower() for m in _EPRINT_RE.findall(text)}
    return keys, dois, eprints


# ---------------------------------------------------------------------------
# Key uniquifier
# ---------------------------------------------------------------------------

def _unique_key(desired: str, existing_keys: set[str]) -> str:
    if desired.lower() not in existing_keys:
        return desired
    suffix_ord = ord("a")
    while f"{desired}{chr(suffix_ord)}".lower() in existing_keys:
        suffix_ord += 1
    return f"{desired}{chr(suffix_ord)}"


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def add_citation(
    bib_path: Path,
    doi: str | None = None,
    arxiv_id: str | None = None,
    *,
    confirm: bool = True,
) -> str:
    """Fetch BibTeX and append to bib_path. Returns the BibTeX string added.

    Args:
        bib_path: Target .bib file.
        doi: DOI to look up via CrossRef.
        arxiv_id: arXiv ID to look up via arXiv API.
        confirm: If True (default), prompt user before writing.
    """
    if not doi and not arxiv_id:
        raise ValueError("Provide either doi or arxiv_id.")

    # Fetch
    if doi:
        doi = normalize_doi(doi)
        try:
            work = fetch_crossref(doi)
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"CrossRef returned HTTP {e.code} for DOI '{doi}'") from e
        bibtex = format_bibtex(work)
    else:
        bibtex = _fetch_arxiv(arxiv_id)

    # Duplicate check
    existing_keys, existing_dois, existing_eprints = _load_bib_keys_and_dois(bib_path)

    if doi and doi.lower() in existing_dois:
        print(f"DOI {doi} already present in {bib_path}. Skipping.", file=sys.stderr)
        return bibtex

    if arxiv_id:
        normalised_eprint = arxiv_id.strip().lower()
        if normalised_eprint in existing_eprints:
            print(f"arXiv:{arxiv_id} already present in {bib_path}. Skipping.",
                  file=sys.stderr)
            return bibtex

    # Ensure unique key
    key_match = _KEY_RE.search(bibtex)
    if key_match:
        original_key = key_match.group(1)
        new_key = _unique_key(original_key, existing_keys)
        if new_key != original_key:
            bibtex = bibtex.replace(f"{{{original_key},", f"{{{new_key},", 1)
            print(f"Key collision: renamed '{original_key}' → '{new_key}'")

    print(bibtex)

    if confirm:
        answer = input(f"\nAppend to {bib_path}? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            print("Aborted.")
            return bibtex

    bib_path.parent.mkdir(parents=True, exist_ok=True)
    with bib_path.open("a", encoding="utf-8") as fh:
        fh.write("\n" + bibtex + "\n")
    print(f"Appended to {bib_path}.")
    return bibtex


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add a citation to a .bib file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--bib", required=True, metavar="FILE",
                        help="Target .bib file (created if absent)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--doi", metavar="DOI",
                       help="DOI to fetch from CrossRef")
    group.add_argument("--arxiv", metavar="ID",
                       help="arXiv ID (e.g. 2301.07041)")
    parser.add_argument("--yes", action="store_true",
                        help="Skip confirmation prompt")
    args = parser.parse_args()

    try:
        add_citation(
            bib_path=Path(args.bib),
            doi=args.doi,
            arxiv_id=args.arxiv,
            confirm=not args.yes,
        )
    except (RuntimeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
