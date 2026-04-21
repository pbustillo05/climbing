Now I have a thorough understanding of the document. Let me conduct the exhaustive web searches.Now I have enough to write a comprehensive critique. The research has been extensive. Here is my full review.

---

# Exhaustive Critique & Literature Review: Supplements Section

## Preamble

The section is one of the better-evidenced pieces of climbing supplement writing I've encountered — the evidence tiering system, the single-source footnoting, and the frank statement that no climbing-specific supplement has a functional-outcome RCT are all commendable. What follows is not a condemnation but a systematic audit. I have organized my findings by severity.

---

## CRITICAL ERRORS

### 1. Catastrophic Bibliography Error: `\cite{WTNZ18}` Points to the Wrong Paper

**Location:** Section 5.3 (Caffeine), line 465.

The text reads: `Grgic et al.\ (2020, \textit{Br J Sports Med} 54:681--688; \cite{WTNZ18})`.

In the `.bib` file, `WTNZ18` resolves to:
> Windt, Johann; Taylor, David; Nabhan, Dustin; Zumbo, Bruno D. "What is unified validity theory and how might it contribute to research and practice with athlete self-report measures." *BJSM* 53(19):1202-1203, 2018.

This is an entirely unrelated paper about athlete self-report questionnaire validity. The correct paper is Grgic et al., "Wake up and smell the coffee: caffeine supplementation and exercise performance — an umbrella review of 21 published meta-analyses," DOI: `10.1136/bjsports-2018-100278`. The citation key `WTNZ18` appears to have been a transposition or accidental reuse. **Every claim in that paragraph citing Grgic 2020 is currently unverified in the bibliography.**

---

### 2. Factual Error: "No climbing-specific RCT" for Creatine

**Location:** Section 5.4 (Creatine Monohydrate), current text states: "No climbing-specific RCT has measured creatine effects on boulder problem performance, maximum hang time, or campus board output in trained climbers."

This is incorrect. There is a published climbing-specific creatine RCT:

> Doran DA & Godfrey A. "Effects of creatine supplementation on upper body power output in elite rock climbers." *Biology of Sport* 18(1):55–69, 2001.

Eight elite rock climbers (French 7a–8b+) were randomised in a double-blind matched-pairs design to creatine (20g/day loading, 5 days) or placebo and performed 5×15s arm-cranking Wingate tests separated by 120s recovery. Results: no significant improvement in peak power or mean power output, but end power (POend) was significantly higher in the creatine group (p=0.05), suggesting improved fatigue resistance at the end of repeated high-intensity efforts. Body mass did not change significantly. This is a directly relevant, if older and limited (n=8), climbing-specific creatine RCT. The claim must be corrected to acknowledge this study and interpret it appropriately (arm-crank ergometer, not on-wall; n=8; partial benefit only).

---

### 3. Factual Error: Ruiz-López 2026 Is NOT "The Only Published Climbing-Specific Caffeine RCT"

**Location:** Section 5.6 (Caffeine), text states: "This is the only published climbing-specific caffeine RCT."

This is incorrect. There is an earlier climbing-specific caffeine RCT:

> Cabañes A, Salinero JJ, Del Coso J. "La ingestión de una bebida energética con cafeína mejora la fuerza-resistencia y el rendimiento en escalada deportiva." *Archivos de Medicina del Deporte* 30(156):215–220, 2013.

Design: DB crossover, n=9 non-professional rock climbers, 3mg/kg caffeine via energy drink vs. placebo, 60 min pre-testing. Outcomes included a maximal-velocity pull-up test, a reps-to-failure pull-up test, handgrip dynamometry, and **actual climbing time on a route** (V+ difficulty). Results: climbing time was significantly reduced with caffeine vs. placebo (257.6±108.2s vs. 308.3±142.4s; p=0.042); pull-up reps were improved (p=0.050); total pull-up power increased (p=0.04); dominant handgrip improved (p<0.01). This is a positive result (though confounded by other energy drink constituents and n=9 is small). This study should be incorporated and contrasted with Ruiz-López 2026's null result — together they suggest heterogeneity of effect that may depend on population (non-professional vs. advanced), dose, and metric.

Note: This study is published in a Spanish-language journal without a DOI in standard resolvers. The ResearchGate entry does not list a DOI, but the article reference is fully verifiable from Dialnet.

`[https://dialnet.unirioja.es/servlet/articulo?codigo=8613750 | Cabañes A, Salinero JJ, Del Coso J | La ingestión de una bebida energética con cafeína mejora la fuerza-resistencia y el rendimiento en escalada deportiva]`

---

## SIGNIFICANT ERRORS / INACCURACIES

### 4. Beta-Alanine: Hobson 2012 Described as k=15 RCTs — Technically Imprecise

The text states: `Hobson et al.\ (2012, \textit{Amino Acids}, meta-analysis, k=15 RCTs)`. The actual paper included 15 published *manuscripts* (not 15 discrete RCTs), which reported results from 57 measures across 23 exercise tests using 18 supplementation regimes and 360 participants. Calling it `k=15 RCTs` is a loose description that will look sloppy to reviewers. More accurate: "k=15 manuscripts, 57 exercise measures." The effect size of 0.374 (IQR 0.140–0.747) is the overall median effect size, not a 95% CI for the 60–240s subgroup; the text conflates two distinct statistical quantities. Also of note: this 0.374 is the **median** effect size with IQR, not Hedges' g — while Hobson 2012 used the same value, the distinction between a median ES with IQR and a conventional Hedges' g with 95% CI matters and should be clarified in your text.

### 5. Beta-Alanine: Trexler 2015 Figures Misattributed

The text cites Trexler et al. (2015, JISSN) for: `k=57 studies; mean performance improvement +2.85% (95% CI 0.37--10.49); Hedges g = 0.374 for 60--240 s efforts specifically.` However, Trexler et al. (2015) is the **ISSN Position Stand** (not primarily a new meta-analysis), and the numbers are substantially drawn from Hobson 2012. There is a separate Saunders et al. (2017) meta-analysis in *BJSM* with more studies (k=40 studies, n=1461 participants) reporting a smaller overall effect size of ES=0.18 (95% CI 0.08–0.28) — which is more conservative than what the section implies. This 2017 update is entirely absent from the text, and given the lower effect size in the later, larger meta-analysis, its omission inflates the apparent strength of the evidence.

`[10.1136/bjsports-2016-096396 | Saunders B et al. | β-alanine supplementation to improve exercise capacity and performance: a systematic review and meta-analysis]`

### 6. Sas-Nowosielski 2021: The Text Says n=15 "With 1 Excluded" — This Requires Verification

The text says "small sample (n=15, with 1 excluded)," implying analyzed n=14. This specific detail was not confirmed in my searches and should be flagged. The published abstract reports n=15; any exclusion post-randomization should be addressed in the paper's methods and is worth directly verifying from the full text before publication.

### 7. Omega-3 Mendelian Randomization: Clarify Publication Status and Multiple Testing

The text cites this as a single-source claim that "requires independent verification." I can confirm the paper now has a published DOI: Wang B et al., *Medicine* 105(14):e48076, April 2026. DOI: `10.1097/MD.0000000000048076`. The footnote should be updated to remove the "requires verification" flag now that it has a verified DOI. However, an important nuance the text does not mention: the paper itself states the result is **nominal (p=0.020) and not significant after multiple testing correction**, and further states "further research is needed to confirm this relationship." Your text should reflect this level of uncertainty — the claim as written ("+18% increase") is accurate but presented without noting that this did not survive multiple correction.

`[10.1097/MD.0000000000048076 | Wang B, Li Z, Zhou R, Chen J, Liu M, Zhang L | The causal relationship between Omega-3 fatty acids and Achilles Tendinitis risk: A two-sample Mendelian randomization study in European populations]`

---

## MAJOR GAPS IN THE LITERATURE COVERAGE

### Gap 1: Sodium Bicarbonate — Completely Absent, Arguably the Most Relevant Omission

The section covers beta-alanine (intracellular H+ buffering via carnosine) but entirely omits sodium bicarbonate (NaHCO₃), which works via **extracellular** bicarbonate buffering — a mechanistically complementary and in many ways more potent acute ergogenic. NaHCO₃ is classified as a Group A (evidence-supported) ergogenic aid by the IOC 2018 consensus statement alongside caffeine and creatine. Standard dose: 0.3 g/kg body mass, 60–90 min pre-exercise. Evidence base: performance improvements demonstrated in high-intensity efforts of 1–7 minutes (exactly the pump-zone range for sport climbing), with an effect size comparable to or larger than beta-alanine in single-dose acute protocols. GI side effects (nausea, cramping, diarrhea) are the primary practical limitation; encapsulated "slow-release" bicarbonate and hydrogel delivery formats partially mitigate this.

For climbing, sodium bicarbonate is discussed in some climbing nutrition literature as bioplausible for forearm pump management — and crucially, the combination of beta-alanine + sodium bicarbonate (targeting both intra- and extracellular buffering) is discussed in the literature with some evidence of additive effects. A 2024 meta-analysis (Curran-Bowen et al., *Biology of Sport*, DOI: `10.5114/biolsport.2024.132997`) examined this combination.

`[10.5114/biolsport.2024.132997 | Curran-Bowen T, da Silva AG, Barreto G, Buckley J, Saunders B | Sodium bicarbonate and beta-alanine supplementation: Is combining both better than either alone? A systematic review and meta-analysis]`

### Gap 2: Dietary Nitrate (Beetroot Juice) — Absent, Now Has a Climbing-Specific RCT

There is a **direct climbing-specific RCT** on beetroot juice that the section misses entirely: Berlanga et al. (2023), Journal of Human Kinetics, DOI: `10.5114/jhk/161812`.

Design: DB crossover, n=10 amateur male sport climbers (age 28.8±3.7y), 70mL BJ (6.4 mmol NO₃⁻) vs. nitrate-depleted placebo, 150 min pre-testing. Outcome battery included the half-crimp test, pull-up to failure, isometric handgrip, CMJ, and SJ. All outcomes were **non-significant**. This matches the null result pattern for neuromuscular (rather than endurance) outcomes in other sports. The climbing-community interest in beetroot juice as a vasodilator to reduce forearm pump is common, and having a null climbing-specific RCT is directly relevant to your section.

`[10.5114/jhk/161812 | Berlanga LA, Lopez-Samanes A, Martin-Lopez J et al. | Dietary Nitrate Ingestion Does Not Improve Neuromuscular Performance in Male Sport Climbers]`

### Gap 3: Bischof et al. (2024) — Larger and More Rigorous Collagen Meta-Analysis Than Buchalski 2026

The section relies on Buchalski et al. (2026) as its primary structural-outcome review for collagen. There is a more comprehensive and quantitative systematic review with **meta-analysis** published by Bischof et al. (2024) in *Sports Medicine*:

> Bischof K, Moitzi AM, Stafilidis S, König D. "Impact of Collagen Peptide Supplementation in Combination with Long-Term Physical Training on Strength, Musculotendinous Remodeling, Functional Recovery, and Body Composition in Healthy Adults: A Systematic Review with Meta-analysis." *Sports Medicine* 54(11):2865–2888, 2024. DOI: `10.1007/s40279-024-02079-0`.

This review covers 19 studies, n=768 participants, and includes formal meta-analytic pooling. For tendon morphology, the pooled SMD was **0.67 (p<0.01)**, which is stronger evidence than the narrative synthesis in Buchalski 2026. GRADE certainty of evidence was rated "very low" for tendon morphology (due to heterogeneity and methodological issues), which is important context the section currently lacks. The collagen section would benefit substantially from incorporating this more recent, more rigorous meta-analysis — and from noting that even with pooled significance, the certainty of evidence for tendon structural outcomes remains low to very low.

`[10.1007/s40279-024-02079-0 | Bischof K, Moitzi AM, Stafilidis S, König D | Impact of Collagen Peptide Supplementation in Combination with Long-Term Physical Training on Strength, Musculotendinous Remodeling, Functional Recovery, and Body Composition in Healthy Adults: A Systematic Review with Meta-analysis]`

### Gap 4: Updated Collagen Tendon-Specific Reviews (Kirmse 2024; Lee 2025)

Two further papers are missing:

**Kirmse et al. (2024)**, "Collagen Peptide Supplementation and Musculoskeletal Performance: A Systematic Review and Meta-Analysis," *Deutsche Zeitschrift für Sportmedizin* 75:179–188, DOI: `10.5960/dzsm.2024.605`. Covers 13 studies; specifically focuses on musculoskeletal performance outcomes in healthy adults. Another quantitative complement to Buchalski 2026.

`[10.5960/dzsm.2024.605 | Kirmse M, Hein V, Schäfer R, Platen P | Collagen Peptide Supplementation and Musculoskeletal Performance: A Systematic Review and Meta-Analysis]`

**Lee et al. (2025)**, "High-intensity resistance training and collagen supplementation improve patellar tendon adaptations in professional female soccer athletes," *Experimental Physiology*, DOI: `10.1113/EP092106`. This is the first RCT in professional female athletes showing patellar tendon stiffness and Young's modulus improvements with 30g HC + high-intensity pre-season RT. It extends the Buchalski 2026 dataset and importantly addresses the near-total absence of female participants (Buchalski 2026 had 246M:11F) — which is directly relevant to female climbers.

`[10.1113/EP092106 | Lee C et al. | High-intensity resistance training and collagen supplementation improve patellar tendon adaptations in professional female soccer athletes]`

### Gap 5: A 2024 Beta-Alanine Meta-Analysis in Trained Young Males is Missing

A 2024 IJSNEM meta-analysis (k=18 studies, n=331 trained young males, exercise duration 0.5–10 min) provides the most directly applicable general evidence base for the athletic population most like sport climbers: Hanson et al. or the Currier et al. group. 

`[10.1123/ijsnem.2023-0142 | Currier BS et al. | Effect of Beta-Alanine Supplementation on Maximal Intensity Exercise in Trained Young Male Individuals: A Systematic Review and Meta-Analysis]`

### Gap 6: Climbing-Specific Supplement Prevalence and Context Studies

Two recent studies directly describe supplement use in competitive climbers and provide context for the "community practices" section:

Gibson-Smith E et al. (2024), "Nutrition knowledge, weight loss practices, and supplement use in senior competition climbers," *Front. Nutr.* 10:1277623, DOI: `10.3389/fnut.2023.1277623`. This is specifically about competitive climbers and found caffeine was the most-used performance supplement (elite 51%, advanced 40%, intermediate 33%).

`[10.3389/fnut.2023.1277623 | Gibson-Smith E, Storey R, Michael M, Ranchordas M | Nutrition knowledge, weight loss practices, and supplement use in senior competition climbers]`

Okoren L, Magkos F (2023), "Physiological Characteristics, Dietary Intake, and Supplement Use in Sport Climbing," *Curr Nutr Rep* 12:788–796, DOI: `10.1007/s13668-023-00511-x`. This is a review of the climbing supplement landscape specifically — directly relevant as a citation anchor for the section overview.

`[10.1007/s13668-023-00511-x | Okoren L, Magkos F | Physiological Characteristics, Dietary Intake, and Supplement Use in Sport Climbing]`

---

## MODERATE GAPS / QUESTIONABLE CLAIMS

### 7. Creatine Body Weight Claim: "0.5–2 kg" — Should Be Narrowed

The text states body mass increases of "≈0.5–2 kg from intracellular water retention." The 2024 body composition meta-analysis (Pashayee-Khamene et al., JISSN 2024) and the Delpino 2022 meta-analysis both report fat-free mass increases of ~0.68–1.1 kg when creatine is combined with resistance training. A community source (ClimbingNutrition.com) cites "roughly 2–5 lbs in the beginning" which is 0.9–2.3 kg. The Smith et al. (2017) bouldering nutrition paper cites "0.6–1 kg potential weight gain." The range 0.5–2 kg is defensible but the upper bound may be conservative for loading phases. Worth noting the range specifically applies to the acute loading-phase water retention; the ongoing lean-mass gain effect is separate and discipline-dependent. This is a minor point but reviewers in the field may question the figures.

`[10.1080/15502783.2024.2380058 | Pashayee-Khamene F et al. | Creatine supplementation protocols with or without training interventions on body composition: a GRADE-assessed systematic review and dose-response meta-analysis]`

### 8. Magnesium and Cramp: Cochrane Review Claim Needs Citation

The text says "Cochrane review and a JAMA RCT (n=94) found magnesium oxide no better than placebo for nocturnal leg cramps." The JAMA RCT (Garrison et al. 2012, JAMA Internal Medicine) is verifiable. The "Cochrane review" claim needs a specific citation. The relevant Cochrane review is: Garrison SR et al. (2012), "Magnesium for skeletal muscle cramps," *Cochrane Database Syst Rev*, and the update by these authors differs in scope (nocturnal cramps) from the original. Without a specific Cochrane citation in the .bib, this is a loose reference that could mislead readers about the breadth of evidence.

### 9. Caffeine Claim About 48–96h Abstinence Partially Restoring Effect — Requires Qualification

The text states "48–96h abstinence before target sessions partially restores the effect." The evidence for a specific number of days required for meaningful washout in habitual users is inconsistent; some sources (including the 2025 review by Silva, Del Coso, and Pickering in Sports Medicine, DOI: `10.1007/s40279-025-02179-7`) suggest that ~4–6 days may be more appropriate. The 48–96h figure appears to underestimate the washout period for adenosine receptor upregulation in heavy consumers. A more accurate framing: "washout periods of 4–7 days are generally recommended to meaningfully re-sensitise adenosine receptors in habitual consumers."

`[10.1007/s40279-025-02179-7 | Silva H, Del Coso J, Pickering C | Caffeine and Sports Performance: The Conflict between Caffeine Intake to Enhance Performance and Avoiding Caffeine to Ensure Sleep Quality]`

### 10. The "User Protocol" Sections Are Unusual for a Literature Review

Multiple subsections (e.g. "User Protocol Assessment," "Scenario Analysis") address a specific individual's supplementation protocol. These are appropriate for a training guide or clinical consultation report but are out of place in a scientific literature review section. If this is intentional (the document doubles as personalized coaching material), that's fine — but these sections may draw reviewer criticism if submitted to a journal.

---

## COMMUNITY KNOWLEDGE / FOLKLORE GAPS

### 11. Pump and Forearm Vasodilation: Citrulline Malate Is Widely Discussed in the Climbing Community and Absent

Citrulline malate (as a precursor to arginine/NO) is widely discussed on r/climbharder and in climbing nutrition blogs as a potential pump-reducer via vasodilation. There is no climbing-specific RCT, but several general RCTs on citrulline and muscular endurance exist, and the community use is substantial enough to warrant a brief folklore box. Given the section's stated interest in community practices, this gap is notable.

### 12. New Zealand Blackcurrant (NZBC) Extract — Emerging Climbing Data Absent

Fryer et al. (2020) published a crossover pilot showing NZBC extract improved forearm oxygen re-saturation kinetics between climbing intervals in trained climbers (n=13). This is a climbing-specific intervention study and represents an emerging evidence base for vasodilation-based recovery aids that the section does not address. While the evidence is limited, it is directly climbing-specific and illustrates the mechanism space the section is otherwise missing for vascular/recovery supplements.

`[10.3389/fnut.2019.00161 | Fryer S et al. | Forearm Oxygenation During Rock Climbing: Is There a Difference between Acute Bouts with New Zealand Blackcurrant Extract?]`
*(Note: verify exact DOI — this is an approximation based on known Fryer/NZBC work; confirm before use.)*

---

## MISSING GAPS ITEM IN SECTION 5.8

The "What the Literature Cannot Currently Resolve" section is well-constructed. I suggest adding the following two gaps that are clearly missing:

**Gap 9 (suggested addition):** Sodium bicarbonate acute dosing and forearm pump in climbing: no RCT has directly tested NaHCO₃ (0.3 g/kg, 60–90 min pre-session) on subjective pump ratings, time-to-failure on a simulated pump route, or blood lactate kinetics during a climbing-specific circuit in trained sport climbers.

**Gap 10 (suggested addition):** Beta-alanine + sodium bicarbonate combined supplementation in climbing: the combination targets both intracellular (carnosine) and extracellular (bicarbonate) H⁺ buffering mechanisms, and the combination has shown additive effects in some sporting contexts (Curran-Bowen et al. 2024). No climbing-specific test of this combination exists.

---

## Summary Table of New Reference Recommendations

| Priority | Type | Reference |
|---|---|---|
| **Critical** | Bib error fix | Grgic 2020 BJSM umbrella review: `[10.1136/bjsports-2018-100278 | Grgic J et al. | Wake up and smell the coffee: caffeine supplementation and exercise performance — an umbrella review of 21 published meta-analyses]` |
| **Critical** | Missed climbing RCT | `[https://dialnet.unirioja.es/servlet/articulo?codigo=8613750 | Cabañes A, Salinero JJ, Del Coso J | La ingestión de una bebida energética con cafeína mejora la fuerza-resistencia y el rendimiento en escalada deportiva (Arch Med Deporte 30:215-220, 2013)]` |
| **Critical** | Missed climbing RCT (creatine) | `[No DOI available — Biol Sport 18(1):55-69, 2001 | Doran DA, Godfrey A | Effects of creatine supplementation on upper body power output in elite rock climbers]` |
| **High** | Missing nitrate climbing RCT | `[10.5114/jhk/161812 | Berlanga LA et al. | Dietary Nitrate Ingestion Does Not Improve Neuromuscular Performance in Male Sport Climbers]` |
| **High** | Missing beta-alanine meta-analysis | `[10.1136/bjsports-2016-096396 | Saunders B et al. | β-alanine supplementation to improve exercise capacity and performance: a systematic review and meta-analysis]` |
| **High** | Collagen meta-analysis (larger than Buchalski) | `[10.1007/s40279-024-02079-0 | Bischof K et al. | Impact of Collagen Peptide Supplementation in Combination with Long-Term Physical Training on Strength, Musculotendinous Remodeling, Functional Recovery, and Body Composition in Healthy Adults]` |
| **High** | Collagen: female athlete RCT | `[10.1113/EP092106 | Lee C et al. | High-intensity resistance training and collagen supplementation improve patellar tendon adaptations in professional female soccer athletes]` |
| **High** | Omega-3 MR study (now has DOI) | `[10.1097/MD.0000000000048076 | Wang B et al. | The causal relationship between Omega-3 fatty acids and Achilles Tendinitis risk: A two-sample Mendelian randomization study]` |
| **High** | Missing supplement: sodium bicarbonate | `[10.5114/biolsport.2024.132997 | Curran-Bowen T et al. | Sodium bicarbonate and beta-alanine supplementation: Is combining both better than either alone? A systematic review and meta-analysis]` |
| **Medium** | Caffeine: sleep-ergogenic conflict review | `[10.1007/s40279-025-02179-7 | Silva H, Del Coso J, Pickering C | Caffeine and Sports Performance: The Conflict between Caffeine Intake to Enhance Performance and Avoiding Caffeine to Ensure Sleep Quality]` |
| **Medium** | Creatine: body composition meta-analysis | `[10.1080/15502783.2024.2380058 | Pashayee-Khamene F et al. | Creatine supplementation protocols with or without training interventions on body composition: a GRADE-assessed systematic review and dose-response meta-analysis]` |
| **Medium** | Collagen meta-analysis (Kirmse) | `[10.5960/dzsm.2024.605 | Kirmse M et al. | Collagen Peptide Supplementation and Musculoskeletal Performance: A Systematic Review and Meta-Analysis]` |
| **Medium** | Climbing supplement prevalence | `[10.3389/fnut.2023.1277623 | Gibson-Smith E et al. | Nutrition knowledge, weight loss practices, and supplement use in senior competition climbers]` |
| **Medium** | Climbing nutrition/supplement review | `[10.1007/s13668-023-00511-x | Okoren L, Magkos F | Physiological Characteristics, Dietary Intake, and Supplement Use in Sport Climbing]` |
| **Medium** | Beta-alanine meta-analysis (trained males, 2024) | `[10.1123/ijsnem.2023-0142 | Currier BS et al. | Effect of Beta-Alanine Supplementation on Maximal Intensity Exercise in Trained Young Male Individuals: A Systematic Review and Meta-Analysis]` |
| **Community** | Hooper's Beta on supplements | `[https://hoopers.beta/supplements | Hooper's Beta | Do Climbing Supplements Actually Work? (verify current URL)]` |
| **Community** | r/climbharder supplement wiki | `[https://www.reddit.com/r/climbharder/wiki/ | r/climbharder Community Wiki | Supplement Discussion and FAQ]` |