# TODO: Workout Manuscript Improvement Backlog (ROI-Ordered)

## ROI Formula

ROI = (Impact x Confidence) / EffortScore
EffortScore: S=1, M=2, L=3

## Phase 2: Content Expansion From Notes

### 15) Build a figures program across the manuscript
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: visual synthesis is currently underdeveloped relative to scope.
Targets: [main.tex](main.tex), [sections/04_biomechanics.tex](sections/04_biomechanics.tex), [sections/05_intervention_studies.tex](sections/05_intervention_studies.tex), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex).
Actions:
- For each high-impact study, include one key figure when license-permitted.
- Track source, permission, and caption provenance.
Done when:
- Figures are included only when licensing is explicit; unlicensed figures are omitted.

### 16) Add finger anatomy and crimp-position figure set
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: anatomy nomenclature and grip mechanics need clear visual standardization.
Targets: [sections/04_biomechanics.tex](sections/04_biomechanics.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex).
Actions:
- Source original published diagrams for crimp positions and finger anatomy including joints, ligaments, and pulleys only when license-permitted.
Done when:
- Terminology maps clearly to figures when available, with text-only fallback when licensing prevents reuse.

### 17) Add performance predictor content and correlation figure bank
ROI: 8.0 (Impact 4, Confidence 4, Effort M)
Why: performance predictor relationships need evidence synthesis before figures can be selected; figures only when license-permitted.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/07_discussion.tex](sections/07_discussion.tex).
Actions:
- LLM research prompt ready: [LLM_feedback/prompts/todo_17_and_preston.md](LLM_feedback/prompts/todo_17_and_preston.md) (merged with Preston's note on the 9c test).
- After merging LLM responses: add original source visuals linking climbing grade with finger strength, pull-up metrics, and other supported predictors only when license-permitted.
- Separate correlation from causation throughout.
Done when:
- Performance predictor synthesis is in the manuscript with evidence tiers and explicit uncertainty notes; figures added only where licensing is confirmed.

### ~~18) Create a new comprehensive finger-injury module~~ — DONE
`injury_management.tex` already covers: A2 pulley anatomy/grading (Schöffl I–IV)/diagnosis/conservative+surgical management, flexor tendon strains, skin basics (flappers, chronic thinning), warm-up, load management (10% rule), experience-dependent risk (Sjöman 2023), and a gaps section. Minor secondary injury types (lumbrical, PIP joint, tenosynovitis, TFCC) remain uncovered but do not warrant a new comprehensive module prompt.

### 19) Add equipment ROI section for training tools
ROI: 7.5 (Impact 3, Confidence 5, Effort M)
Why: tool choices are practical and frequently requested by readers.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex) or a new section file.
Actions:
- Rank equipment by bang-for-buck using outcome relevance, cost, and evidence quality.
- Include devices such as specialty hangboards, force devices, and gym attachments.
- Let Claude decide final placement (existing section or new section) during architecture pass.
Done when:
- A reader can make budget-prioritized equipment decisions with evidence context.

### 20) Add scientific measurements deep dive section
ROI: 7.5 (Impact 3, Confidence 5, Effort M)
Why: measurement rigor is central for tracking progression and comparing interventions.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex) or a new section file.
Actions:
- Cover metrics including Tindeq Critical Force, W', peak force asymmetry, and reliability considerations.
- Define interpretation ranges and minimal meaningful changes where available.
- Let Claude decide final placement (existing section or new section) during architecture pass.
Done when:
- The manuscript has a standardized metrics reference with quality caveats.

### 21) Add skincare science and folklore critical review
ROI: 7.5 (Impact 3, Confidence 5, Effort M)
Why: skin-management practice is high-impact in climbing and prone to biased folklore.
Targets: [sections/12_recovery.tex](sections/12_recovery.tex) or a new section file.
Actions:
- Compare dry-management and moisture-management schools using evidence tiers.
- Keep this section text-only with no graphic skin imagery.
- Explicitly mark folklore claims and TO_VERIFY uncertainties.
- Let Claude decide final placement (existing section or new section) during architecture pass.
Done when:
- Skincare guidance is evidence-stratified and bias-aware.

## Phase 4: Agentic Workflow and Collaboration Infrastructure

### 28) Import reusable cite agents and scripts from reference project
ROI: 6.0 (Impact 3, Confidence 4, Effort M)
Why: avoids re-inventing reliable citation automation.
Targets: project tooling and docs.
Actions:
- Review ../BourbakIA/bourbakia/cite/.
- Copy or adapt useful agents and scripts.
- Document provenance and project-specific adjustments.
Done when:
- Citation verification automation runs natively in this project.

### 29) Import critique workflow for iterative quality control
ROI: 6.0 (Impact 3, Confidence 4, Effort M)
Why: structured critique loops improve quality and consistency over time.
Targets: project tooling and docs.
Actions:
- Review ../BourbakIA/bourbakia/critique/.
- Copy or adapt useful critique agents and scripts.
- Integrate into manuscript revision workflow.
Done when:
- A repeatable critique pipeline is available for each revision round.

### 30) Make repo collaboration-ready for community contribution
ROI: 4.0 (Impact 2, Confidence 4, Effort M)
Why: eventual public collaboration is a stated goal.
Targets: repository structure and contributor docs.
Actions:
- Add contribution guidelines for manual and agent-assisted improvements.
- Add issue templates for claim verification, citation fixes, and section improvements.
Done when:
- External contributors can propose high-quality changes with low onboarding friction.

## Phase 5: Technical and QA Polish

### 31) Add claim-level verification appendix
ROI: 6.0 (Impact 3, Confidence 4, Effort M)
Why: transparent provenance supports rigorous review.
Targets: [main.tex](main.tex), [bibliography.bib](bibliography.bib).
Actions:
- Add appendix table with claim id, status label, ESS, citation key(s), DOI state, TO_VERIFY state.
Done when:
- Any claim can be audited in one lookup.

### 32) Add and enforce a manuscript QA checklist
ROI: 6.0 (Impact 3, Confidence 4, Effort M)
Why: prevents recurring regressions across passes.
Targets: [summary.md](summary.md) or new checklist doc.
Actions:
- Include checks for unresolved citations, missing labels or ESS, TO_VERIFY leakage, stale time framing, and LaTeX warning thresholds.
Done when:
- Every major revision records pass or fail checklist outcomes.

### 33) Reduce overfull and underfull warnings in table-heavy sections
ROI: 5.0 (Impact 2, Confidence 5, Effort M)
Why: improves PDF readability and production quality.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L32), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L60), [sections/11_injury_management.tex](sections/11_injury_management.tex#L25).
Actions:
- Improve wrapping and table width strategy.
Done when:
- Warnings are reduced to minimal justified cases.

### 34) Resolve caption warnings and standardize table-note behavior
ROI: 4.0 (Impact 2, Confidence 4, Effort M)
Why: compile hygiene and consistency.
Targets: [main.tex](main.tex), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/10_supplements.tex](sections/10_supplements.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Align caption options and standardize table-note formatting.
Done when:
- Caption warnings are eliminated from build logs.

## Suggested Claude Execution Order

Next session — Content expansion: items 15–21.
Session N — Agentic workflow and collaboration setup: items 28–30.
Session N — QA and technical polish: items 31–34.

## Publication-Readiness Gate

- Every actionable recommendation has status label plus ESS.
- No TO_VERIFY item appears as settled recommendation.
- Folklore claims have explicit prevalence verification.
- Every empirical claim cites [bibliography.bib](bibliography.bib) through cite commands.
- Methods cover all domains and grading workflow.
- Injury guidance is risk-stratified and neutral.
- Build has zero unresolved citations and zero LaTeX errors.

## Integration Check: Notes Fully Captured

- Figures expansion: items 15-17.
- Finger injuries deep dive: item 18.
- Equipment by ROI: item 19.
- Scientific measurements deep dive: item 20.
- Skincare critical review: item 21.
- Strict bibliography and metadata verification: done (Phase 0–1).
- Section numbering redesign: item 26.
- Critique and cite agentic workflow import: items 28-29.
- Neutrality and model-brand removal policy: items 6 and 22.
- Licensed-original-only figure policy: items 15-17 and Figure License Rule.
- Claude-owned section placement decisions: items 19-21 and 26.
