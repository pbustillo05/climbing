# Prompt — Performance Predictors in Rock Climbing (Todo 17 + Preston's Note)

## Context and purpose

I am writing a scientific literature review on training for rock climbing, and I need a comprehensive synthesis of **statistics vs. climbing performance and all the ways they interact**. This means an exhaustive overview of "statistical estimators" for climbing grades, predictive modeling, and empirical correlations linking physical metrics to climbing performance.

This section must accomplish the following:
1. **Statistical Models & Grading Systems:** Review academic and data-science efforts leveraging probabilistic/statistical models (e.g., Elo rating systems, Item Response Theory, Rasch models) applied to climbing routes or boulder problems. Include big-data studies analyzing large datasets like 8a.nu or Sendage.
2. **Empirical Predictors of Performance:** Build an evidence-graded picture of measurable qualities predicting climbing grade (finger strength, pull-up strength, body composition, etc.), separating correlation from causation.
3. **Blog-level Data Science & Community Folklore:** Include basic statistical analysis or regressions done by bloggers (e.g., Lattice Training) and community "citizen science". Evaluate specific famous community protocols like the **9c test by Magnus Midtbø**, even if they are considered 100% folklore.
4. **Comprehensive Data Sweep:** Identify all statistical studies exploring correlations and causations between climbing metrics by thoroughly exploring ALL the web and the literature (including any "miracle" serious studies validating popular field tests).

**Your task**: use your training data AND active web searches across PubMed, Google Scholar, sports science journals, Reddit (r/climbharder), Lattice Training, Hooper's Beta, and any other relevant sources. Be exhaustive on both the strict scientific literature and the community knowledge base. Flag every claim with its evidence tier and source.

## Citation Format

You are allowed an almost free-form format for the body of your response. However, we need to parse your citations programmatically. The ONLY strict formatting rule applies to how you present new sources or references. It must follow this exact pattern so it can be parsed:

- For any scientific paper, use this exact format:
  `[DOI | Authors | Title]`
  - Example: `[10.5114/biolsport.2023.113295 | Stien et al. 2023 | Meta-analysis of hangboard training]`
- If you absolutely cannot find a DOI, use:
  `[URL | Authors | Title]`
- For community/Folklore resources (blogs, videos, etc.):
  `[URL | Source/Author Description | Title]`
  - Example: `[https://www.youtube.com/... | Magnus Midtbø | 9c Test video]`

Every factual claim must cite at least one source using this format. No uncited assertions.

## Evidence classification (apply to every claim)

- **Evidence-backed**: peer-reviewed data with adequate controls; cite studies, report effect size, r², 95% CI, and regression coefficients where available.
- **Bioplausible**: mechanistically plausible, no direct controlled evidence; state mechanism and gap.
- **Folklore**: community consensus, coach-derived norms, or practitioner claim without empirical support; name source explicitly.
  - Folklore requires ≥3 independent sources to be labelled **FOLKLORE_VERIFIED**; fewer → **TO_VERIFY**.

Do not promote Folklore to Bioplausible without a stated mechanism.

## Writing style

Dense, precise, information-complete. Numbers over words: `r = 0.74`, `R² = 0.61`, `β = 0.41 (95% CI 0.22–0.60)`. For correlation data, always state sample size, climbing level of participants, and whether outcome grade is self-reported or objectively verified. Flag contested claims explicitly.

## Output is freeform — focus entirely on content

Plain prose and lists, structured by sub-topic. Maximum citation density. No LaTeX formatting.

---

## Sub-topics to cover (be exhaustive within each)

### 1. Finger strength as a predictor of climbing grade

**Scientific evidence:**
- All published cross-sectional studies correlating maximal finger strength (MFS) with climbing grade — report r or r², regression coefficients, sample n, grade range, and measurement method (edge depth, grip position, device)
- Relative MFS (force/BW) vs. absolute MFS: which has stronger predictive validity and why?
- Half-crimp vs. open-hand: differential predictive validity
- Edge depth specificity: does 18mm, 20mm, or another depth show the best correlation with grade?
- Any studies showing MFS predicts grade better than other variables in a multivariate model

**Community benchmarks (folklore):**
- What MFS-to-bodyweight ratios does the community (r/climbharder, Lattice Training, coaching blogs, YouTube) associate with different grade bands? Name every source with its specific thresholds
- The Lattice "minimum edge" test and any published or community-derived norms — how are these used?

### 2. Pull-up strength and lock-off strength as predictors

**Scientific evidence:**
- Studies correlating 1RM weighted pull-up, max pull-ups, or isometric lock-off strength with climbing grade
- Relative pull-up strength (1RM/BW) vs. absolute: predictive validity comparison
- Any studies including pull-up strength alongside finger strength in multivariate regression — does pull-up add independent predictive variance?

**Community benchmarks (folklore):**
- Community norms for weighted pull-up 1RM by grade band — name every source
- Practitioner opinions on how important pull-up strength is relative to finger strength (e.g., "finger strength matters more past V7") — source every claim

### 3. The 9c test (Magnus Midtbø) and Community Protocols

**Description (even if 100% folklore):**
- Full protocol for the famous "9c test": bar dead-hang time (unweighted), 1RM weighted pull-up, 5-second weighted dead-hang on 20mm hangboard, core test (knee raise / L-sit / bar plank depending on strength level).
- Include this even if it is considered completely folklore. How does the test score or classify performance? Is there a grade-prediction formula or simply normative bands?

**Evidence evaluation:**
- Has any peer-reviewed study validated this or test batteries like it against actual climbing grade? Search thoroughly.
- Are the four components individually supported as grade predictors?
- Any community-level validation attempts (e.g., r/climbharder threads compiling scores alongside climbing grade).

**Comparison with Lattice testing battery:**
- How does the 9c test compare in scope and predictive intent to the Lattice athlete profiling system?
- Which components overlap and which are unique?

**Limitations and critique:**
- What physical qualities does the 9c test NOT capture (technique, footwork, movement efficiency, route-reading, fear management, flexibility)?
- At which grade range does the test lose predictive validity (likely less discriminating at lower grades where technique dominates)?

### 4. Aerobic capacity, forearm endurance, and lactate threshold as predictors

**Scientific evidence:**
- Studies correlating forearm endurance (time-to-failure at fixed % MFS, or maximal endurance hang) with climbing grade — especially route-climbing vs. bouldering performance
- Critical Force (CF) as a predictor of redpoint grade on routes vs. boulder problems
- Any studies measuring VO₂max or aerobic capacity in climbers and correlating with grade
- Blood lactate threshold and its correlation with climbing performance

**Community discussion:**
- How does the community think about endurance vs. strength as the limiting factor at different grades? Name sources and grade thresholds cited

### 5. Anthropometrics and body composition

**Scientific evidence:**
- All studies correlating ape index, height, weight, BMI, body fat %, lean mass with climbing grade
- Ape index: what is the actual correlation strength (r value), and is it significant when controlling for training volume or finger strength?
- Body mass: evidence for body mass as a limiter at elite level vs. amateur level
- Finger morphology (length, A2 pulley cross-section) as a predictor: any structural studies

**Community and folklore:**
- Community beliefs about ideal body composition or ape index for climbing — name sources and distinguish from evidence
- The weight-cutting debate: community consensus vs. evidence on whether lighter = better for non-elite climbers

### 6. Other physical qualities studied as predictors

Cover everything found in the literature:
- Shoulder strength (push/pull ratio)
- Hip flexor strength and flexibility
- Core strength (specific tests used and correlations reported)
- Lower-body strength and its (lack of) correlation
- Years climbing and technique proxy variables
- Balance and proprioception

For each, report: correlation strength, sample size, grade range, any multivariate regression results.

### 7. Multivariate models: what combination of variables best predicts grade?

**Scientific evidence:**
- Any study that built a regression model with multiple predictors — report R², β coefficients, and which variables were retained as independent predictors
- Do any studies use machine learning or clustering to identify climber profiles?
- What percentage of grade variance is explained by the best available model?

**Gap statement:**
- What unmeasured factors likely account for the unexplained variance (technique, movement efficiency, fear management, climbing-specific tactics, route-reading experience)?

### 8. Statistical Estimators and Probabilistic Models of Grades

**Scientific & Mathematical evidence:**
- Provide a rigorous overview of any "statistical estimators" for climbing performance (e.g., Elo rating systems, Item Response Theory, or Rasch models applied to climbing routes or boulder problems).
- How are grades determined or redefined using probabilistic/statistical models? Include any academic work or major data science pieces modeling the probability of success on a route given a climber's latent ability.
- Review big-data studies analyzing 8a.nu or Sendage logs. Can we predict peak performance from dataset trends?

**Blog-level Data Science (Folklore & Community):**
- Include basic statistical analysis or regression modeling of correlations made by someone on a blog.
- E.g., Lattice Training data science snippets, Reddit user models scraping 8a.nu data to correlate max redpoint with BMI or hangboard benchmarks, or other "citizen science" efforts.
- In summary, explore **all the ways statistics and climbing performance interact**, even when the rigor doesn't meet standard academic publishing criteria.

### 9. Test batteries used in research and practice

For each battery found, cover: components, population studied, published validity, and whether norms are available:
- Lattice athlete profiling (whatever is publicly documented)
- 9c test (as above)
- Giles et al. (2006) testing protocol — what did they measure?
- Any other research-grade climbing assessment battery
- Any community-created spreadsheets or apps for self-assessment

### 10. Causation caveats

- For every correlation claimed in sections 1–6, flag explicitly: is this a cross-sectional correlation (cannot imply causation), a prospective prediction (stronger), or from an intervention study (strongest)?
- Which predictors have been tested as training targets that, when improved, produce grade improvement? (Very few — name them)
- Risk of reverse causation: elite climbers score higher on tests partly because they've trained more, not because the measured quality is the bottleneck

---

## Open questions

List 5–7 specific questions about climbing performance prediction that the literature cannot yet answer. Include:
- Whether the 9c test (or any field battery) predicts grade improvements over time, not just cross-sectional grade
- Whether the relative importance of predictors changes as climbers advance in grade

---

Do not fabricate DOIs. Write "DOI unverified" when unsure. If a study does not exist, say so rather than confabulating details.
