### High-confidence problems / likely mistakes in the current draft

1. **Caffeine meta-analysis citation appears mismatched (important).**  
   In `supplements.tex`, you cite **Windt et al. (2018) Br J Sports Med** as “Grgic et al. (2020) … caffeine strength/endurance ES …” via `\cite{WTNZ18}`. But your `bibliography.bib` entry `WTNZ18` is **about validity theory for athlete self-report measures**, not caffeine. That’s a hard factual/citation error and will propagate into your “Best general evidence” claims.  
   *Action:* replace `WTNZ18` with the correct caffeine meta-analysis key(s) (see “New references” below).

2. **Beta-alanine meta-analysis “Hobson 2012” is cited in prose but not in your bib (at least in the excerpt).**  
   Your section references “Hobson et al. (2012, Amino Acids, meta-analysis…)” but I don’t see a corresponding BibTeX entry in the excerpt you provided. If it’s missing in the actual file, that’s a governance + completeness issue.

3. **Beetroot/nitrate and sodium bicarbonate are absent despite being common “high-intensity intermittent” ergogenics relevant to climbing-style efforts.**  
   Even if you ultimately conclude “no direct climbing grade RCT evidence,” these are common in strength/endurance communities and would likely be asked about on r/climbharder.

4. **Creatine: you correctly flag lack of climbing-specific RCTs, but you may be missing “adjacent task” nuance.**  
   For bouldering-style repeated maximal efforts (10–60 s with long rests), creatine is plausibly more relevant than for long sport routes; your current caveat is mostly mass gain. Consider explicitly separating “absolute force/power benefit” vs “strength-to-weight trade-off” by discipline.

---

### Missing or under-covered scientific literature (esp. post‑2020) that is directly climbing-related or “near-climbing”

#### A) Dietary nitrate / beetroot juice (climbing-specific studies exist; mixed results)
You currently do not cover nitrate/BRJ at all, but there is **climbing-specific research**:

- One study in *Journal of Human Kinetics* reports **no improvement** in neuromuscular performance in male sport climbers after acute beetroot juice ingestion (cross-over design; DOI present). ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/37229410/?utm_source=openai))  
- A newer “climbers” paper exists but appears to be **mountain climbers** (altitude trekking context), not rock climbers; still relevant as “climber” wording can confuse readers and should be disambiguated if you include it. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/40323707/?utm_source=openai))

**Why this matters for your section:** nitrate is popular, the evidence is mixed, and you already have a pattern of reporting null vs positive results (good). This fits well.

#### B) Caffeine: replace the incorrect meta-analysis citation; add at least one canonical caffeine strength/power meta-analysis
You already include a climbing-specific caffeine RCT (good, 2026). ([mdpi.com](https://www.mdpi.com/2072-6643/18/2/284?utm_source=openai))  
But your “general evidence” citations need fixing/expanding. A commonly cited systematic review/meta-analysis in sports nutrition on caffeine and strength/power exists (2018 JISSN). ([jissn.biomedcentral.com](https://jissn.biomedcentral.com/articles/10.1186/s12970-018-0216-0?utm_source=openai))  
Also, an older but still canonical MSSE meta-analysis exists (2010). ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/20019636/?utm_source=openai))  
(You can decide which to feature; your manuscript’s “dense, numeric” style suggests including at least one effect size + CI source.)

#### C) Beta-alanine: cite the actual meta-analysis DOI you quote (it exists and is open)
Your text already uses the key numeric (median ES ~0.374; 60–240 s window). The primary Hobson meta-analysis DOI is resolvable and on PMC. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC3374095/?utm_source=openai))

#### D) Sodium bicarbonate (strongly relevant to 1–7 min high-intensity, but GI-limited)
Not currently discussed. There are multiple systematic reviews/meta-analyses on sodium bicarbonate performance; likely “bioplausible → evidence-backed (non-climbing)” category. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/31191097/?utm_source=openai))  
It also has a practical relevance: **GI distress risk** is unusually high and could be safety-relevant in climbing (cramping, urgent bathroom needs at crag/comp).

---

### Questionable / overstated / needs tighter classification

1. **“Only climbing-specific caffeine RCT” claim is currently true in your draft context, but should be stated with date anchoring.**  
   Given you’re writing on **2026-04-21**, phrase as “As of 2026-04-21, only one published climbing-specific caffeine RCT…” to future-proof.

2. **Vitamin C “critical gap” framing is fine mechanistically, but be careful not to imply proven necessity.**  
   You do state the RCT gap (“No factorial RCT…”)—keep that explicit. But the “single highest-priority protocol modification” sentence reads close to prescriptive certainty. Consider tightening to: “highest-priority *mechanistically plausible* modification; necessity untested.”

3. **Omega-3 Mendelian randomization claim needs sourcing.**  
   You flag it “single-source claim” (good), but right now it’s a naked statement. If you keep it, it needs a DOI/URL and careful MR limitations (instrument validity, pleiotropy, phenotype definition like ICD-coded tendinitis vs clinically verified).

---

### Community / folklore gaps worth adding (even if only as TO_VERIFY buckets)
You asked for climbing hubs like r/climbharder/Lattice/Hooper’s Beta; I didn’t yet pull those pages in this pass, but based on what repeatedly appears in climbing supplement discussions, you likely want explicit folklore boxes for:

- **“Beetroot juice / nitrates for ‘pump’ reduction”** (common in endurance circles; would map to forearm oxygenation folklore in climbing).  
- **“Sodium bicarbonate to ‘buffer pump’”** (common in CrossFit/boxing circles; plausible crossover).  
- **“Creatine is only for boulderers / ruins sport climbing”** (you partially address; could formalize as folklore + quantify plausible mass gain distribution).  
- **Electrolytes/salt loading for cramping / forearm pump** (often asserted; evidence mixed; likely TO_VERIFY unless you decide it’s outside scope).

If you want, I can do a dedicated second pass that **only** harvests “≥3 independent community sources” per folklore claim to meet your FOLKLORE_VERIFIED policy.

---

## New references to consider (minimalist bracket format)

### Fix your caffeine meta-analysis citation problem
- [10.1186/s12970-018-0216-0 | Grgic et al. | Effects of caffeine intake on muscle strength and power: a systematic review and meta-analysis] ([jissn.biomedcentral.com](https://jissn.biomedcentral.com/articles/10.1186/s12970-018-0216-0?utm_source=openai))  
- [10.1249/MSS.0b013e3181cabbd8 | Warren et al. | Effect of caffeine ingestion on muscular strength and endurance: a meta-analysis] ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/20019636/?utm_source=openai))  

### Beta-alanine meta-analysis you are already using numerically
- [10.1007/s00726-011-1200-z | Hobson et al. | Effects of β-alanine supplementation on exercise performance: a meta-analysis] ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC3374095/?utm_source=openai))  

### Nitrate / beetroot juice — climbing-specific (null finding)
- [10.5114/jhk/161812 | (Authors listed on PubMed record) | Dietary Nitrate Ingestion Does Not Improve Neuromuscular Performance in Male Sport Climbers] ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/37229410/?utm_source=openai))  

### Nitrate / beetroot juice — “climbers” but likely mountaineering context (include only if you explicitly separate it from rock climbing)
- [URL | (PubMed record) | The effect of acute beetroot juice consumption prior to climbing on lower-body isokinetic and isometric strength, aerobic power, and muscle soreness among mountain climbers] ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/40323707/?utm_source=openai))  

### Sodium bicarbonate (non-climbing, but highly relevant physiology)
- [URL | Hadzic et al. | The Impact of Sodium Bicarbonate on Performance in Response to Exercise Duration in Athletes: A Systematic Review] ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/31191097/?utm_source=openai))  
- [URL | (Authors per PMC) | Effect of sodium bicarbonate supplementation on two different performance indicators in sports: a systematic review with meta-analysis] ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8076585/?utm_source=openai))  

---

### Next minimal questions (so I don’t over-ask)
1. Do you want nitrate/BRJ and sodium bicarbonate added as **full subsections** (like creatine/caffeine) or as a smaller “Other common ergogenics” subsection?  
2. Are you okay with me doing a **second web pass explicitly targeting r/climbharder + Lattice + Hooper’s Beta** to collect ≥3 independent sources per folklore claim (to meet your FOLKLORE_VERIFIED rule)?