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
```

Run from the project root (`/Users/pablo/Documents/Projects/workout`).

## Pass/Fail Outputs

| Condition | Output |
|-----------|--------|
| DOI resolves, key unique | BibTeX printed; appended after confirmation |
| DOI resolves, key collision | Key renamed `LastnameYEAR_2`; appended |
| DOI already in `.bib` | `DOI already present. Skipping.` (stderr) |
| DOI fails CrossRef (HTTP 404/5xx) | `Error: CrossRef returned HTTP NNN` (stderr); mark claim `TO_VERIFY` in manuscript |
| Network failure | `Error: network failure — <reason>` (stderr) |

## TO_VERIFY Protocol

Any DOI that fails CrossRef resolution must:
1. Be marked `TO_VERIFY` in the manuscript box header (use `toverifybox` environment).
2. NOT be added to `bibliography.bib` until manually resolved.
3. Be entered in the TO_VERIFY appendix tracker table in `main.tex`.
