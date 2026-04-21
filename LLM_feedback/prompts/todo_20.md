# Prompt G — Scientific Measurements and Metrics for Climbing Training

## Context and purpose

I am writing a scientific literature review on training for rock climbing. I need a comprehensive section on how to measure, test, and interpret training metrics in climbers — covering both laboratory-standard protocols and field tools accessible to practitioners. This section should serve as a standardised metrics reference with quality caveats, so a climber or coach can select appropriate measures, understand their reliability, and interpret their results with appropriate uncertainty.

**Your task**: produce an exhaustive research synthesis on scientific measurement in climbing training. Use your training data AND active web searches across PubMed, Google Scholar, relevant exercise physiology journals, climbing-specific research groups (Schöffl lab, Laffaye lab, Giles/Simon/Schweizer etc.), Tindeq/Lattice technical documentation, and community sources. Be exhaustive. Flag every claim's evidence tier and source.

## Citation format

- Scientific papers: `[DOI | Authors | Title]`
  - Example: `[10.5114/biolsport.2023.113295 | Stien et al. 2023 | Meta-analysis of hangboard training]`
  - If DOI unverified: `[DOI unverified | Authors | Title | Journal, year]`
- Other resources: `[URL or source description]`
  - Example: `[https://tindeq.com/... | Tindeq Progressor documentation]`
- Every factual claim must cite at least one source. No uncited assertions.

## Evidence classification (apply to every claim)

- **Evidence-backed**: peer-reviewed data with adequate controls; cite studies, report effect size and 95% CI.
- **Bioplausible**: mechanistically plausible, no direct controlled intervention evidence; state mechanism and gap.
- **Folklore**: community consensus or practitioner claim without empirical support; name source explicitly.

## Writing style

Dense, precise, information-complete. Numbers over words: `ICC = 0.94`, `MDC = 12 N`, `W' = 8.4 kJ`. Flag contested or unverified claims explicitly.

## Output is freeform — focus entirely on content

Plain prose and lists, structured by sub-topic. Maximum information density and citation coverage. No LaTeX formatting.

---

## Sub-topics to cover (be exhaustive within each)

### 1. Maximal finger strength (MFS)

**Measurement methods:**
- Hangboard dynamometry: dead-hang to failure, timed dead-hang, relative vs. absolute force
- Edge depths used in research: 18mm standard (Stien et al.), 20mm (other protocols), variability across studies
- Half-crimp vs. open-hand position: which is recommended as standard and why
- Force gauge attachment setups: which load cell positions and body positions have published reliability data
- Intraclass Correlation Coefficient (ICC) and Minimal Detectable Change (MDC) values reported in the literature

**Interpretation:**
- Normative values by climbing grade (if published)
- MFS relative to body weight as a predictor: regression data, r², predictive validity for redpoint grade
- What MFS change is meaningful: minimum meaningful change thresholds where available

**Protocols:**
- Tindeq Progressor protocols for MFS testing: documented procedures and reported reliability
- Lattice testing protocols: published or documented norms
- Research-grade protocols: what do Stien et al., Devise et al., and others use?

**Community folklore around MFS:**
- What does r/climbharder and the coaching community say a "good" MFS score looks like at V6 / V8 / V10+? Name every source
- Community heuristics about minimum MFS targets before progressing to advanced training (e.g., "bodyweight hang on 20mm for X seconds") — source each one
- Any community-derived or coach-published normative tables (Lattice norms, Tyler Nelson benchmarks, ClimbHarder spreadsheets)

### 2. Critical Force (CF) and W'

**Theoretical framework:**
- CP/CF two-parameter model applied to isometric finger flexors
- W' definition: anaerobic work capacity above CF; units, typical values in climbers
- Distinction between CF (aerobic capacity ceiling) and MFS (peak force ceiling)
- How the model is derived: all-out test, 3-min test, multi-trial regression — different estimation methods and their validity

**Measurement protocols:**
- Standard CF estimation methods: sustained isometric tests at multiple intensities, regression on time-to-exhaustion
- Tindeq all-out protocol for CF estimation: what is it, what has been published on its validity
- Time trial tests (e.g., 60-s or 90-s at fixed % MFS) as CF proxies: evidence on correlation with full regression method
- Practical considerations: reliability in field conditions vs. lab

**Interpretation:**
- Normative CF values by climbing grade (if any published data exist)
- CF as predictor of endurance performance on routes vs. boulders
- How CF and MFS together describe an athlete's physiological profile
- CF:MFS ratio as a training target concept: any evidence vs. practitioner consensus

**Training implications:**
- Does CF training (work at >CF intensity) improve CF specifically?
- Intervention data on CF-targeted training in climbers (any RCTs or controlled studies)

**Community folklore around CF:**
- How do community sources (Tindeq user community, r/climbharder, coaching blogs) use CF in practice — what testing protocols do they actually run, what thresholds do they cite?
- Any community-derived CF norms or "good CF:MFS ratio" targets — name every source explicitly
- Practitioner debates about whether CF testing is useful for non-elite climbers

### 3. Peak force asymmetry

**Definition and measurement:**
- Left-right asymmetry in isometric finger force: how measured, which fingers/positions
- Inter-finger force distribution (index-middle-ring-little): methods and what they reveal
- Grip position asymmetry (crimp vs. open hand discordance between hands)

**Clinical and performance relevance:**
- Any data linking force asymmetry to injury risk (pulley injury incidence, overuse patterns)
- Any data linking asymmetry to performance limitations
- Threshold values for "clinically meaningful" asymmetry — published benchmarks or consensus

**Measurement tools:**
- Tindeq bilateral testing: protocol documentation
- Finger force distribution systems (multi-sensor rigs): research use
- Simple field alternatives: single-arm hangs, subjective force matching

### 4. Rate of Force Development (RFD) and force-velocity profiling

**Relevance to climbing:**
- Why RFD matters for dynamic moves (dyno, deadpoint, campus moves)
- Any evidence linking RFD to climbing performance outcomes

**Measurement:**
- Isometric RFD from load cell: what time windows are standard (0–50ms, 0–100ms, 0–200ms, peak)
- Tindeq or similar device RFD extraction: what the data export provides
- Reliability data for RFD measurements in finger flexors

**Normative data:**
- Any published RFD norms for climbers by grade or level

### 5. Endurance metrics: Slope of Decline (SoD), Blood Lactate, oxygenation

**Slope of Decline (SoD) / force fatigue curves:**
- Definition: rate of force decline during sustained effort or intermittent hangs
- How to extract from Tindeq or load cell data
- Published reliability and validity data
- Correlation with climbing performance or CF

**Blood lactate in climbing:**
- Any studies measuring blood lactate during climbing vs. hanging protocols
- Lactate threshold testing applied to climbing training load prescription

**Near-infrared spectroscopy (NIRS) / muscle oxygenation (SmO2):**
- Which climbing research groups have used NIRS on forearm flexors
- What Moxy, BSX, or similar devices reveal about forearm deoxygenation during climbing
- Evidence on SmO2 as a training load proxy or recovery indicator

### 6. Body composition and anthropometrics

**What the research measures:**
- Ape index, height, weight, BMI in climbing performance prediction models
- Body fat and lean mass: how measured in climbing research, predictive validity
- Finger length / morphology as performance predictor

**Normative data:**
- Published anthropometric profiles by climbing grade (Magiera et al. or equivalent)

### 7. Reliability, validity, and minimal detectable change (MDC)

**Cross-cutting concerns:**
- ICCs reported across different finger strength measures in the literature
- MDC for MFS, CF, RFD, SoD — what change exceeds measurement noise
- Sources of variability: time of day, warm-up protocol, hydration, skin condition
- Standardisation recommendations to improve test-retest reliability

### 8. Testing protocols and practical implementation

**Full testing battery recommendation:**
- What combination of metrics gives the most information with reasonable testing burden
- Frequency of re-testing: how often is meaningful change detectable
- Software and hardware ecosystem: Tindeq app, ClimbHarder tools, spreadsheet-based regression

**Field vs. lab tradeoffs:**
- What can be done with a Tindeq + phone vs. what requires lab equipment
- Which metrics are stable enough for self-coaching vs. which need specialist interpretation

**Community folklore around testing practice:**
- What testing cadences does the community actually use? (e.g., "test every 6 weeks" — where does this come from?)
- Community-held beliefs about which metrics matter most for improvement, even if not supported by research — name sources (r/climbharder, coaching podcasts, YouTube channels)
- Any practitioner frameworks for interpreting a full testing battery that have no published scientific validation but are widely cited (e.g., Lattice athlete scoring, Tyler Nelson functional movement screen analogs)

---

## Open questions

List 5–7 specific questions about climbing measurement science that the literature cannot yet answer.

---

## Seed references to check

- Stien et al. (2023). *Biology of Sport* 40(3):875–889. `[10.5114/biolsport.2023.113295]`
- Devise et al. (2022). *Front Sports Act Living* 4:862782. `[10.3389/fspor.2022.862782]`
- Laffaye G et al. — any papers on force profiling in climbers
- Giles et al. (2006) — climbing performance predictors (verify DOI)
- Draper et al. — any papers on physiological profiling of climbers
- Bertuzzi et al. — energy systems in climbing
- Tindeq technical documentation and any published validation studies
- Lattice Training methodology documentation

Do not fabricate DOIs. Write "DOI unverified" when unsure.
