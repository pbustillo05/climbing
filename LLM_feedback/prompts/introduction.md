# Prompt — Introduction & Methods Review

## Context and purpose

I am writing a scientific literature review on training for rock climbing, and I need multiple LLMs to thoroughly review the current draft of my "Introduction" and "Methods".

**Your task**: Perform an **EXHAUSTIVE web search** across recent climbing science overviews and sports science epistemologies. Your main role is to explore the literature to find:
1. **Mistakes or outdated information** in the current text's framing of the field.
2. **Gaps in the literature** (e.g., historical context of climbing research, definitions of terms like "bouldering" vs "sport climbing", grade conversions, and how the evidence strength score (ESS) maps onto traditional GRADE frameworks).
3. **Questionable framing** about the relative weight of folklore vs. science in the sport.

You will be provided with:
- The LaTeX content of the section (`sections/introduction.tex` and `sections/methods.tex`).
- The current bibliography (`bibliography.bib`).

## Formatting Rules

You are allowed an almost free-form format so you can focus entirely on the content—plain prose, bullet points, whatever works best to convey your findings.

**The ONLY strict formatting rule** applies to how you present new sources or references. It must be minimalist and follow this exact pattern so I can easily parse them with Python scripts to verify and add them to my `.bib` file:

- For any new scientific paper you suggest, you MUST use this exact format:
  `[DOI | Authors | Title]`
  - Example: `[10.1007/s40279-015-0331-5 | Saul et al. | Physiology of Rock Climbing]`
- If you absolutely cannot find a DOI, use:
  `[URL | Authors | Title]`
- For community/Folklore resources:
  `[URL | Source/Author Description | Title]`

## Instructions

1. **Read** the provided `sections/introduction.tex` and `sections/methods.tex` and note all existing claims on the evolution of climbing science and grading systems.
2. **Search exhaustively** on the web for high-level climbing science reviews and epistemological frameworks for sports science mapping.
3. Compare the findings. If we missed a major foundational paper summarizing climbing science, flag it!
4. Identify any gaps: Are the definitions precise? Does the methodology for finding papers fall short in a way we should address?
5. **Output your critique**, suggested additions, and corrected facts in whatever structural format you prefer (free-form).
6. **Provide all new references** explicitly using the bracketed format defined above.
7. Do not rewrite the `.tex` files for me. Just provide your research findings, critique, and references.
