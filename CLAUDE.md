# Workout Project Guide (Claude Code)

## Goal
Maintain literature reviews on exercise science. Build personalised workout plans. Analyse training progress statistically.

## Author Intent (Locked)

1. **Audience**: primarily personal scientific reference with eventual public sharing on r/climbharder.
2. **Scope**: one unified manuscript covering the full climber-training landscape.
3. **Knowledge classes**: keep both scientific evidence and folklore.
4. **Folklore policy**: only use FOLKLORE_VERIFIED when prevalence is explicitly verified in ≥3 independent community sources.
5. **Unverified claims**: flag TO_VERIFY; never present as settled guidance.
6. **Injury guidance**: neutral and risk-stratified — not uniformly conservative or uniformly aggressive.
7. **Evidence grading**: use ESS 0–10.
8. **Neutrality**: no mention of individual model brands in manuscript body text.
9. **Figure policy**: include only original source figures with explicit license permission; do not redraw, recreate, or approximate restricted figures; omit and keep text-only synthesis when permission is absent.
10. **Section architecture**: Claude decides final section placement and boundaries based on whole-manuscript coherence.

## Scientific Rigor Standard

### Citation and study analysis
Every empirical claim requires a verified DOI or stable URL. For each cited study report:
- **Design**: study type (RCT, cohort, cross-sectional, case series), allocation concealment, blinding, control condition.
- **Sample**: n, sex, training status, attrition.
- **Protocol**: intervention dose (frequency, intensity, duration, volume), outcome measures, follow-up length.
- **Findings**: primary outcome with effect size and 95% CI, p-value, and whether the outcome is a surrogate (e.g., dynamometric) or functional (e.g., on-wall performance, grade).
- **Limitations**: anything that constrains generalisation (small n, homogeneous sample, short follow-up, lack of blinding, industry funding).
- **Quality rating**: PEDro score for RCTs; GRADE or equivalent for reviews; note if only a conference abstract.

Do not cite a study without confirming the DOI resolves. Do not assert a finding beyond what the study's design supports.

### Evidence tiers
Every substantive claim must be labelled:
- **Evidence-backed**: supported by peer-reviewed intervention data with adequate controls; cite specific studies.
- **Bioplausible**: mechanistically plausible from physiology or biomechanics, but no direct controlled intervention evidence exists; state the mechanism and the gap.
- **Folklore**: community consensus, coaching heuristic, or practitioner claim without empirical support; source explicitly (e.g., `r/climbharder`, Lattice Training blog, specific YouTube video, coaching book with edition).

Do not promote a Folklore claim to Bioplausible without a stated mechanism. Do not promote a Bioplausible claim to Evidence-backed without a cited RCT or systematic review.

### Writing style
Dense, precise, information-complete. Every sentence carries a fact, a number, a constraint, or a classification that would be lost if the sentence were removed. No hedging filler, no transitional summaries, no repetition of what was just stated. Numbers over words: write `4–8 weeks`, `≥80% MFS`, `SDM = 0.41 (95% CI 0.03–0.80)`, not "several weeks" or "high intensity" or "a moderate effect." Flag contested or unverified claims explicitly rather than softening them with vague language.

## Deliverables

**Literature reviews**: structured by topic; each study in a summary table (design, n, protocol, primary outcome, effect size, quality score) plus narrative synthesis; findings grouped by evidence tier; explicit statement of what the literature cannot yet answer.

**Workout plans**: weekly structure with session labels; each exercise with sets × reps or time, load as %1RM / RPE / RIR, rest intervals; progression rule as a concrete threshold (e.g., "add 2.5 kg when all sets completed at RIR ≥ 2 for two consecutive sessions"); deload trigger and protocol; injury-risk flags for any movement classified as high-load on vulnerable structures.

**Progress analysis**: adherence rate, weekly volume per muscle group, rolling 4-week e1RM trend per lift, flag any week where volume drops >20% below 4-week average.

## Decision Rules
- If inputs are incomplete, ask only the minimum needed questions before proceeding.
- Prioritise injury-risk management and sustainable progression over aggressive loading.
- Use measurable thresholds, not vague advice.
- When evidence is absent or weak, say so explicitly and classify accordingly — do not fill the gap with confidence.

## Manuscript Governance Rules (Hard Constraints)

### Citation Rule — Fail Condition
Every empirical citation in the manuscript body and summary tables **must** use a `\cite{key}` command referencing an entry in `bibliography.bib`. Any bare `\href{https://doi.org/...}` or plain-text author/year paper reference in body prose or table first-columns is a governance violation. The only permitted DOI text is inside `bibliography.bib` entries themselves. Fail condition: `grep -rn '\\href{https://doi' sections/` returns any result.

### Bib Expansion Workflow
Use `python -m scripts.cite.add_citation --doi <DOI> --bib bibliography.bib` to auto-fetch BibTeX from CrossRef. Any DOI that fails CrossRef resolution must be marked `TO_VERIFY` in the manuscript and excluded from `bibliography.bib` until manually resolved.

### Claim Status Labels (Mandatory)
Every actionable recommendation and evidence-tier box must carry one of:
- **EVIDENCE_BACKED**: supported by directly cited studies with transparent design and bias context.
- **BIOPLAUSIBLE**: mechanistically plausible, indirect or incomplete intervention support.
- **FOLKLORE_VERIFIED**: community-held belief with explicit prevalence verification from ≥3 independent climbing-community sources (e.g., r/climbharder + coach blog + published coaching book). Fewer than 3 verifiable sources → mark TO_VERIFY.
- **TO_VERIFY**: unresolved or provenance-unclear claim. Must NOT be presented as settled guidance.

### Evidence Strength Score (ESS 0–10)
Every actionable recommendation must carry both a status label and an ESS:
- ESS 10: well-powered climbing RCT, low risk of bias, functional outcomes.
- ESS 9: strong climbing RCT with minor limitations.
- ESS 8: climbing RCT with moderate limitations.
- ESS 7: controlled non-randomized climbing intervention or high-quality climbing review.
- ESS 6: prospective climbing cohort or repeated-measures climbing intervention, acceptable controls.
- ESS 5: climbing observational evidence with meaningful confounding.
- ESS 4: high-quality adjacent-sport intervention with explicit transfer uncertainty.
- ESS 3: observational adjacent-sport evidence, substantial indirectness.
- ESS 2: mechanistic rationale or expert interpretation, no direct intervention support.
- ESS 1: anecdotal or highly limited evidence.
- ESS 0: unreliable, unresolvable, or critically biased source basis.

### Box Header Format (Mandatory)
All `evidencebox`, `bioplausbox`, `folklorebox`, and `toverifybox` headers must follow the pattern:
```
\begin{evidencebox}{Recommendation title · EVIDENCE_BACKED · ESS 7}
```
Do NOT replace boxes with inline tags.

### Neutrality Rule
Do not name specific LLM model vendors in manuscript body text. Methods may state that free-tier frontier LLMs were used for multi-source feedback and that synthesis was orchestrated programmatically.

### Abstract and Conclusion Maintenance (Mandatory)
Whenever a significant piece of content is added to any section (new domain coverage, new summary table, new subsection with actionable recommendations, or new evidence box), the abstract and conclusion must be updated in the same pass:
- **Abstract**: add or update the domain's evidence summary sentence and ESS range; keep total length ≤ 4 paragraphs.
- **Conclusion**: add or update the domain subsection with ≤ 3 sentences covering the key finding, the strongest evidence (ESS + study), and the primary gap.
Fail condition: a section contains content not reflected in either the abstract or conclusion.

### Scientific Tone Rule
Manuscript body text must not contain process or workflow commentary (e.g., "previously flagged," "bibliography entry has been corrected," "confirmed across multiple literature queries"). Retain only neutral methodology statements. Methods section is the only permitted location for workflow description.

### Caveat Standardisation
Use the `\singlesource` macro (defined in `main.tex`) for all vanilla single-source footnotes. Custom footnotes with additional qualifications (Mendelian randomisation caveats, specific study qualifiers) may remain as explicit `\footnote{}` calls. Do not repeat the same caveat sentence verbatim without using the macro.

### Injury-Risk Stratification
Injury guidance must use explicit risk strata:
- **Low**: estimated incidence <5%/year, manageable with standard precautions.
- **Moderate**: 5–20%/year or context-dependent, requires specific monitoring.
- **High**: >20%/year or high consequence, explicit mitigation required.
- **Very High**: near-certain injury without intervention, contraindicated without medical supervision.
Separate injury incidence from return-to-sport risk. Flag uncertainty when incidence data are absent.
