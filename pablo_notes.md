# Some extensions or modifications to make

## 1. Figures
I want a lot more figures:
- For each paper that we use the findings of, we should aim to import their main figure if they have a cool one.
- We should have a diagram of crimp positions and of the nomenclature of joints/ligaments/pulleys in the fingers.
- Correlations between climbing grade (in various versions of the sport), finger strength, pull-up abilities,... whatever we can find with sources.
and maybe other cool stuff.

## 2. Injuries
I want a new/better section on finger injuries:
- type of injuries,
- ways to avoid them (with a deepdive on how to warmup properly), 
- symptoms,
- diagnostics,
- rehab protocols.

## 3. Equipment
List of equipement, listed by ROI/bang-for-your-buck, to improve training (are weird hangboards that shape your fingers useful? force measuring devices? weird gym attachements?)

## 4. Scientific Measurments
Tindeq Critical Force, W', peak force left vs right,... I want a thorough overview of metrics people use to assess their progress/strength/ability.

## 5. Skin care
A deepdive on skincare practices and tricks (without images this time haha it's too gross). It seems to me like two big schools are:
- keep it as dry as you can, file it,...
- keep it very moist, use cream/moisturizer all the time, let it heal naturally,...
I want as scientific of a dive as possible. This is a topic where I think the community/folklore knowledge might be super biased so it's kinda interesting to appraoch it critically/rigorously.

## 6. bib
EVERY single citation must be a bib entry in `bibliography.bib` and must be throughly verified with a metadata extractor python script. In the big tables listing all the papers, we should use \cite{...} commands instead of writing the paper manually. It should just be `Authors \cite{...}` in the first column. This must be made into an unbreakable rule in `CLAUDE.md`. Read the content of `../BourbakIA/bourbakia/cite/` and copy the agents and scripts from there that could be useful here.

## 7. Numbering of files
We kept the old numbering of files in `sections/` but it doesn't make sense anymore. Can we redesign the file names?

## 8. Agentic workflow
Read the content of `../BourbakIA/bourbakia/critique/` and help me copy a `critique` agentic workflow. Copy the agents and scripts from there that could be useful here. The ultimate goal is that this can be made into a github repo I can share with the `r/climbharder` subreddit. Then the redditors could help me improve it by either manually suggesting changes, or by using LLMs+Claude to automate improvements. Collaborative agent-powered lit review, where others can help me by essentially using their tokens to improve this.

## 9. Neutrality
There can be NO mention of how we sourced the information (no mention of Grok, Meta, Perplexity,...). We can just say in the method that free-tiers of frontier LLMs were prompted for feedback, and Claude Sonnet 4.6 orchestrated the whole project.