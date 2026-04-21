# Prompt — Weekly Training Integration Section Review

## Context and purpose

I am writing a scientific literature review on training for rock climbing, and I need multiple LLMs to thoroughly review the current draft of my "Weekly Training Integration" section.

**Your task**: Perform an **EXHAUSTIVE web search** across PubMed, Google Scholar, sports science journals, and climbing community hubs (e.g., r/climbharder, Lattice Training, Power Company Climbing, Hooper's Beta). Your main role is to explore the literature and community knowledge base to find:
1. **Mistakes or outdated information** in the current text.
2. **Gaps in the literature** (e.g., how to periodize climbing with hangboarding vs. lifting, non-linear vs. linear periodization, fatigue management, minimal effective volume) that the section misses.
3. **Questionable claims** that lack sufficient evidence or misrepresent the source text.
4. **Folklore or community practices** regarding structuring a training week that we haven't addressed.

You will be provided with:
- The LaTeX content of the section (`sections/weekly_integration.tex`).
- The current bibliography (`bibliography.bib`).

## Formatting Rules

You are allowed an almost free-form format so you can focus entirely on the content—plain prose, bullet points, whatever works best to convey your findings.

**The ONLY strict formatting rule** applies to how you present new sources or references. It must be minimalist and follow this exact pattern so I can easily parse them with Python scripts to verify and add them to my `.bib` file:

- For any new scientific paper you suggest, you MUST use this exact format:
  `[DOI | Authors | Title]`
  - Example: `[10.1519/JSC.0000000000002049 | Smith et al. | Periodization block variations in elite climbers]`
- If you absolutely cannot find a DOI, use:
  `[URL | Authors | Title]`
- For community/Folklore resources (blogs, videos, etc.):
  `[URL | Source/Author Description | Title]`
  - Example: `[https://www.powercompanyclimbing.com/... | Power Company | High-Low training weeks]`

## Instructions

1. **Read** the provided `sections/weekly_integration.tex` and note all existing claims on block periodization, exercise ordering, volume loads, etc.
2. **Search exhaustively** on the web for recent strength & conditioning / climbing periodization papers and community heuristics.
3. Compare the findings. If we missed a major paper or a programming consensus detail among elite coaches, flag it.
4. Identify any gaps: Is the scheduling of strength vs. skills missing? Are recovery constraints overlooked?
5. **Output your critique**, suggested additions, and corrected facts in whatever structural format you prefer (free-form).
6. **Provide all new references** explicitly using the bracketed format defined above.
7. Do not rewrite the `.tex` file for me. Just provide your research findings, critique, and references.
