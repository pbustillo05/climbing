#!/usr/bin/env python3
"""Fetch authoritative BibTeX for a DOI from the CrossRef API.

Usage:
    python -m bourbakia.cite.fetch_bibtex 10.1007/s40544-022-0594-9
    python -m bourbakia.cite.fetch_bibtex https://doi.org/10.1007/s40544-022-0594-9

Prints a BibTeX entry to stdout. Metadata comes directly from CrossRef, so
author names, titles, and journal names are authoritative — not model-generated.
"""

from __future__ import annotations

import json
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

BTYPE_MAP = {
    "journal-article": "article",
    "book": "book",
    "book-chapter": "incollection",
    "proceedings-article": "inproceedings",
    "monograph": "book",
    "report": "techreport",
    "dissertation": "phdthesis",
}

_UA = "BourbakIA/0.1 (https://github.com/bourbakia/bourbakia)"


def _ascii_letters(text: str) -> str:
    """Return uppercase ASCII letters from text.

    This keeps key generation stable for names that include accents or
    punctuation, while preserving deterministic behavior.
    """
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return "".join(ch for ch in ascii_text if ch.isalpha()).upper()


def make_alpha_key(family_names: list[str], year: str) -> str:
    """Create an alpha-style citation key base from author families and year.

    Rules:
    - 1 author: first 3 letters of family name
    - 2-4 authors: first letter of each family name
    - 5+ authors: first letters of first 3 family names + 'E' (et al.)
    - year suffix: last 2 digits (or '00' fallback)
    """
    cleaned = [_ascii_letters(name) for name in family_names]
    cleaned = [name for name in cleaned if name]

    if not cleaned:
        base = "ANO"
    elif len(cleaned) == 1:
        base = cleaned[0][:3]
    elif len(cleaned) <= 4:
        base = "".join(name[0] for name in cleaned)
    else:
        base = "".join(name[0] for name in cleaned[:3]) + "E"

    digits = "".join(ch for ch in year if ch.isdigit())
    suffix = digits[-2:] if len(digits) >= 2 else "00"
    return f"{base}{suffix}"


def normalize_doi(doi: str) -> str:
    doi = doi.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.lower().startswith(prefix):
            return doi[len(prefix):]
    return doi


def fetch_crossref(doi: str) -> dict:
    doi = normalize_doi(doi)
    encoded = urllib.parse.quote(doi, safe="/")
    url = f"https://api.crossref.org/works/{encoded}"
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())["message"]


def get_year(work: dict) -> str:
    for field in ("published", "published-print", "published-online", "issued"):
        parts = work.get(field, {}).get("date-parts", [[]])
        if parts and parts[0]:
            return str(parts[0][0])
    return "????"


def format_authors(work: dict) -> str:
    authors = work.get("author", [])
    parts = []
    for a in authors:
        family = a.get("family", "")
        given = a.get("given", "")
        if family and given:
            parts.append(f"{family}, {given}")
        elif family:
            parts.append(family)
        elif given:
            parts.append(given)
    return " and ".join(parts) if parts else "Unknown"


def make_key(work: dict) -> str:
    authors = work.get("author", [])
    year = get_year(work)
    families = [a.get("family", "") for a in authors if a.get("family")]
    return make_alpha_key(families, year)


def format_bibtex(work: dict) -> str:
    btype = BTYPE_MAP.get(work.get("type", ""), "misc")
    key = make_key(work)
    year = get_year(work)
    doi = work.get("DOI", "")
    title = (work.get("title") or ["Untitled"])[0]
    authors = format_authors(work)

    fields: list[tuple[str, str]] = [
        ("author", authors),
        ("title", title),
        ("year", year),
        ("doi", doi),
    ]

    if btype == "article":
        journal = (work.get("container-title") or [""])[0]
        if journal:
            fields.append(("journal", journal))
        if volume := work.get("volume"):
            fields.append(("volume", volume))
        if issue := work.get("issue"):
            fields.append(("number", issue))
        if pages := work.get("page"):
            fields.append(("pages", pages))
    elif btype in ("incollection", "inproceedings"):
        booktitle = (work.get("container-title") or [""])[0]
        if booktitle:
            fields.append(("booktitle", booktitle))
        if publisher := work.get("publisher"):
            fields.append(("publisher", publisher))
    elif btype == "book":
        if publisher := work.get("publisher"):
            fields.append(("publisher", publisher))

    lines = [f"@{btype}{{{key},"]
    for name, value in fields:
        lines.append(f"  {name:<12} = {{{value}}},")
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m bourbakia.cite.fetch_bibtex <doi>", file=sys.stderr)
        sys.exit(1)

    doi = sys.argv[1]
    try:
        work = fetch_crossref(doi)
    except urllib.error.HTTPError as e:
        print(f"Error: CrossRef returned HTTP {e.code} for DOI '{normalize_doi(doi)}'",
              file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error: network failure — {e.reason}", file=sys.stderr)
        sys.exit(1)

    print(format_bibtex(work))


if __name__ == "__main__":
    main()
