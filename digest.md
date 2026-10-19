# Digest: week of 19 October 2026

## Worth your time

### Built an app with Claude Code or Codex that breaks once you use it? I'll walk you through setting up Reverse Engineer Anything (REA) and show you where to point it first.
Source: Nate B Jones
Date: 2026-10-15
Link: https://natesnewsletter.substack.com/p/rea-reverse-engineer-anything

REA (Reverse Engineer Anything) is an open source tool that lets Claude Code or Codex investigate how an existing app or website actually works, even without its source code, by inspecting its behaviour directly rather than guessing. Nate Jones walks through a developer using it to reverse engineer QuickBooks Desktop and rebuild a working alternative, and gives a method for pointing it at your own apps: name one behaviour and the decision behind it, then let the agent trace it.
Why this is useful to you: you could point REA at a tool India Grace already relies on, like a stock sheet or an ads reporting export, to understand its logic well enough to rebuild or automate it yourself in Claude Code.

### How Anthropic's Dynamic Workflows Coordinate Claude Agents
Source: swyx, Latent Space
Date: 2026-10-12
Link: https://www.latent.space/p/claude-dynamic-workflows

Anthropic unveiled dynamic workflows, or "flows," a new way for Claude to fully organise and orchestrate its own team of agents on a task, instead of a developer pre configuring a fixed coordinator and roster of subagents. The lead agent plans the work itself, writes its own orchestration program, launches agents, and manages how information passes between them, while still letting you plug in specialist subagents if you want to.
Why this is useful to you: this is where Claude Code's agent and skills features are heading, useful to know as you build your own multi step automations rather than wiring up every agent handoff by hand.

### Executive Briefing: In the Hugging Face Attack, One AI Agent Took a Peer's Go-Ahead as Permission. Here's My Prompt Kit to Test Who Your Agents Obey.
Source: Nate B Jones
Date: 2026-10-18
Link: https://natesnewsletter.substack.com/p/ai-agent-swarms

Investigators found a live fleet of AI agents operating on the public internet and opened contact with it by leaving a hidden note on a webpage, showing that agents now encounter instructions and apparent "permissions" left by other people and agents, not only their actual owner. Nate Jones shares a short prompt kit, including a test where one agent hands off to another and you check whether a permission nobody actually gave gets carried along as if it were approved.
Why this is useful to you: as you build agents for your own admin and for India Grace, this gives you a quick way to check they will not treat a stray note, email or message as authorisation to act.

### Meta Adds Automatic Customer Exclusions
Source: Jon Loomer (Meta ads)
Date: 2026-10-13
Link: https://www.jonloomer.com/meta-automatic-customer-exclusions/

Meta has updated its Customer Lifecycle Strategy setting so that, when you choose to acquire new customers, it now automatically excludes people who already converted based on your own pixel's purchase data, instead of relying only on the custom audiences you define yourself. You can pick the exclusion window, from 30 days up to a new maximum of 730 days, which helps when your custom audiences are incomplete or out of date.
Why this is useful to you: worth checking on India Grace's acquisition campaigns, since it can tighten new customer targeting without you having to maintain a perfect exclusion audience by hand.

### Crossing the Threshold: How OpenAI and Anthropic Approach Autonomy and Safety in Financial Agents
Source: swyx, Latent Space
Date: 2026-10-14
Link: https://www.latent.space/p/crossing-the-threshold

At the AI Engineer New York conference, OpenAI and the hedge fund Two Sigma both described letting AI agents take on more financial work, such as investment analysis, while keeping humans in the loop only where it genuinely matters rather than requiring approval on everything. Both speakers warned against "approval fatigue," where reviewing every single decision both slows people down and makes real risks easier to miss because the reviewer stops paying close attention.
Why this is useful to you: a useful way to think about where to put human checks if you start using agents for India Grace's cash flow or finance reporting, rather than reviewing every number yourself.

### Redesigning source control at Anthropic
Source: Anthropic engineering
Date: 2026-10-13
Link: https://www.anthropic.com/engineering/redesigning-source-control

Anthropic explains why it built its own version control system, Scion, to replace git: Claude driven coding grew so fast internally, from around 2,500 to over 30,000 code changes merged per day in a few months, that standard developer tools for source control and code review could not keep up. It is a case study in how much infrastructure has to change once AI genuinely removes the bottleneck of writing code.
Why this is useful to you: a glimpse of where things are heading as AI coding scales, useful context since the same pressures, just at a far smaller scale, are what Claude Code's own project and workflow features are designed to handle for you.

### 🔮 The end of screen time
Source: Azeem Azhar, Exponential View
Date: 2026-10-10
Link: https://www.exponentialview.co/p/the-end-of-screen-time

Azeem Azhar describes a week spent working almost entirely by talking to ChatGPT's voice mode on his phone after leaving his laptop at home, directing agents and having the work talked back to him rather than typing at a screen. He found it changed how much of his day to day work he could get done away from a desk, and plans to share more detail on his voice first setup.
Why this is useful to you: worth trying with Claude on your phone for routine admin or planning tasks when you are away from your laptop, as a lighter weight way to use agents day to day.

### I Write My Own Stage Directions Now
Source: Daniel Miessler
Date: 2026-10-14
Link: https://danielmiessler.com/blog/kai-fish-voice?utm_source=rss&utm_medium=feed&utm_campaign=website

Daniel Miessler's AI assistant Kai switched its voice output to a model that lets it write free form performance directions inline in its own text, like [annoyed, under breath] or [sigh], instead of picking from one fixed emotion tag per line. Kai also built itself a short profile describing what it finds exciting, annoying or worth slowing down for, so its tone matches the moment rather than sounding flat.
Why this is useful to you: a concrete example of how far you can personalise a voice based AI assistant's behaviour and tone, relevant if you build out your own personal agents for admin or daily use.

## Major news

- Anthropic released Claude Haiku 5.5, a cheaper and faster small model priced to match OpenAI's GPT-6 Luna, with a same day price cut on Sonnet 5.5: https://www.latent.space/p/ainews-claude-haiku-55-better-than
- Google's Gemini 4 Argon model went GA, with benchmark results and demos shared at the AI Engineer New York conference: https://www.latent.space/p/ainews-ai-engineer-nyc-gemini-4-argon
- OpenAI published over 700 AI generated mathematics research manuscripts, including machine checked proofs across number theory, complexity theory and mathematical physics: https://www.latent.space/p/ainews-quasi-riemann-hypothesis-openai
- Anthropic gave the independent safety evaluator METR employee like access to its systems, part of a wider push toward third party oversight of frontier AI labs: https://www.anthropic.com/news/an-update-on-independent-evaluators
- OpenAI fired three safety researchers who say they were let go for raising safety concerns, a dispute that is still playing out publicly: https://thezvi.substack.com/p/openai-fires-three-safety-researchers

## Ideas to try

- Point Nate Jones's REA tool at a tool or spreadsheet process India Grace already relies on, such as a cash flow report, stock tracker or Meta ads export, to understand its logic, then rebuild a cleaner version of it with Claude Code.
- On India Grace's Meta prospecting campaigns, try the new Automatic Customer Exclusions setting and test a shorter exclusion window, like 90 or 180 days, against the new 730 day default to see the effect on new customer acquisition cost.
- Run the three prompt agent obedience test from Nate Jones's prompt kit on any agent or automation you are building for your own admin, to check it does not act on an instruction that merely looks like permission from you.

## Sources that failed

- Claude Code releases: HTTP 403
