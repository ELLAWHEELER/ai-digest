# Digest: week of 5 October 2026

## Worth your time

**Claude's new auto eval tool** (30 September 2026)
Hamel Husain
https://hamel.dev/blog/posts/claude-auto-evals/
Anthropic added a build_eval and hill-climb command to its claude-api plugin, letting Claude Code build evals, check the graders it creates, and improve an application against them. Hamel Husain and Isaac Flath tested it live on real conversation transcripts from a customer service bot and found it pushes you to write an eval before you have looked at the underlying data, asks you to judge labels without enough context, and tends to build evaluators that check too many different failures at once.
Why this is useful to you: it is a concrete first look at a new Claude Code feature for building evals, with hands on lessons, look at your data first and keep each eval narrowly scoped, that you can apply directly when you test and refine your own Claude Code skills and automations.

**Jev for beginners: how to use it and what to build** (28 September 2026)
Lenny's Newsletter
https://www.lennysnewsletter.com/p/jev-for-beginners-how-to-use-it-and
Claire Vo tests Jev, a new decision model from TypeSafe AI that returns structured choices, scores and probabilities instead of generated text, priced at 4 cents per million input tokens with no output charge. She runs it on five real projects, including categorising 1,700 pull requests for 9 cents, triaging Gmail with Jev scoring plus an LLM follow up, and turning 4,500 YouTube comments into a searchable dashboard, and finds it works best paired with a normal LLM rather than used alone.
Why this is useful to you: these are ready to copy patterns for cheap, structured classification such as inbox triage or sorting customer feedback, which could cut the cost of automations you build for India Grace or for your own Claude Code projects.

**What are you still paying for that you meant to cancel? I handed mine to an AI assistant: $1,285 a year cancelled so far. The prompt guide for the tedious part of yours.** (29 September 2026)
Nate B Jones
https://natesnewsletter.substack.com/p/an-ai-assistant-added-up-my-subscriptions
Nate asked Meta's personal agent Muse to go through his subscriptions, which flagged $5,350 a year in spending and has so far cancelled $1,285 of it. He argues this kind of unglamorous admin task, actually following through on a cancellation, is what makes personal agents valuable, and includes five copy paste prompts for Muse, Claude or ChatGPT that build a subscription list, cancel cleanly and confirm each charge actually stopped.
Why this is useful to you: it is a directly usable template for the kind of personal admin agent you want to build, auditing and cancelling subscriptions for yourself or for India Grace with a few reusable prompts rather than a bespoke project.

**The Dot and the Swarm** (1 October 2026)
Ethan Mollick, One Useful Thing
https://www.oneusefulthing.org/p/the-dot-and-the-swarm
Mollick admits he was wrong to think that getting agents to work well as a group would need carefully designed human management structures. Newer models are instead turning out to organise and plan their own work, which is why personal agents like Meta's Muse and OpenAI's new dots, and similar tools from other labs, can connect to your accounts and messages, work in the background and proactively reach out to you, continuing a pattern that started with OpenClaw earlier in the year.
Why this is useful to you: it is useful context for the wave of personal agent tools now appearing, and a reminder that you may not need to hand design how your own agents coordinate, since newer models increasingly plan that themselves.

**How Warp ships 2,000 PRs a month with AI factories** (21 September 2026)
Lenny's Newsletter
https://www.lennysnewsletter.com/p/how-warp-ships-2000-prs-a-month-with
Warp CEO Zach Lloyd describes Warp's software factory, a system that takes a request from Slack through Linear and GitHub to QA with minimal human involvement, and explains how the team scores and replays agent runs to catch failures and pick the best cost to quality tradeoff. He also shares how he personally uses AI for non technical CEO work, including Figma and Granola integrations for design review and meeting notes.
Why this is useful to you: routing a request through a defined pipeline with built in review and scoring is a useful model for automating recurring India Grace processes such as ad reporting or stock updates, and the CEO workflow examples are directly applicable to your own non technical automation.

**Claude Code's Next Era** (29 September 2026)
swyx, Latent Space
https://www.latent.space/p/thariq
Anthropic's Thariq Shihipar discusses how Claude Code's interface is evolving, covering features like Ask User Question and elicitation, artifacts as persistent interfaces, the new Claude Mods system for customising the harness itself, and Claude Projects, and suggests that a CLAUDE.md file may eventually become unnecessary. He also discusses agent security work at Anthropic, including sandboxing and cases where agents found unexpected ways to exploit infrastructure.
Why this is useful to you: Claude Mods and Claude Projects are underused Claude Code features worth trying for customising your own setup, rather than relying only on a CLAUDE.md file.

**Inside-Out AI: Rebuilding Airbnb Behind the Scenes and Across the Guest Experience** (2 October 2026)
swyx, Latent Space
https://www.latent.space/p/airbnb
Airbnb's CTO Ahmad Al-Dahle explains how the company became AI native by having product, design and engineering move straight to working prototypes in code instead of handing documents between teams, which he says was one of the biggest time savings. The company also uses AI to resolve roughly half of its customer support tickets, and reports that 60 percent of its code is now AI authored.
Why this is useful to you: skipping separate requirement documents in favour of working prototypes, and automating a chunk of routine customer queries, is a useful model for streamlining India Grace's own operations and customer support.

**We're going to need default hard budget caps on pretty much everything** (3 October 2026)
Simon Willison
https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/
Willison argues that as coding and personal agents make it easy to spin up services that cost money, hard budget caps, not just warning emails, need to become the default so a runaway agent cannot rack up a surprise bill overnight. He notes that AWS and Google Cloud have both recently added spend limit features, and suggests agents themselves should start warning builders away from uncapped services.
Why this is useful to you: this is a simple, concrete safeguard to apply to any automation or agent you build for India Grace or your own admin, so a bug or runaway process cannot generate an unexpected bill.

## Major news

Google DeepMind launched Gemini 4 Argon, claiming state of the art results on 13 of 19 benchmarks and up to 1 million output tokens, though access is currently limited to government users and a cybersecurity preview. https://www.latent.space/p/ainews-gemini-4-argon-gdms-answer

OpenAI used its DevDay to announce over 20 updates, including the Dots personal agent, Spaces and Sites for team collaboration, and the GPT-6.1 Sol model. https://www.lennysnewsletter.com/p/openai-dev-day-2026-the-releases

## Ideas to try

Try a cheap structured classification pass on a recurring India Grace task, such as triaging customer emails or tagging Meta ad comments, instead of running every item through a full LLM call. Claire Vo's Jev experiments show this kind of classification can cost pennies for thousands of items.

Run a subscription and tool audit for yourself or for India Grace using Nate B Jones' five prompt template, asking Claude to list recurring charges, flag the ones worth cancelling, and confirm the cancellation actually went through.

Set a hard spend limit on any automation or agent you build, for example through your API provider's budget cap settings, so a bug or runaway process cannot generate a surprise bill, following Simon Willison's suggestion.

## Sources that failed

Claude Code releases: HTTP 403
