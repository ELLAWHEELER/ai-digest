# Digest: week of 2 November 2026

## Worth your time

### Five controls to set before you let an AI agent buy, pay, or cancel anything for you, so it finishes the job without spending money you didn't approve.
Source: Nate B Jones
Date: 2026-10-31
Link: https://natesnewsletter.substack.com/p/ai-agents-website-access

Nate Jones looks at what happens when you let an AI agent complete real world tasks like booking a hotel or buying something, and how new trust systems from Cloudflare, Google, Stripe, Visa and Meta are shaping which agents websites will actually let in. He lays out five specific controls to put in place before handing an agent a first real task: narrow its access, require approval at specific points, and check where the result actually lands.
Why this is useful to you: This is directly about the kind of personal agent you are building toward for your own life and admin, and gives a concrete checklist to use the first time you let one of your own agents spend money or book something on your behalf.

### The October inflection point for vibe game development
Source: Simon Willison
Date: 2026-10-28
Link: https://simonwillison.net/2026/Oct/28/vibe-game-development/

Simon Willison argues that October 2026 was the moment vibe coding games with AI crossed a real threshold, driven mainly by Claude Opus 5.5's jump in 3D modelling, music generation and game design judgement. He walks through browser based games he built with single prompts and almost no iteration, including one made entirely in the regular Claude chat interface without Claude Code.
Why this is useful to you: It is a clear, low effort example of what Claude Opus 5.5 can now build unsupervised from a single good prompt, a useful benchmark for how far you can push "ask Claude to just build it" style requests in your own Claude Code experiments.

### How To Use Decision Models for Evals
Source: Hamel Husain
Date: 2026-10-20
Link: https://hamel.dev/blog/posts/decision-model-evals/

Hamel Husain tests several small decision models, fast classifiers from TypeSafe, Perplexity, Liquid, Cloudflare and OpenAI, as a cheaper alternative to using a large language model as a judge when running automated evals. He shows that the default 0.50 decision threshold these tools ship with is often wrong for a given task, and that tuning it against your own labelled examples can meaningfully improve accuracy without changing the model.
Why this is useful to you: If you build any kind of automated checking into your Claude Code skills or agents, this is a practical reminder to tune the threshold against real examples rather than trusting a tool's default settings.

### Why Reddit built its own AI prototyping tool | Blair Metcalf
Source: Lenny's Newsletter
Date: 2026-10-26
Link: https://www.lennysnewsletter.com/p/why-reddit-built-its-own-ai-prototyping

Reddit's principal UX engineer Blair Metcalf explains Reddit Proto, an internal tool that lets designers turn ideas into working prototypes using real Reddit data, without touching GitHub, by connecting Cursor to a custom design system MCP that maps Reddit's components directly to production code. The tool has reached full adoption across Reddit's product and UX teams and produced more than 700 prototypes, with non engineers often getting the best results.
Why this is useful to you: It is a working example of the pattern behind Claude Code skills and MCP connections, giving an AI tool a mapped out reference to your own system so it builds things that actually fit, worth copying in miniature for your own automations or for India Grace's reporting formats.

### You delegated the work to agents and ended up with a new job: reading their updates. My guide to a Chief of Staff that brings you decisions with the evidence.
Source: Nate B Jones
Date: 2026-10-27
Link: https://natesnewsletter.substack.com/p/ai-agent-overload

Nate Jones describes a common failure mode once you start delegating tasks to multiple AI agents: the updates they send back pile up into a new job of reading and triaging them yourself. His fix is a Chief of Staff layer that closes out finished threads without spinning off new work, stays quiet unless something actually changed, and brings you a recommendation with the evidence rather than a raw list.
Why this is useful to you: This is a direct answer to a problem you will likely hit as you build more agents for your own admin, worth building in from the start rather than retrofitting once your inbox of agent updates gets noisy.

### Grok vs. Dot vs. Muse vs. Claude Duet: which one crushes the competition?
Source: Lenny's Newsletter
Date: 2026-10-28
Link: https://www.lennysnewsletter.com/p/grok-vs-dot-vs-muse-vs-claude-duet

Claire Vo ran the same nine real tasks, including a Slack reply, a Sentry bug fix, inbox triage and a Figma thumbnail, across four personal agents: Grok Bot, ChatGPT's Dot, Meta's Muse and Claude Duet, scoring each live. She comes away with a scoreboard and a clear view of which agent she would trust for work tasks versus personal ones.
Why this is useful to you: It is a ready made comparison of the exact category of personal agent you are trying to build toward, useful for deciding which one to actually trial on your own admin tasks before building something custom.

### Meta Clarifies Upcoming Placement Control Changes
Source: Jon Loomer (Meta ads)
Date: 2026-10-27
Link: https://www.jonloomer.com/meta-placement-control-changes/

Jon Loomer updates his earlier reporting now that Meta has officially confirmed it: ad set level placement control is being removed for Sales, Leads, App Promotion and Engagement campaign objectives, a wider set than he originally expected. Meta's suggested workarounds, customising creative per placement and using placement value rules to adjust bids, only partly make up for losing the ability to simply switch placements off.
Why this is useful to you: This is a direct, imminent change to how India Grace's Meta campaigns can be configured, worth checking your active campaign objectives against this list now and testing placement value rules before the change lands.

### How a 19-year-old intern built the growth engine behind this $2B AI company | Hector Serrano
Source: Lenny's Newsletter
Date: 2026-11-01
Link: https://www.lennysnewsletter.com/p/how-a-19-year-old-intern-built-the

Hector Serrano explains how he built Wispr Flow's paid user generated content program, paying a roster of 50 creators to produce 500 to 600 UGC ads a month, with top earners making over $13,000 a month, as part of a strategy that helped the company grow revenue 30x. He argues paid UGC, long used by direct to consumer brands, is still an underused growth lever for other companies willing to run it properly.
Why this is useful to you: It is a concrete, adaptable playbook for a paid UGC creator program that India Grace could test at a much smaller scale alongside its existing Meta ads work.

## Major news

- Google released Gemini 4 Argon, a notably stronger model with a lengthy new safety card, though a detailed read suggests it mostly confirms known risk patterns rather than raising new alarms: https://thezvi.substack.com/p/gemini-4-argon-the-model-and-safety
- Anthropic filed its S-1 with the SEC, formally starting the process toward a Nasdaq listing under the ticker ANT: https://www.anthropic.com/news/s1-sec
- New interpretability research from Goodfire suggests the inside of language models may be more understandable than assumed, a step that could make it easier to catch AI mistakes before they cause harm: https://thezvi.substack.com/p/i-can-see-everything
- Microsoft offered a voluntary exit to around 60,000 employees, about 27 percent of its workforce, as AI infrastructure spending reshapes how big tech staffs itself: https://www.exponentialview.co/p/microsoft-is-making-room-for-machines

## Ideas to try

- Before letting any personal agent (Claude Duet or otherwise) make a purchase or booking for you, set up Nate Jones's five controls on one low stakes task first, such as narrowing what it can access and requiring approval at a specific step, rather than giving it open ended access from the start.
- Build a small reference file for India Grace, similar in spirit to Reddit's design system MCP, that captures brand colours, product terminology and your standard report formats, so any Claude Code skill you build for content or reporting already knows how India Grace looks and talks.
- Check India Grace's active Meta campaign objectives against Jon Loomer's list (Sales, Leads, App Promotion, Engagement) now, since ad set level placement control is being removed for all of them, and test placement value rules as the workaround before the change lands.

## Sources that failed

- swyx, Latent Space: ProxyError (unable to connect to proxy while fetching the feed)
- Claude Code releases: HTTP 403
