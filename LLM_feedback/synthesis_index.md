# Synthesis Index — Performance Testing and Predictors

Compact cross-reference for writing agents. Each subtopic maps claims to source files so agents read only targeted snippets. Consensus = how many of the 11+8 LLM responses mention the claim. Files listed are those with the richest coverage for that subtopic.

---

## SECTION A — Physical Measurement Methodology (todo_20 primary)

### A1. MFS measurement: edge depth, grip position, body position
**Primary files**: `todo_20/deepseek.md` lines 1–60, `todo_20/kimi.md` lines 1–50, `todo_20/gemini.md` lines 1–80, `todo_20/qwen.md` lines 1–30
**Consensus**: ≥7 LLMs

**Key claims (all EVIDENCE_BACKED)**:
- ICC for MFS ranges 0.294–1.0 across 15 studies, median 0.86; edges 20–23 mm consistently ICC > 0.90 → `10.3389/fspor.2025.1650198` (Jullien/Pérez-Cordero et al. 2025 systematic review)
- Half-crimp: generally higher absolute force than open-hand; recommended research standard for specificity
- Seated bent-arm (Sit90) position: bouldering r = 0.73, sport climbing r = 0.64 (strongest correlation with performance) → `Stien et al. 2025 position comparison` (DOI unverified; `todo_20/gemini.md` line 11)
- Straight-arm position: lower reliability (ICC 0.88 vs bent-arm 0.94) but stronger correlation with grade (r² = 0.48 sport, r² = 0.66 bouldering) → same Stien 2025 study
- Tindeq Progressor validity vs. Kistler force plate: ICC = 0.99 one-handed rung pull and bent-arm lock-off; within-day ICC 0.90–0.98, between-day 0.95–0.98 → `Draper et al. (Tindeq validation, DOI unverified)`; bench test ICC ≥ 0.999 vs. Instron → (`todo_20/kimi.md` lines 14–18)
- MDC for MFS estimated ~5–7% (calculated from published ICCs); no single peer-reviewed MDC value published for climbing MFS → gap

**Unique single-LLM claim — TO_VERIFY**:
- Wolf et al. 2025: open-hand produced slightly *higher* force than half-crimp on 23 mm rung in some advanced climbers, mean 9.8% overestimation in half-crimp; authors recommend open-hand to reduce pulley stress → `todo_20/deepseek.md` line 13. Contradicts standard narrative; likely real paper but needs DOI.

---

### A2. Tindeq Progressor protocols
**Primary files**: `todo_20/kimi.md` lines 30–45, `todo_20/gemini.md` lines 28–33, `todo_20/qwen.md` lines 30–35
**Consensus**: ≥5 LLMs

**Key claims**:
- Tindeq samples at 80 Hz; adequate for peak force, **inadequate for RFD** (systematic underestimation of RTD vs. isokinetic dynamometer; ICC = 0.73–0.88 for RTD; MDC = 49–76% — very large) → `todo_20/kimi.md` lines 88–93
- Six Tindeq test modes: Live Data, Peak Load, RFD, Repeaters, Critical Force, and endurance variants
- Standard MFS test: 3 maximal reps, 90 s rest, free-hanging 20 mm rung → `todo_20/gemini.md` line 29

---

### A3. CF measurement protocols
**Primary files**: `todo_20/kimi.md` lines 37–62, `todo_20/gemini.md` lines 36–63, `todo_20/qwen.md` lines 27–48
**Consensus**: ≥6 LLMs

**Key claims (EVIDENCE_BACKED)**:
- Multi-trial gold standard: intermittent isometric at 45%, 60%, 80% MVC; 7:3 work:rest; linear regression work vs. time → slope = CF, intercept = W' → `10.1123/ijspp.2018-0809` (Giles et al. 2019)
- All-out test (single session): 24 maximal one-arm pulls, 7:3 ratio; CF = mean force last 6 contractions → `10.1123/ijspp.2020-0637` (Giles et al. 2021); ICC = 0.900 (95% CI 0.616–0.979) for CF; W' agreement lower (ICC 0.768)
- Baláš 2024 validation: ICC > 0.90 for CF via all-out method → `10.1007/s00421-024-05490-7`
- Mean CF in climbers: ~425.7 ± 82.8 N = 41.0 ± 6.2% MVC; W' ~30,882 ± 11,820 N·s → Giles 2019
- Critical finding (todo_20/kimi.md): CF as typically defined (mean last 3 contractions = 20.1 ± 5.7 kg) **overestimates** sustainable intensity — only 38% of subjects completed 720 s at this load; end-force (16.8 ± 5.2 kg) is a better sustainable threshold → Devise et al. validation study (DOI: likely `10.3389/fspor.2022.862782` or companion paper; verify)
- CF all-out test ICC = 0.92 → cited in `todo_20/qwen.md` and `todo_20/kimi.md`

**Folklore**:
- CF:MFS ratio target 60–70% for route climbers, >75% for endurance specialists → Lattice Training + Power Company podcasts; no RCT data; BIOPLAUSIBLE
- Community uses CF:MFS > 50% as minimum benchmark → `todo_20/kimi.md` line 58

---

### A4. RFD measurement in climbing
**Primary files**: `todo_20/kimi.md` lines 83–95, `todo_20/gemini.md` lines 82–95, `todo_17/claude.md` lines 23–30
**Consensus**: ≥4 LLMs

**Key claims**:
- Elite vs. advanced climbers: ES 1.02–1.58 at relative time periods; ES 0.72–0.84 at absolute windows (50–150 ms only discriminated elite vs. non-elite) → `10.1371/journal.pone.0249353` (Stien et al. 2021)
- Recommend relative time periods (% of time to peak force), not absolute ms windows, for RFD analysis
- Levernier & Laffaye 2019: 4-week elite training → RFD +27.5–32% (neural adaptation) → DOI unverified (`todo_20/kimi.md` line 88)
- Stien 2023 meta-analysis: RFD SDM = 0.91 (95% CI 0.21–1.61) following resistance training → `10.5114/biolsport.2023.113295`
- **Critical**: Tindeq 80 Hz sampling underestimates RTD systematically; MDC = 49–76% for RFD measures; research requires ≥200 Hz → `todo_20/kimi.md` lines 92–94

**No published RFD norms by grade** (gap — all LLMs agree)

---

### A5. Endurance metrics: SoD, NIRS, blood lactate
**Primary files**: `todo_20/kimi.md` lines 100–130, `todo_20/qwen.md` lines 62–82
**Consensus**: ≥3 LLMs

**Key claims**:
- Slope of Decline (SoD): rate of force drop during sustained effort; extractable from Tindeq data; no peer-reviewed reliability/validity data published → gap
- NIRS/SmO2: Schöffl lab and others used NIRS on forearm flexors; wearable Moxy etc. correlate with fatigue but lab-bound; wearable NIRS validity vs. gold standard unpublished in climbing context → BIOPLAUSIBLE
- Blood lactate: accumulates post-ascent 4–7 mmol/L; lactate threshold from treadmill/cycle tests **does not correlate with climbing grade** → `Billat et al. 1995` (DOI: `10.1249/00005768-199504000-00002` unverified) and multiple reviews
- Intermittent endurance test (7/3 at 60% MVC to failure) better construct validity for aerobic capacity than continuous hang (which is primarily strength-dependent)

---

## SECTION B — Finger Strength as Predictor (todo_17 primary)

### B1. Relative vs. absolute MFS
**Primary files**: `todo_17/claude.md` lines 53–58, `todo_17/deepseek.md` lines 10–15, `todo_17/qwen.md` lines 8–9
**Consensus**: ALL LLMs (highest consensus point in entire corpus)

**Key claims (EVIDENCE_BACKED)**:
- Relative MFS (force/BW) consistently outperforms absolute MFS in correlation analyses; mechanistic reason: climbing requires gravity resistance proportional to body weight
- Stien 2024 IJSPP: relative half-crimp R² = 0.48–0.58 (strongest of 6 grips) → `DOI: 10.1123/ijspp.2023-0030` (verify — may be different DOI; source `todo_17/claude.md` line 37)
- Stien 2025 normative (n=307): finger strength explains 68% (males) and 64% (females) of climbing ability variance; intermittent endurance adds 28%/34% → `10.1080/02640414.2024.2449316`
- Buraas/Stien 2025 (n=19 males): climbing-specific finger strength r = 0.89 bouldering, r = 0.67 redpoint, r = 0.82 campus → `10.1007/s00421-025-05802-5` (or PMID 40325204; verify DOI)

---

### B2. Half-crimp vs. open-hand predictive validity; edge depth specificity
**Primary files**: `todo_17/claude.md` lines 59–82, `todo_17/deepseek.md` lines 13–16
**Consensus**: ≥7 LLMs

**Key claims (EVIDENCE_BACKED)**:
- Half-crimp R² = 0.48–0.58 (highest of 6 techniques in Stien 2024 IJSPP; open-hand lower)
- 20 mm edge: de facto standard; 18–23 mm range shows acceptable ICC > 0.90; below 18 mm or above 25 mm reliability degrades → Jullien 2025 systematic review
- Standard: `10.1080/17461391.2010.546431` (Baláš et al. 2012) shows moderate-strong validity (r 0.42–0.79) for climbing-specific tests

**Contested claim TO_VERIFY**:
- MacKenzie 2020: shoulder endurance (max pull-ups + arm crank power + bent-arm hang) explained R² = 0.77 (males), 0.62 (females) — **higher than any single finger strength model** → `10.1123/ijspp.2019-0451` (verify DOI; mentioned by todo_17/deepseek.md and todo_17/meta.md; contradicts finger-first narrative but may reflect sample/measure heterogeneity)

---

### B3. Lattice norms and community benchmarks for MFS
**Primary files**: `todo_17/claude.md` lines 95–100, `todo_17/deepseek.md` lines 20–24, `todo_17/kimi.md` (all)
**Consensus**: ≥8 LLMs

**Key claims (FOLKLORE_VERIFIED, ≥3 sources)**:
- 7-second 2-arm max hang on 20 mm edge (%BW) norms (reverse-engineered from Lattice athlete videos + WMG Climbing blog + Lattice blog):
  V4: 49% | V5: 55% | V6: 61% | V7: 67% | V8: 73% | V9: 79% | V10: 85% | V11: 91% | V12: 96% | V13: 101% | V14: 106% | V15: 110% | V16: 114% | V17: 118%
- Sources: `https://wmgclimbing.wordpress.com/2024/03/10/approximating-lattices-finger-strength-data-set/`, `https://latticetraining.com/2-arm-fs-test/`, `https://latticetraining.com/blog/predictors-for-performance/`, UKC forums
- StrengthClimbing Finger Strength Analyzer 2.0 (J. Banaszczyk): grade prediction from 20 mm hang + pull-up → `https://strengthclimbing.com/finger-strength-analyzer/` — TO_VERIFY as single primary source for grade-prediction formula

---

### B4. Pull-up strength as predictor (secondary)
**Primary files**: `todo_17/claude.md` lines 100–130 (§2), `todo_17/deepseek.md` lines 27–44, `todo_17/qwen.md` lines 13–21
**Consensus**: ≥8 LLMs

**Key claims (EVIDENCE_BACKED)**:
- Pull-up strength correlates moderately with grade (r = 0.55 bouldering, 0.57 campus in Buraas/Stien 2025; not significant for redpoint)
- Lattice data (N=901 bouldering): 2-rep max pull-up R = 0.346, adj. R² = 0.117 — substantially below finger strength (R² = 0.167)
- **Exception — elite route climbing**: Lattice (N=422 routes): 2RM pull-up strongest predictor at Higher Elite level (R = 0.521, adj. R² = 0.253, β = 0.040 IRCRA units) → `https://latticetraining.com/blog/what-is-the-number-1-measure-of-performance-for-sport-climbers/`
- Independent contribution of pull-up beyond finger strength: **not established** in any single multivariate model with partial correlations reported → key gap

**Community benchmarks (FOLKLORE_VERIFIED)**:
- Advanced (~7b/V8): ~120–140% BW 1RM; Elite (~8b): ~150–160% BW; Higher elite (~8c+): ~166% BW → Lattice blog + StrengthClimbing + UKC forums

---

### B5. Multivariate models: what best explains climbing grade variance?
**Primary files**: `todo_17/claude.md` lines (§7, ~lines 250–320), `todo_17/qwen.md` lines 63–70, `todo_17/perplexity.md` lines 44–48
**Consensus**: ≥7 LLMs

**Key studies (EVIDENCE_BACKED)**:
| Study | n | Design | Best model R² | Notes |
|---|---|---|---|---|
| Mermier et al. 2000 | 44 | PCA + regression | 0.66 | Training component 58.9%; anthropometrics 0.3% → `10.1136/bjsm.34.5.359` |
| Baláš et al. 2012 | ~60 | SEM | 0.97 | SEM-specific; latent hand-arm + body fat + experience → `10.1080/17461391.2010.546431` — very high, SEM caution |
| Laffaye et al. 2016 | 41 | PCA + regression | 0.64 | Training component (fingers + upper-limb power) 46% → DOI unverified, Researchgate |
| Saeterbakken et al. 2023 | — | regression by discipline | 0.58 | Women lead: upper-body power β=0.59 + finger endurance β=0.48; Men lead: lower-body + upper-body + fat + motor-planning → `10.3390/ijerph20197699` |
| Stien 2025 normative | 307 | CFA | ~0.96 model | Only includes finger strength + intermittent endurance; doesn't include all predictors |

**Gap statement**: Best physical-only models explain R² ≈ 0.63–0.66 (Mermier 2000, Laffaye 2016); 33–50% unexplained = technique + psychology + route-reading + grade subjectivity + training specificity. No adequate prospective (longitudinal) model exists.

---

## SECTION C — Aerobic Capacity, CF, and Endurance as Predictors

### C1. Critical Force as route climbing predictor
**Primary files**: `todo_17/claude.md` lines (§4a), `todo_17/qwen.md` lines 38–45, `todo_17/deepseek.md` (§4)
**Consensus**: ≥6 LLMs

**Key claims (EVIDENCE_BACKED)**:
- CF (% BW) r = 0.61 with sport climbing grade; W' r = 0.34 with bouldering (route > boulder for CF) → `10.1123/ijspp.2018-0809` (Giles et al. 2019)
- Lattice 2025 (N=422): CF R² = 0.16 overall; **not significant at Higher Elite (p=0.052)** — diminishing returns at elite level
- CF as predictor requires minimum ability ~RP ≥ 7a/V4 (6% of beginners could not generate stable plateau) → CAMP4 review

---

### C2. VO₂max and systemic aerobic capacity: null predictor
**Primary files**: `todo_17/claude.md` (§4b), multiple others
**Consensus**: ≥7 LLMs (null result = strong)

**Key claims (EVIDENCE_BACKED)**:
- Billat et al. 1995: 7b routes elicited only 37.7–45.6% treadmill VO₂max; HR 77–85.5% max; lactate 4.3–5.7 mmol/L → `10.1249/00005768-199504000-00002` (unverified)
- Multiple reviews confirm: treadmill/cycle VO₂max does NOT correlate significantly with climbing grade
- Only vertically mounted isokinetic rowing ergometer showed significant aerobic-performance correlation → Frontiers 2024 systematic review

---

## SECTION D — Anthropometrics and Other Physical Predictors

### D1. Ape index: null result
**Primary files**: `todo_17/claude.md` (§5a), `todo_17/meta.md` lines 111–120, `todo_17/qwen.md` lines 47–50
**Consensus**: ≥6 LLMs

**Key claims (EVIDENCE_BACKED)**:
- Ozimek 2023 systematic review (18 studies): "none of the analyzed work showed differences between sport climber groups in the ape index" → `10.1519/JSC.0000000000004418`
- Watts et al. 2003 (n=90 junior competitive): no ape index-grade correlation → `10.1136/bjsm.37.5.420` (unverified)
- Mermier 2000: anthropometric component explains **0.3%** of variance
- **Contradictory finding (single study, small n)**: Frontiers 2025 IFSC vs. national boulderers (n=34): ape index significantly higher in international group (p<0.05) → `10.3389/fspor.2025.1588414` — note: small n, ethnic confounders → TO_VERIFY full paper

---

### D2. Body composition
**Primary files**: `todo_17/claude.md` (§5b), `todo_17/qwen.md` lines 45–51
**Consensus**: ≥6 LLMs

**Key claims**:
- Lower body fat % associated with elite status (EVIDENCE_BACKED); but: Mermier 2000 — body mass explains <1% variance when training variables included
- A2 pulley CSA hypertrophy in elite climbers: structural adaptation (not predictor before training) — BIOPLAUSIBLE
- Weight-cutting: RED-S risk documented in competitive climbers (Schöffl lab); community warns against it — FOLKLORE_VERIFIED

---

### D3. Other physical predictors
**Primary files**: `todo_17/claude.md` (§6), `todo_17/perplexity.md` lines 35–43
**Consensus**: varies by predictor

**Key claims**:
- Shoulder strength (r ≈ 0.56–0.60): EVIDENCE_BACKED moderate correlation (MacKenzie 2020 shoulder ergometer)
- Core strength (L-sit, front lever): **no peer-reviewed grade-correlation study** → TO_VERIFY
- Lower body CMJ: EVIDENCE_BACKED null for bouldering/sport; significant for speed climbing (r = −0.78 to −0.90) → need DOI for speed climbing study
- Years climbing / technique proxies: strong correlate (EVIDENCE_BACKED cross-sectional); Mermier 2000 years-experience loaded on training component (58.9%); 8a.nu OLS: years significantly positive all subgroups
- Hip flexor / flexibility: Lattice 2025 (bouldering R = 0.026, p = 0.62) — effectively null → `https://latticetraining.com/blog/predictors-for-performance/`

---

## SECTION E — Statistical/Probabilistic Grading Models

### E1. IRT, Rasch, and Elo applied to climbing
**Primary files**: `todo_17/claude.md` (§8a), `todo_17/qwen.md` lines 73–79, `todo_17/kimi.md` (todo_17)
**Consensus**: ≥5 LLMs

**Key claims**:
- Rasch/1PL-IRT: P(success) = exp(θ−β)/(1+exp(θ−β)); same functional form as Elo; both model climber ability (θ) vs. route difficulty (β) on same scale
- Scarff 2020 arXiv preprint: "Whole-History Rating" (Bradley-Terry model) applied to route difficulty estimation from logbook data → `arxiv:2001.05388` (preprint; not peer-reviewed)
- Drummond 2021: Bayesian MCMC on theCrag/Vertical-Life data; each grade increment = 3.17× difficulty on V-scale → `todo_17/qwen.md` line 76; need DOI
- Rosenthal 2022 blog: Bayesian "Route Response Theory" on 8a.nu; structurally Bayesian Rasch model → `https://www.ethanrosenthal.com/2022/04/15/bayesian-rock-climbing/`
- Frontiers 2024: ML + grading bias review → `10.3389/fspor.2024.1512010`

**Key academic gap**: No peer-reviewed full IRT/Rasch paper published specifically for sport climbing grade prediction (Rasch applied to adjacent sports, not climbing directly)

---

### E2. Big-data and ML approaches (8a.nu, Moonboard)
**Primary files**: `todo_17/claude.md` (§8b), `todo_17/qwen.md` (§8)
**Consensus**: ≥3 LLMs (mostly noted by claude.md; unique niche content)

**Key claims (blog-level / TO_VERIFY for specific sources)**:
- 8a.nu OLS regression: years climbing = strongest predictor; height negative predictor for males; weight/height minimal after multicollinearity correction → GitHub: `https://github.com/stevebachmeier/climber-characteristic-analysis`
- Moonboard CNN grade prediction (Stanford CS229 2017): CNNs best but still below human accuracy → `https://cs229.stanford.edu/proj2017/final-reports/5232206.pdf`
- "Board-to-Board" (arXiv 2023): CNN generalizability drops across Moonboard versions → `https://arxiv.org/pdf/2311.12419`
- PLOS One (mention in chatgpt_sources.md line 24): "An Adapted Elo Framework for Skill Rating and Probabilistic..." applied to bouldering — likely real paper, needs DOI from chatgpt_sources → `journals.plos.org` (search "adapted Elo climbing")

---

## SECTION F — Test Batteries: 9c Test, Lattice, Research Batteries

### F1. 9c test protocol (FULL TREATMENT)
**Primary files**: `todo_17/claude.md` (§3), `todo_17/deepseek.md` lines 49–70, `todo_17/github.md` lines 99–120, `todo_17/grok.md` (all), `todo_17/qwen.md` lines 23–37
**Consensus**: ALL LLMs

**Protocol (FOLKLORE_VERIFIED — ≥3 independent sources confirming same 4 components)**:
1. **Max finger strength** (5 s weighted hang, 20 mm edge, half-crimp): 1 pt = 100% BW → +10% per pt → 10 pts = 220% BW (non-linear: 7→8 = 160%→180%, 8→9 = 180%→200%, 9→10 = 200%→220%)
2. **Max pull-up** (1RM weighted): 1 pt = 100% BW → 10 pts = 220% BW (same scale)
3. **Core test** (tiered by level): 1 pt = 10 s bent-knee L-sit; 4 pt = 10 s straight L-sit; 7 pt = 5 s front lever; 10 pt = 30 s front lever
4. **Bar dead-hang** (unweighted time): 1 pt = 10 s → 10 pts = 100 s

**Grade prediction table** (community version from theCrag + OpenClimbing.info):
40 = 9c | 38–39 = 9b/9b+ | 36–37 = 9a+/9b | 32–35 = 9a/9a+ | 28–31 = 8c/8c+ | 24–27 = 8b/8b+ | 20–23 = 8a/8a+ | 18–19 = 7c+ | 16–17 = 7c | 12–15 = 7b/7b+ | 8–11 = 7a/7a+ | 4–7 = 6b/6c | 1–3 = 6a

Sources: `https://www.youtube.com/watch?v=UOBB4wkTdxQ` | `https://www.hoopersbeta.com/library/can-the-ultimate-climbing-test-really-reveal-your-biggest-weakness` | `https://www.thecrag.com/en/climbing/virtual/route/4430259711` | `https://climbapedia.org/content/climbing-potential` | `https://www.ukclimbing.com/forums/walls+training/magnus_midtbo_-_9c_fitness_test-730174` | `https://www.menshealth.com/fitness/a36704997/marine-strength-test-climbing-michael-eckert-magnus-midtbo/`

**Peer-reviewed validation: ZERO** — confirmed by all LLMs; no published study in PubMed/IJSPP/Frontiers

**Evidence support for individual components**:
- Exercise 1 (finger strength): EVIDENCE_BACKED (see §B1)
- Exercise 2 (pull-up): EVIDENCE_BACKED as moderate predictor (see §B4)
- Exercise 3 (core/front lever): **TO_VERIFY** — no published grade-correlation for L-sit or front lever; BIOPLAUSIBLE for anterior chain tension
- Exercise 4 (bar dead-hang unweighted): **TO_VERIFY** — poor grip specificity; measures endurance on large jug; Hooper's Beta: tests mental tenacity, not forearm aerobic endurance

**Limitations (all LLMs agree)**:
- Does not capture: technique, footwork, route-reading, fear management, flexibility, forearm aerobic endurance, skin condition
- Predictive validity likely weakest below ~7a (technique dominates) and coarsest above 8c+ (point increments too coarse; 8b vs 8c = only 3–4 pts difference within measurement noise)
- Injury concern: 160%→180%→200%→220% BW jumps in finger scoring = dangerous if used as training targets (Hooper's Beta critique)

---

### F2. Lattice Training athlete profiling
**Primary files**: `todo_17/claude.md` (§9a), `todo_17/qwen.md` lines 81–87, `todo_17/deepseek.md` (§2c)
**Consensus**: ≥8 LLMs

**Components (publicly documented)**:
1. 7-second 2-arm max hang, 20 mm edge, half-crimp, %BW
2. 2-rep max weighted pull-up, %BW
3. 60% MFS power endurance: 7/3 repeaters to failure (TTE)
4. Box-split flexibility (hip abduction, cm)
5. Some versions: CF proxy test

Published validity: blog-level only (n=422 routes, n=901 bouldering; 2025); no peer-reviewed independent validation of battery as whole
URLs: `https://latticetraining.com/blog/predictors-for-performance/` | `https://latticetraining.com/blog/what-is-the-number-1-measure-of-performance-for-sport-climbers/`

---

### F3. Research-grade batteries
**Primary files**: `todo_17/claude.md` (§9b–f), `todo_17/qwen.md` lines 81–87
**Consensus**: ≥4 LLMs

**Giles 2006** (`10.2165/00007256-200636060-00006`): narrative review, not a validated test battery — foundational reference

**IRCRA position (Draper et al. 2015/2021)**: standardized reporting scale (IRCRA 1–32) + research descriptors; no fully validated battery → `https://www.researchgate.net/publication/281232738` (search for DOI)

**Stien 2022 mini-review** (`10.3389/fspor.2022.847447`): recommended 4-test battery: (1) 7 s max hang; (2) continuous hang to failure on 20–25 mm; (3) 7/3 at 60% MVC to failure; (4) isometric pull-up on 23 mm campus rung for RFD

**Climbro**: 4-test protocol (MFS, RFD explosive pull, continuous endurance, intermittent 7/3); validated across 3 IRCRA groups; allows CF/W' estimation → `https://climbro.com/2023/01/strength-and-endurance-testing-for-efficient-climbing-training/`

**Community tools**:
- StrengthClimbing Critical Force Calculator → `https://strengthclimbing.com/critical-force-calculator/`
- OpenClimbing 9C calculator → `https://www.open-climbing.info/9c-calc.html`
- Tindeq app (CF test mode, all-out protocol)

---

## KEY CAUSATION CAVEATS (apply across all sections)

**From todo_17/claude.md (§10) — consensus all LLMs**:
1. All studies are cross-sectional unless explicitly noted — NO causal inference
2. Reverse causation: higher-grade climbers score better on tests partly because they've trained more, not because the measured quality was the bottleneck
3. Selection bias: range restriction within competitive samples inflates correlations
4. Self-reported grade: major noise source (gym vs. outdoor, RP vs. OS, grade inflation)

**Predictors with intervention evidence (causal plausibility)**:
- MFS: Hermans 2022 RCT (n=35) improved Fpeak/RFD vs. control (`10.3389/fspor.2022.888158`); Stien 2023 meta-analysis (`10.5114/biolsport.2023.113295`) — but climbing grade not measured as outcome in either
- RFD: Levernier & Laffaye 2019 (4-week, elite, +RFD)
- **No predictor has been shown to causally improve climbing grade in an adequately powered RCT**

---

## OPEN QUESTIONS (consensus across ≥5 LLMs)
1. Does any field battery (9c, Lattice) predict grade **improvement over time** (prospective), not just concurrent grade?
2. How does relative importance of predictors shift across the grade spectrum (V4→V17)?
3. What is CF's independent contribution after controlling for MFS (partial correlation unreported)?
4. Can technique and movement efficiency be quantified and how much variance do they explain?
5. Are predictors sex-specific and discipline-specific at elite level?
6. Is MFS-grade relationship linear or does it show threshold/diminishing returns effects?
7. Does inter-individual response to training (baseline score predicts gain magnitude) generalize across metrics?

---

## DOIs TO ADD TO BIBLIOGRAPHY (verified or high-confidence from ≥3 LLMs)

Run `python -m scripts.cite.add_citation --doi <DOI> --bib bibliography.bib` for each:

```
10.1136/bjsm.34.5.359          # Mermier 2000
10.1080/17461391.2010.546431   # Baláš 2012
10.1371/journal.pone.0249353   # Stien 2021 RFD
10.3389/fspor.2022.888061      # Vereide 2022 RFD
10.1123/ijspp.2018-0809        # Giles 2019 CF original
10.1123/ijspp.2020-0637        # Giles 2021 all-out test
10.1007/s00421-024-05490-7     # Baláš 2024 CF validation
10.3389/fspor.2023.1130812     # Langer 2023 systematic review
10.1080/02640414.2024.2449316  # Stien 2025 normative
10.3389/fspor.2024.1512010     # Frontiers 2024 grading ML
10.2165/00007256-200636060-00006  # Giles 2006 review
10.1007/s00421-025-05802-5     # Buraas/Stien 2025 (may fail — use PMID 40325204 as fallback)
10.3389/fspor.2025.1650198     # Jullien/Pérez-Cordero 2025 reliability review
10.1519/JSC.0000000000003548   # Torr et al. 2022 validity
10.3390/ijerph20197699         # Saeterbakken 2023 competitive predictors
10.1007/s00421-003-1036-7      # Watts 2004 physiology review
10.1080/02640419608727715      # Grant et al. 1996
10.3389/fspor.2022.888158      # Hermans 2022 RCT
10.3389/fspor.2022.847447      # Stien 2022 mini-review
10.1519/JSC.0000000000004418   # Ozimek 2023 systematic review
10.1123/ijspp.2019-0451        # MacKenzie 2020 (verify DOI)
10.3389/fspor.2025.1588414     # Frontiers 2025 IFSC morphology (verify)
10.1519/JSC.0b013e3182577026   # Fanchini 2013
```

Already in bib (skip): `10.5114/biolsport.2023.113295` (Stien 2023), `10.3389/fspor.2022.862782` (Devise 2022)

**URLs to cite as `\url{}` with `\bibitem`** (no DOI):
- `https://arxiv.org/abs/2001.05388` = Scarff 2020 Whole-History Rating
- `https://www.ethanrosenthal.com/2022/04/15/bayesian-rock-climbing/` = Rosenthal 2022 IRT blog
- `https://latticetraining.com/blog/predictors-for-performance/` = Lattice 2025 bouldering predictors
- `https://latticetraining.com/blog/what-is-the-number-1-measure-of-performance-for-sport-climbers/` = Lattice 2025 sport climbing
- `https://www.hoopersbeta.com/library/can-the-ultimate-climbing-test-really-reveal-your-biggest-weakness` = Hooper's Beta 9c critique
- `https://strengthclimbing.com/finger-strength-analyzer/` = StrengthClimbing analyzer
- `https://wmgclimbing.wordpress.com/2024/03/10/approximating-lattices-finger-strength-data-set/` = WMG blog Lattice norms
