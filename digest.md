# Digest: week of 28 September 2026

## Anthropic news

### Claude discovers a novel enzyme system with CRISPR-like repeats
23 September 2026
https://www.anthropic.com/news/claude-discovers-novel-enzyme-system

Anthropic has formed a new life sciences research team that uses Claude to explore DNA datasets and generate research hypotheses with only high level direction from scientists. In an early result, Claude autonomously identified a previously unnoticed enzyme system built around a reverse transcriptase, including an array of DNA repeats similar to CRISPR and an accessory protein of unknown function. The team does not yet know what the system does, but its combination of features has only been seen in a handful of other systems, all of which turned out to be programmable tools for editing DNA.

### Partnering with Accenture on embedded evaluation
18 September 2026
https://www.anthropic.com/news/accenture-embedded-evaluation

Anthropic is partnering with Accenture, through its Faculty AI unit, to embed external evaluators inside the company with employee level access to red team models, run alignment assessments and test safeguards. Both companies plan to invest at least 1 billion dollars each over five years, and Anthropic is funding Accenture's work directly for now since no shared system for funding independent evaluators yet exists. Anthropic says this does not reduce its own responsibility for model safety, but is meant to make its safety claims independently verifiable, and it plans to bring on more evaluators over time.

### Introducing the Life Sciences Verification Program
17 September 2026
https://www.anthropic.com/news/life-sciences-verification-program

Anthropic launched the Life Sciences Verification Program, giving verified life science professionals more permissive access to its Mythos, Opus and Sonnet models for work such as drug discovery and clinical research that is normally blocked by its general safety classifiers. Applicants go through a vetting process covering research credentials, security and ethical oversight, then can apply for a Standard Use grant covering most day to day work, or a narrower High risk Use grant for specific higher risk projects that removes additional safeguards. The program is launching in beta for teams and institutions, with access for individual Pro and Max plans planned later.

## Ideas to try

1. The Claude Science team's approach, giving Claude a dataset and high level direction and letting it explore and generate hypotheses on its own, is a useful structure to copy for a Claude Code skill that scans India Grace's stock or sales data each week and flags anomalies or ideas for Ella to review, rather than building one monolithic script that does everything.
2. Anthropic's embedded evaluation partnership pairs its models with an independent checker rather than trusting them unsupervised. Ella could build the same pattern into any India Grace automation she creates in Claude Code, for example an agent that drafts Meta ads copy or bid changes, by adding a second review step that checks the first agent's output before anything goes live.
3. The Life Sciences Verification Program tiers model access and safeguards by verified use case rather than a single flat setting. When Ella sets permissions for her own Claude Code agents and skills, this is worth copying: split automations into low risk tasks that can run with fewer confirmations, such as pulling a weekly stock report, and higher risk ones that always need her sign off, such as anything that spends money or emails customers.

## Sources that failed

- Ethan Mollick, One Useful Thing
- Zvi Mowshowitz
- Dwarkesh Patel
- Azeem Azhar, Exponential View
- swyx, Latent Space
- Simon Willison
- Benedict Evans
- Andrej Karpathy
- Daniel Miessler
- The Rundown
- Dario Amodei essays
