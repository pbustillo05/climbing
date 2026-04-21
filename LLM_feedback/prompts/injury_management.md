# Prompt — Finger Injury Management Section Review

## Context and purpose

I am writing a scientific literature review on training for rock climbing, and I need multiple LLMs to thoroughly review the current draft of my "Finger Injury Management" section.

**Your task**: Perform an **EXHAUSTIVE web search** across PubMed, Google Scholar, sports medicine/orthopedics journals, and climbing community hubs (e.g., The Climbing Doctor, Hooper's Beta, r/climbharder, UKClimbing). Your main role is to explore the literature and community knowledge base to find:
1. **Mistakes or outdated information** in the current text.
2. **Gaps in the literature** (e.g., comprehensive coverage of all soft-tissue, luminal, and joint finger injuries weighted by their prevalence and recurrence rates, unloader rings, the role of NSAIDs, the "rest vs load" debate for various tendinopathies) that the section misses.
3. **Questionable claims** that lack sufficient evidence or misrepresent the source text.
4. **Folklore or community practices** regarding finger rehab that we haven't addressed.

You will be provided with:
- The LaTeX content of the section (`sections/injury_management.tex`).
- The current bibliography (`bibliography.bib`).

## Formatting Rules

You are allowed an almost free-form format so you can focus entirely on the content—plain prose, bullet points, whatever works best to convey your findings.

**The ONLY strict formatting rule** applies to how you present new sources or references. It must be minimalist and follow this exact pattern so I can easily parse them with Python scripts to verify and add them to my `.bib` file:

- For any new scientific paper you suggest, you MUST use this exact format:
  `[DOI | Authors | Title]`
  - Example: `[10.1007/s00402-023-05118-x | Lutter et al. | Mechanisms of acute climbing injuries in the fingers]`
- If you absolutely cannot find a DOI, use:
  `[URL | Authors | Title]`
- For community/Folklore resources (blogs, videos, etc.):
  `[URL | Source/Author Description | Title]`
  - Example: `[https://www.youtube.com/... | The Climbing Doctor | Finger injury rehab overview]`

## Instructions

1. **Read** the provided `sections/injury_management.tex` and note all existing claims on diagnostic techniques, rehab timelines (covering ANY type of finger injuries across the full spectrum, weighting heavily those with high recurrence), taping methods, and returning to sport.
2. **Search exhaustively** on the web for recent climbing-specific injury management papers and physical therapy protocols (like Schöffl, Lutter, or Schweizer). Look for systematic reviews and clinical guidelines on all forms of finger pathologies.
3. Compare the findings. If we missed a major paper or a standardized rehab protocol, flag it. If an injury timeline is too aggressive/conservative according to the latest research, critique it.
4. Identify any gaps: Is the role of eccentric loading in tendinopathy missing? Are diagnostic tests (ultrasound vs MRI) accurately represented?
5. **Output your critique**, suggested additions, and corrected facts in whatever structural format you prefer (free-form).
6. **Provide all new references** explicitly using the bracketed format defined above.
7. Do not rewrite the `.tex` file for me. Just provide your research findings, critique, and references.
