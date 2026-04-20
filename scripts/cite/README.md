# Citation Verification Scripts

Copied from `../BourbakIA/bourbakia/cite/`. Provides CrossRef-backed BibTeX auto-fetch.

## Invocation

```bash
# Add a single citation by DOI
python -m scripts.cite.add_citation --doi 10.5114/biolsport.2023.113295 --bib bibliography.bib

# Confirm without prompt
python -m scripts.cite.add_citation --doi 10.5114/biolsport.2023.113295 --bib bibliography.bib --yes

# Fetch BibTeX only (no file write)
python -m scripts.cite.fetch_bibtex 10.5114/biolsport.2023.113295

# Rekey bibliography entries to alpha-style keys and update cites
python -m scripts.cite.rekey_alpha_keys --bib bibliography.bib --files main.tex sections/**/*.tex --yes

# Convert DOI href/plain DOI references to \cite{key} using bibliography mappings
python -m scripts.cite.convert_doi_to_cite --bib bibliography.bib --files sections/09_weekly_integration.tex sections/10_supplements.tex sections/11_injury_management.tex sections/12_recovery.tex --yes
```

Run from the project root (`/Users/pablo/Documents/Projects/workout`).

## Key Style

Bib keys are generated in alpha-like format:
- 1 author: first 3 letters of family name + 2-digit year (`KIV07`)
- 2-4 authors: first letter of each family name + 2-digit year (`KHKT07`)
- 5+ authors: first 3 family initials + `E` + 2-digit year (`MABE11`)

On collisions, keys get letter suffixes (`KIV07a`, `KIV07b`, ...).

## Pass/Fail Outputs

| Condition | Output |
|-----------|--------|
| DOI resolves, key unique | BibTeX printed; appended after confirmation |
| DOI resolves, key collision | Key renamed with letter suffix (e.g., `KIV07a`); appended |
| DOI already in `.bib` | `DOI already present. Skipping.` (stderr) |
| DOI fails CrossRef (HTTP 404/5xx) | `Error: CrossRef returned HTTP NNN` (stderr); mark claim `TO_VERIFY` in manuscript |
| Network failure | `Error: network failure — <reason>` (stderr) |

## TO_VERIFY Protocol

Any DOI that fails CrossRef resolution must:
1. Be marked `TO_VERIFY` in the manuscript box header (use `toverifybox` environment).
2. NOT be added to `bibliography.bib` until manually resolved.
3. Be entered in the TO_VERIFY appendix tracker table in `main.tex`.
