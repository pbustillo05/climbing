# Prompt — Hangboarding Section Review

## Context and purpose

I am writing a scientific literature review on training for rock climbing, and I need multiple LLMs to thoroughly review the current draft of my "Hangboarding" section.

**Your task**: Perform an **EXHAUSTIVE web search** across PubMed, Google Scholar, sports science journals, and climbing community hubs (e.g., r/climbharder, Lattice Training, Hooper's Beta, Eva López's blog). Your main role is to explore the literature and community knowledge base to find:
1. **Mistakes or outdated information** in the current text.
2. **Gaps in the literature** (e.g., recent studies on max hangs vs. repeaters, minimal edge depth, finger biomechanics, injury mechanisms during hangboarding that the section misses).
3. **Questionable claims** that lack sufficient evidence or misrepresent the source text.
4. **Folklore or community practices** regarding hangboarding that we haven't addressed.

You will be provided with:
- The LaTeX content of the section, which includes: 
   - `sections/biomechanics.tex`
   - `sections/intervention_studies.tex`
   - `sections/practitioner_consensus.tex`
   - `sections/discussion.tex`
- The current bibliography (`bibliography.bib`).

## Formatting Rules

You are allowed an almost free-form format so you can focus entirely on the content—plain prose, bullet points, whatever works best to convey your findings.

**The ONLY strict formatting rule** applies to how you present new sources or references. It must be minimalist and follow this exact pattern so I can easily parse them with Python scripts to verify and add them to my `.bib` file:

- For any new scientific paper you suggest, you MUST use this exact format:
  `[DOI | Authors | Title]`
  - Example: `[10.1080/02640414.2020.1804782 | Lopez-Rivera et al. | The effects of two maximum grip strength training methods using the same effort duration and different edge depth on grip endurance in elite climbers]`
- If you absolutely cannot find a DOI, use:
  `[URL | Authors | Title]`
- For community/Folklore resources (blogs, videos, etc.):
  `[URL | Source/Author Description | Title]`
  - Example: `[https://www.youtube.com/... | Hooper's Beta | Max Hangs vs Repeaters]`

## Instructions

1. **Read** the provided LaTeX files that make up the Hangboarding section, and note all existing claims on biomechanics, training interventions, consensus, and discussion points.
2. **Search exhaustively** on the web for recent hangboarding papers (especially post-2020 RCTs and systematic reviews).
3. Compare the findings. If we missed a major paper, flag it. If a claim in the text is too strong according to the latest research, critique it.
4. Identify any gaps: Are there side effects, nuances about edge depths, half-crimp versus drag biomechanics, or practical training variations missing?
5. **Output your critique**, suggested additions, and corrected facts in whatever structural format you prefer (free-form).
6. **Provide all new references** explicitly using the bracketed format defined above.
7. Do not rewrite the `.tex` files for me. Just provide your research findings, critique, and references.
