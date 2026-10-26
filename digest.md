# Digest: week of 26 October 2026

## Worth your time

### Claude Duet is beautiful. I still forgot to use it
Source: Lenny's Newsletter
Date: 2026-10-21
Link: https://www.lennysnewsletter.com/p/claude-duet-is-beautiful-i-still

Claire Vo reviews Claude Duet, Anthropic's new phone based personal agent built for small business owners and busy professionals, testing it on her inbox, Slack, a sales pipeline, a Google Docs sales deck and a launch video. She finds the onboarding, task lists and artifacts genuinely polished, but says it stalls on real tasks, isn't proactive enough and lacks a desktop app, so it hasn't made her regular working stack yet.
Why this is useful to you: Claude Duet is the closest thing Anthropic has shipped to the personal life and admin agent you are trying to build toward, and this review gives an honest list of what already works and what still needs a human workaround.

### Donating Agent Skills to the Agentic AI Foundation
Source: Anthropic news
Date: 2026-10-22
Link: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation

Anthropic is handing over the Agent Skills standard, the format it created for Claude Code so an agent can carry a folder of task specific instructions and scripts, to a new vendor neutral foundation under the Linux Foundation. More than 70 platforms, including ChatGPT, Cursor, GitHub Copilot and VS Code, now support the format, with around 1 million skills published and 280 million installs since it launched in December 2025.
Why this is useful to you: this is the exact skills system you are learning to build with Claude Code, and the fact that it now works across most major AI tools means a skill you write once for your own workflows or for India Grace should keep working wherever you use it next.

### "Claude cuts my TikTok": How this creator is scaling video with AI | Brooke Lacey
Source: Lenny's Newsletter
Date: 2026-10-19
Link: https://www.lennysnewsletter.com/p/claude-cuts-my-tiktok-how-this-creator

Creator Brooke Lacey walks through the Claude Code, FFmpeg and Whisper workflow she uses to turn a raw phone video into a finished TikTok in about 15 seconds, including how she taught Claude her specific jump cut style and how she mines her own comments for new video scripts. She runs her entire weekly short form video operation this way with no editor.
Why this is useful to you: it is a concrete, reusable example of teaching Claude Code a repeatable creative or admin task by showing it your style once, a pattern you could adapt for India Grace content editing or your own personal admin automation.

### A LiteLLM release carried credential-stealing malware this week. If you've pasted an AI key into any app, the prompt guide to check what it can reach and shut it off.
Source: Nate B Jones
Date: 2026-10-24
Link: https://natesnewsletter.substack.com/p/ai-agents-cybersecurity

Nate Jones covers a week of major security incidents, including a LiteLLM release that shipped credential stealing malware, and explains why AI service keys are now valuable theft targets since a stolen key lets an attacker run paid AI work on someone else's account. He offers two prompts readers can run themselves to check what their existing AI keys and connectors can reach, plus a list of accounts and devices to review first.
Why this is useful to you: as you connect more tools, skills and accounts to Claude, this is a direct way to check what your own keys and connectors could expose if one of them were compromised.

### 30 Months on the Exponential (in Charts)
Source: Ethan Mollick, One Useful Thing
Date: 2026-10-20
Link: https://www.oneusefulthing.org/p/30-months-on-the-exponential-in-charts

To mark the release of his new book, Mollick charts how far AI has progressed since early 2024, noting that 180 models are now more capable than the original GPT-4 and that the length of task AI can reliably complete has grown enormously. He made the charts themselves by delegating the whole process, research, graphing, layout and citations, to an orchestrator agent in Claude Projects, giving it only a few sentences of direction and picking from the options it generated.
Why this is useful to you: the orchestrator pattern he describes, one agent coordinating several sub agents on a complex task from loose instructions, is worth trying for multi step India Grace work like compiling a finance or stock report, rather than working through it step by step yourself.

### Choose an Audience for Each Ad Creative
Source: Jon Loomer (Meta ads)
Date: 2026-10-20
Link: https://www.jonloomer.com/choose-an-audience-for-each-ad-creative/

Meta is rolling out a feature letting advertisers set an age and gender audience for each individual ad creative within a single ad set, rather than creating separate ad sets per age group. Loomer walks through turning it on for both the newer multimedia and older single media ad creation flows, and notes it is a soft targeting suggestion rather than a hard restriction.
Why this is useful to you: this could simplify how you structure India Grace's Meta campaigns, letting you test creative aimed at different age groups inside one ad set instead of splitting budget and learning phase across several.

### Battle Drones - a vibe coded RTS with audio-based multiplayer
Source: Simon Willison
Date: 2026-10-20
Link: https://simonwillison.net/2026/Oct/20/battledrones/

Willison describes building a full real time strategy game almost entirely by vibe coding, giving Claude loose instructions like "make it a lot more fun" and reviewing almost none of the generated code himself, across more than 300 commits mostly written by Claude Code. The result includes multiple game modes, a random map generator and multiplayer between two phones that sync over audio.
Why this is useful to you: it is a vivid example of how far you can delegate a build to Claude Code with loose, iterative feedback rather than detailed specs, a useful contrast to keep in mind when deciding how much direction to give versus how much to hand off on your own projects.

### Writing Is Closer to Thought Than Code
Source: Daniel Miessler
Date: 2026-10-23
Link: https://danielmiessler.com/blog/writing-is-closer-to-thought-than-code?utm_source=rss&utm_medium=feed&utm_campaign=website

Responding to a debate with developer Matt Pocock, Miessler argues that when building with AI the most important artifact is not the code but a clear written articulation of what you actually want, since AI has become extraordinary at execution while most failures now come from a gap between what was asked and what was meant. He frames this as a communication problem rather than a technical one, with the real iteration loop happening in refining your intent in writing, not in reworking the output.
Why this is useful to you: a useful reminder for any Claude Code or automation project that time spent clearly writing out what you want before you start is usually the highest leverage step.

## Major news

- A critical PHP vulnerability and a Node.js flaw triggered a global scramble this week, with Microsoft reporting a Chinese state aligned group using swarms of AI agents to breach cloud accounts at scale: https://www.exponentialview.co/p/the-internets-wuhan-moment
- Meta released Muse Wonder, a new frontier model aimed at agentic tasks: https://www.lennysnewsletter.com/p/how-i-ai-meta-muse-wonder-how-brooke
- Anthropic says new defenses have cut the data harvested by distillation attacks on Claude by around 90 to 99 percent: https://www.anthropic.com/news/distillation-defenses

## Ideas to try

- Test the new Choose an Audience for Each Ad Creative setting on India Grace's next Sales campaign, serving different age or gender creative from inside one ad set instead of splitting into separate ad sets, and compare delivery and cost efficiency after a week.
- Run the two exposure check prompts from Nate Jones's piece against your own Claude and API keys, connectors and automations this week, given the LiteLLM credential theft incident, so you know exactly what each one can reach.
- Try setting up an orchestrator style agent, one agent in Claude Projects directing several sub agents, for a multi step India Grace task such as pulling together a cash flow or stock report, instead of working through each step yourself in chat.

## Sources that failed

- swyx, Latent Space: ProxyError: HTTPSConnectionPool(host='latent.space', port=443): Max retries exceeded with url: /feed (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: 403 Forbidden')))
- Claude Code releases: HTTP 403
