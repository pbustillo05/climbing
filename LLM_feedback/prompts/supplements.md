# Prompt — Supplements Section Review

## Context and purpose

I am writing a scientific literature review on training for rock climbing, and I need multiple LLMs to thoroughly review the current draft of my "Supplements" section.

**Your task**: Perform an **EXHAUSTIVE web search** across PubMed, Google Scholar, sports nutrition journals, and climbing community hubs (e.g., r/climbharder, Lattice Training, Hooper's Beta). Your main role is to explore the literature and community knowledge base to find:
1. **Mistakes or outdated information** in the current text.
2. **Gaps in the literature** (studies on creatine, collagen, beta-alanine, caffeine, etc., directly in climbing or highly relevant adjacent sports that the section misses).
3. **Questionable claims** that lack sufficient evidence or misrepresent the source text.
4. **Folklore or community practices** regarding supplements that we haven't addressed.

You will be provided with:
- The LaTeX content of the section (`sections/supplements.tex`).
- The current bibliography (`bibliography.bib`).

## Formatting Rules

You are allowed an almost free-form format so you can focus entirely on the content—plain prose, bullet points, whatever works best to convey your findings.

**The ONLY strict formatting rule** applies to how you present new sources or references. It must be minimalist and follow this exact pattern so I can easily parse them with Python scripts to verify and add them to my `.bib` file:

- For any new scientific paper you suggest, you MUST use this exact format:
  `[DOI | Authors | Title]`
  - Example: `[10.1123/ijsnem.2017-0133 | Shaw et al. | Vitamin C–enriched gelatin supplementation before intermittent activity augments collagen synthesis]`
- If you absolutely cannot find a DOI, use:
  `[URL | Authors | Title]`
- For community/Folklore resources (blogs, videos, etc.):
  `[URL | Source/Author Description | Title]`
  - Example: `[https://www.youtube.com/... | Hooper's Beta | Do climbing supplements actually work?]`

## Instructions

1. **Read** the provided `sections/supplements.tex` and note all existing claims, studies, and dosages.
2. **Search exhaustively** on the web for recent papers (especially post-2020) on the same supplements and any new ones popular in climbing/strength sports. Look for systematic reviews and meta-analyses.
3. Compare the findings. If we missed a major paper or a climbing-specific RTC, flag it. If a claim in the text is too strong according to the latest research, critique it.
4. Identify any gaps: Are there side effects (e.g., creatine weight gain, GI distress) or practical climbing applications missing?
5. **Output your critique**, suggested additions, and corrected facts in whatever structural format you prefer (free-form).
6. **Provide all new references** explicitly using the bracketed format defined above.
7. Do not rewrite the `.tex` file for me. Just provide your research findings, critique, and references.
