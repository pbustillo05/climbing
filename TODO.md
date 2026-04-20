# TODO: Workout Manuscript Improvement Backlog (ROI-Ordered)

Date: 2026-04-20 (updated from 2026-04-19)
Scope reviewed: [main.tex](main.tex) and all included sections [sections/01_abstract.tex](sections/01_abstract.tex) to [sections/12_recovery.tex](sections/12_recovery.tex), plus notes in [pablo_notes.md](pablo_notes.md).
Primary objective: one rigorous manuscript that integrates intervention science, measurable practice, and verified community knowledge for climbers.

## Author Intent Locked In

1. Audience: primarily personal scientific reference with eventual public sharing on r/climbharder.
2. Scope: one unified manuscript that aims to cover the full climber-training landscape.
3. Knowledge classes: keep both scientific evidence and folklore.
4. Folklore policy: only use FOLKLORE_VERIFIED when prevalence is explicitly verified in independent community sources.
5. Unverified claims policy: unresolved claims must be flagged TO_VERIFY.
6. Injury guidance: neutral and risk-stratified, not uniformly conservative or uniformly aggressive.
7. Evidence grading: use a 0-10 Evidence Strength Score (ESS).
8. Neutral sourcing language: no mention of individual model brands in manuscript body text.
9. Figure policy: include only original source figures with explicit license permission; otherwise include no figure.
10. Section architecture policy: Claude decides final section placement and boundaries based on whole-manuscript coherence.

## Implementation Decisions (2026-04-20)

The following decisions were locked in during the 2026-04-20 planning session and must not be overridden without explicit user instruction.

1. **ESS format**: Extend existing LaTeX boxes — keep `evidencebox`/`bioplausbox`/`folklorebox`, add status label and ESS badge in the box header title argument. Example: `\begin{evidencebox}{Collagen loading · EVIDENCE_BACKED · ESS 6}`. Do NOT replace boxes with inline tags.
2. **Bib expansion workflow**: Use `bourbakia-cite add --doi <DOI> --bib bibliography.bib` (CrossRef auto-fetch) to expand bibliography entries. Any DOI that fails CrossRef resolution is flagged TO_VERIFY in the manuscript and excluded from `bibliography.bib` until manually resolved.
3. **Session focus order**: Phase 0 (items 1–8) → Phase 1 (items 9–14) → Phase 2 (items 15–21). No Phase 2 content expansion begins until Phase 1 is complete.

## Non-Negotiable Global Rules

### Claim Status Labels

- EVIDENCE_BACKED: claim supported by directly cited studies with transparent design and bias context.
- BIOPLAUSIBLE: mechanistically plausible claim with indirect or incomplete intervention support.
- FOLKLORE_VERIFIED: community-held belief with explicit prevalence verification.
- TO_VERIFY: unresolved or provenance-unclear claim pending verification.

Rule: TO_VERIFY items cannot be presented as settled recommendations.

### Evidence Strength Score (ESS 0-10)

- ESS 10: well-powered climbing RCT with low risk of bias and functional outcomes.
- ESS 9: strong climbing RCT with minor limitations.
- ESS 8: climbing RCT with moderate limitations.
- ESS 7: controlled non-randomized climbing intervention or high-quality climbing review.
- ESS 6: prospective climbing cohort or repeated-measures climbing intervention with acceptable controls.
- ESS 5: climbing observational evidence with meaningful confounding or indirectness.
- ESS 4: high-quality adjacent-sport intervention evidence with explicit transfer uncertainty.
- ESS 3: observational adjacent-sport evidence with substantial indirectness.
- ESS 2: mechanistic rationale or expert interpretation without direct intervention support.
- ESS 1: anecdotal or highly limited evidence.
- ESS 0: unreliable, unresolvable, or critically biased source basis.

Rule: every actionable recommendation must include both status label and ESS.

### Citation Rule (Hard Constraint)

- Every empirical citation must exist in [bibliography.bib](bibliography.bib).
- Every citation in prose and summary tables must use cite commands.
- In paper summary tables, first column format should be: Authors \cite{key}.
- Manual plain-text paper references are disallowed in final manuscript state.

### Neutrality Rule

- Do not name specific model vendors in the manuscript body text.
- Methods may state that free-tier frontier LLMs were used for feedback and that Claude Sonnet 4.6 orchestrated synthesis.

### Figure License Rule

- Only use original source figures with explicit license permission.
- Do not redraw, recreate, or approximate restricted figures.
- If license permission is absent, omit the figure and keep text-only synthesis.

## ROI Formula

ROI = (Impact x Confidence) / EffortScore
EffortScore: S=1, M=2, L=3

## Phase 0: Governance and Integrity Lock (highest ROI)

### 1) Make citation rule unbreakable in project policy
ROI: 25.0 (Impact 5, Confidence 5, Effort S)
Why: ensures reproducibility and prevents bibliography drift.
Targets: [CLAUDE.md](CLAUDE.md), [bibliography.bib](bibliography.bib).
Actions:
- Add explicit hard-rule language for citation format and table conventions.
- Add a fail condition for any manual non-cite paper reference.
Done when:
- Policy text clearly forbids non-bibliography citations.

### 2) Build metadata-verification pipeline for bibliography entries
ROI: 12.5 (Impact 5, Confidence 5, Effort M)
Why: source metadata quality is currently a key integrity bottleneck.
Targets: [bibliography.bib](bibliography.bib), [CLAUDE.md](CLAUDE.md).
Actions:
- Copy `add_citation.py` and `fetch_bibtex.py` from `../BourbakIA/bourbakia/cite/` into `scripts/cite/` in this project.
- Use `bourbakia-cite add --doi <DOI> --bib bibliography.bib` to auto-fetch BibTeX from CrossRef for any new or missing citation.
- Any DOI that fails CrossRef resolution must be marked TO_VERIFY in the manuscript and excluded from `bibliography.bib` until resolved manually.
- Document invocation and pass/fail outputs in `scripts/cite/README.md`.
Done when:
- All bib entries can be machine-checked for DOI resolution and metadata consistency.
- Scripts are present in `scripts/cite/` and invocable without additional setup.

### 3) Enforce manuscript-wide claim labeling legend
ROI: 12.5 (Impact 5, Confidence 5, Effort M)
Why: prevents mixed certainty language.
Targets: [main.tex](main.tex), [sections/05_intervention_studies.tex](sections/05_intervention_studies.tex), [sections/07_discussion.tex](sections/07_discussion.tex), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/10_supplements.tex](sections/10_supplements.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Extend existing `evidencebox`/`bioplausbox`/`folklorebox` box headers to include status label and ESS badge in the title argument: e.g. `\begin{evidencebox}{Recommendation title · EVIDENCE_BACKED · ESS 7}`. Do NOT replace boxes with inline tags.
- Apply EVIDENCE_BACKED, BIOPLAUSIBLE, FOLKLORE_VERIFIED, TO_VERIFY labels consistently across all recommendation boxes.
Done when:
- No actionable recommendation appears without a status label.
- All box headers follow the `Title · LABEL · ESS N` pattern.

### 4) Implement ESS 0-10 across actionable content
ROI: 12.5 (Impact 5, Confidence 5, Effort M)
Why: creates graded evidence confidence instead of binary framing.
Targets: [sections/07_discussion.tex](sections/07_discussion.tex), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/10_supplements.tex](sections/10_supplements.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Add ESS next to each recommendation and one-line rationale for low ESS values.
Done when:
- Every recommendation has status label plus ESS.

### 5) Add TO_VERIFY quarantine workflow and tracker
ROI: 12.5 (Impact 5, Confidence 5, Effort M)
Why: unresolved claims are currently too close to prescriptive guidance.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L98), [sections/10_supplements.tex](sections/10_supplements.tex#L136), [sections/11_injury_management.tex](sections/11_injury_management.tex#L228), [sections/12_recovery.tex](sections/12_recovery.tex#L243), [main.tex](main.tex).
Actions:
- Add TO_VERIFY labels and one consolidated appendix tracker table.
- Exclude TO_VERIFY items from high-confidence recommendations.
Done when:
- No TO_VERIFY claim is written as settled guidance.

### 6) Enforce neutrality language and remove model-brand mentions
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: final manuscript should be methodologically transparent without brand-specific noise.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L8), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L227), [sections/10_supplements.tex](sections/10_supplements.tex#L8), [sections/03_methods.tex](sections/03_methods.tex).
Actions:
- Remove named-vendor references from body text.
- Keep a compact neutral methods statement about LLM-assisted feedback and orchestration.
Done when:
- Brand names are absent from manuscript body.

### 7) Define folklore verification criteria and thresholds
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: folklore is allowed, but only if prevalence is explicitly established.
Targets: [sections/06_practitioner_consensus.tex](sections/06_practitioner_consensus.tex), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Require at least three independent climbing-community sources for FOLKLORE_VERIFIED status.
- Move unverified folklore candidates to TO_VERIFY.
Done when:
- Every folklore claim has traceable prevalence support.

### 8) Build injury-risk stratification framework and apply globally
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: aligns guidance with neutral risk communication.
Targets: [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Define strata (Low, Moderate, High, Very High).
- For each recommendation: include risk tier, estimated risk range, and uncertainty.
- Separate injury incidence from return-to-sport risk.
Done when:
- Injury guidance is consistently risk-tiered and neutral.

## Phase 1: Evidence Integrity in Existing Sections

### 9) Unify citation usage in sections 09-12
ROI: 12.5 (Impact 5, Confidence 5, Effort M)
Why: manual DOI text still undermines bibliographic consistency. ~30 studies cited in these sections are missing from bibliography.bib.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/10_supplements.tex](sections/10_supplements.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex), [bibliography.bib](bibliography.bib).
Actions:
- Step 1: Extract all plain-text citations from sections 09–12 (grep for `\href{https://doi` and manual author/journal strings).
- Step 2: Batch-expand bibliography.bib using `bourbakia-cite add --doi <DOI> --bib bibliography.bib` for each missing study. Flag any unresolvable DOIs as TO_VERIFY.
- Step 3: Replace all `\href{DOI}` and plain-text paper strings with `\cite{key}` commands.
- Step 4: Update table first columns to `Authors \cite{key}` pattern.
Done when:
- `grep -rn '\\href{https://doi' sections/09*.tex sections/10*.tex sections/11*.tex sections/12*.tex` returns zero results.
- Empirical claims and tables consistently use bibliography keys.

### 10) Rewrite Methods to match full manuscript scope
ROI: 12.5 (Impact 5, Confidence 5, Effort M)
Why: current methods do not yet describe all domains.
Targets: [sections/03_methods.tex](sections/03_methods.tex#L4).
Actions:
- Add domain-specific search and inclusion criteria.
- Add ESS and status-label assignment workflow.
- Add handling rules for adjacent-sport transfer evidence.
Done when:
- Methods can reproduce evidence decisions across all sections.

### 11) Resolve known citation metadata conflicts
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: unresolved metadata contradictions reduce trust.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L8), [bibliography.bib](bibliography.bib#L150).
Actions:
- Verify canonical source metadata and normalize references.
Done when:
- No duplicate-conflict records remain for one study.

### 12) Add evidence summary tables for sections 09-12
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: high-density recommendation sections need auditable study summaries.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/10_supplements.tex](sections/10_supplements.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Include design, sample, protocol, primary outcome, effect size, CI, p-value, endpoint type, and quality score.
Done when:
- Every EVIDENCE_BACKED recommendation maps to table rows.

### 13) Reframe unsupported precision in numerical thresholds
ROI: 8.0 (Impact 4, Confidence 4, Effort M)
Why: avoids overconfident guidance when support is weak.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L124), [sections/12_recovery.tex](sections/12_recovery.tex#L339).
Actions:
- Replace brittle cutoffs with ranges where needed.
- Add ESS and uncertainty qualifiers.
Done when:
- Low-support thresholds are not presented as definitive.

### 14) Distinguish functional versus surrogate outcomes for all key recommendations
ROI: 8.0 (Impact 4, Confidence 4, Effort M)
Why: prevents over-transfer from proxy outcomes.
Targets: [sections/05_intervention_studies.tex](sections/05_intervention_studies.tex), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/10_supplements.tex](sections/10_supplements.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Tag major findings by endpoint type and tune recommendation strength accordingly.
Done when:
- Endpoint class is explicit at recommendation sites.

## Phase 2: Content Expansion From Notes

**Status: DEFERRED** — begin only after all Phase 1 items (1–14) are complete.

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

### 17) Add correlation figure bank for climbing performance predictors
ROI: 8.0 (Impact 4, Confidence 4, Effort M)
Why: performance relationships are easier to interpret through comparative plots.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/07_discussion.tex](sections/07_discussion.tex).
Actions:
- Add original source visuals linking climbing grade with finger strength, pull-up metrics, and other supported predictors only when license-permitted.
- Separate correlation from causation in figure captions.
Done when:
- Predictor relationships are visualized only with licensed originals and explicit uncertainty notes.

### 18) Create a new comprehensive finger-injury module
ROI: 8.0 (Impact 4, Confidence 4, Effort M)
Why: current injury coverage is not yet structured at the required depth.
Targets: [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Structure with subsections: injury types, prevention, warm-up deep dive, symptoms, diagnostics, rehab protocols.
- Cross-link guidance to risk strata and ESS.
Done when:
- Finger-injury pathway is complete from prevention through return-to-climb.

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

## Phase 3: Single-Manuscript Coherence and Structure

### 22) Remove process or workflow language from body text
ROI: 20.0 (Impact 4, Confidence 5, Effort S)
Why: improves scientific tone and public readability.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L8), [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex#L227), [sections/10_supplements.tex](sections/10_supplements.tex#L8).
Actions:
- Remove workflow commentary and retain only neutral methodology.
Done when:
- Manuscript reads as scientific synthesis, not process log.

### 23) Expand conclusion to represent full manuscript breadth
ROI: 10.0 (Impact 5, Confidence 4, Effort M)
Why: current conclusion underrepresents expanded domains.
Targets: [sections/08_conclusion.tex](sections/08_conclusion.tex#L4).
Actions:
- Add concise takeaways for supplements, injuries, measurements, equipment, and recovery.
Done when:
- Conclusion reflects all major domains and uncertainty levels.

### 24) Update abstract for expanded scope and certainty framework
ROI: 6.0 (Impact 3, Confidence 4, Effort M)
Why: abstract should match final manuscript content.
Targets: [sections/01_abstract.tex](sections/01_abstract.tex#L3).
Actions:
- Add one concise line each for new domains and ESS framing.
Done when:
- Abstract is aligned with final section coverage.

### 25) Consolidate repeated caveats into a compact template language
ROI: 7.5 (Impact 3, Confidence 5, Effort M)
Why: improves scanability while preserving uncertainty signaling.
Targets: [sections/09_weekly_integration.tex](sections/09_weekly_integration.tex), [sections/10_supplements.tex](sections/10_supplements.tex), [sections/11_injury_management.tex](sections/11_injury_management.tex), [sections/12_recovery.tex](sections/12_recovery.tex).
Actions:
- Standardize caveat phrasing tied to labels and ESS.
Done when:
- Caveats remain clear with less repetition.

### 26) Redesign section file numbering and naming scheme
ROI: 6.0 (Impact 3, Confidence 4, Effort M)
Why: current numbering no longer reflects actual manuscript logic.
Targets: [main.tex](main.tex), [sections/](sections/).
Actions:
- Claude proposes final canonical section order and section boundaries using whole-document coherence.
- Rename section files based on that architecture decision.
- Update all input references and any tooling assumptions.
Done when:
- File names reflect final architecture and compile cleanly.

### 27) Clean cross-references and unused labels
ROI: 6.0 (Impact 3, Confidence 4, Effort M)
Why: improves navigability and editorial hygiene.
Targets: [main.tex](main.tex#L63), [sections/05_intervention_studies.tex](sections/05_intervention_studies.tex#L109), [sections/06_practitioner_consensus.tex](sections/06_practitioner_consensus.tex#L3), [sections/10_supplements.tex](sections/10_supplements.tex#L453).
Actions:
- Remove orphan labels or add meaningful references.
Done when:
- Labels and references are functionally aligned.

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

Session 2 — Governance lock: items 1–8.
Session 3 — Bib expansion + citation migration: items 1, 2, 9 (cite{} conversion of 09–12).
Session 4 — ESS scoring + claim labels + TO_VERIFY tracker: items 3, 4, 5.
Session 5 — Methods rewrite + evidence tables + precision reframe: items 10, 11, 12, 13, 14.
Session 6+ (after Phase 1 complete) — Content expansion: items 15–21.
Session N — Manuscript coherence and architecture: items 22–27.
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
- Strict bibliography and metadata verification: items 1-2, 9.
- Section numbering redesign: item 26.
- Critique and cite agentic workflow import: items 28-29.
- Neutrality and model-brand removal policy: items 6 and 22.
- Licensed-original-only figure policy: items 15-17 and Figure License Rule.
- Claude-owned section placement decisions: items 19-21 and 26.
