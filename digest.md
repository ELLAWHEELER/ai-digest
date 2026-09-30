# Digest: week of 21 September 2026

Covers posts from 18 to 26 September 2026 (8 day window). No new posts this week from Dwarkesh Patel, Benedict Evans, Andrej Karpathy or Anthropic engineering.

## Source: Ethan Mollick, One Useful Thing

### The Overhang
18 September 2026 | [Read the post](https://www.oneusefulthing.org/p/the-overhang)

Mollick argues that while everyone debates future AI, today's models are already capable of weeks of human work and are barely being used. His examples: GPT-6 Astra turned the 1977 text game Zork into a playable 3D game, and Fable 5.1 rebuilt Umberto Eco's library in 3D from videos and photos. He also gave GPT-6 Astra his upcoming book and it produced an animated trailer in Blender, with a script and music, without being told how.

## Source: Zvi Mowshowitz

### On Ezra Klein’s Podcast With Jensen Huang
25 September 2026 | [Read the post](https://thezvi.substack.com/p/on-ezra-kleins-podcast-with-jensen)

Zvi's commentary on Nvidia CEO Jensen Huang's interview with Ezra Klein. Zvi's reading is that Huang sees AI as just another software product, so by his own logic any lab that can't test its models safely should be shut down, which is a stricter line than most safety advocates take. Zvi says this matters because Huang has real influence over chip supply and American AI policy.

### AI #187: Coming Into Play
24 September 2026 | [Read the post](https://thezvi.substack.com/p/ai-187-coming-into-play)

Zvi's weekly roundup, led by the release of Claude Opus 5.5 (reported to be excellent) and OpenAI's cheaper new GPT-6 Sol and Luna models. It also notes that Bernie Sanders and Greg Casar have introduced a Ban Artificial Superintelligence Act. The rest covers a long list of topics, from AI agents and hacking incidents to Anthropic's new biology lab.

### Claude Opus 5.5: The System Card
23 September 2026 | [Read the post](https://thezvi.substack.com/p/claude-opus-55-the-system-card)

Zvi reads through the system card (Anthropic's safety and capability report) for Claude Opus 5.5, which Anthropic says matches or beats Fable 5.1 while costing less than Opus 5. He walks through the safety classifiers and risk tests, which put Opus 5.5 at the same risk level as Fable 5.1. He also flags a notable policy change: Anthropic no longer tests special "helpful only" versions of Claude.

## Source: Azeem Azhar, Exponential View

### 🔮 Safety in numbness
26 September 2026 | [Read the post](https://www.exponentialview.co/p/safety-in-numbness)

Azeem uses Erik Hoel's argument that creative writing degrees have flattened literary fiction, by sanding away anything odd through repeated peer critique, as a warning about AI. His worry is that LLMs could do the same to other fields, pushing everyone's work toward a safe, homogenised middle. His point is that standardisation should help people reach further, not make everyone sound alike.

### 🤖 Your agent, whose interests?
25 September 2026 | [Read the post](https://www.exponentialview.co/p/meta-muse-digital-butler)

Meta's Muse, an AI agent that gets tasks done for you (one user got $250 of flight delay compensation in five minutes), quickly became the top free iPhone app in the US. Meta plans to profit by taking a small fee from transactions. Azeem notes that Shopify, home to the long tail of niche brands, is a partner, while Amazon has blocked Muse because "agents don't window-shop" and that threatens its advertising income.

### 📈 Monday data: More AI numbers, more clarity?
21 September 2026 | [Read the post](https://www.exponentialview.co/p/monday-data-ai-investment-brief)

An extract from Exponential View's new AI Investment Brief, analysing what large US companies say about AI on earnings calls. A third of S&P 500 companies now put a number on their AI use, but only 15% quantify its impact on the business, up from 9%. Where they do, the average claimed boost is 47% for cost or productivity and 40% for revenue, though the spread is wide.

## Source: swyx, Latent Space

### OpenRouter: from Seed to Stripe — with OpenRouter’s Alex Atallah & AMP’s Anjney Midha
25 September 2026 | [Read the post](https://www.latent.space/p/openrouter)

A podcast with OpenRouter's CEO on how a service dismissed as "just a wrapper" became a routing layer used by over 10 million developers to reach many AI models through one account, now handling more than 10 trillion tokens a day. It covers why they bet early that no single model would win and why they stayed focused rather than adding products. It also explains why Stripe bought them: fraud, including attacks by autonomous agents, is becoming a major problem for AI services.

### [AINews] The Future of Latent Space
25 September 2026 | [Read the post](https://www.latent.space/p/ainews-the-future-of-latent-space)

swyx announces changes to Latent Space: merging its newsletter with its Discord community, a possible move to Beehiiv and a new homepage, and reopening for sponsorships. The news section that follows covers the week's model releases. One practical detail: on one test, Opus 5.5 scores 24% at low effort and 62% at xhigh, but drops to 59% at max, so one engineer recommends avoiding "max".

### Runway’s WorldPrompt and the Engineering of Real-Time Worlds
25 September 2026 | [Read the post](https://www.latent.space/p/runway)

Runway's GWM Worlds 2 generates interactive video and audio in real time, a bit like a video game that is invented as you play. Its new WorldPrompt feature lets you fix parts of the world, such as the first frame, and then schedule events and character actions, including live. Unlike games such as Minecraft it can be prompted but not programmed, and all of these real-time world models still only run for minutes at a time.

## Source: Simon Willison

### Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war
22 September 2026 | [Read the post](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/)

Anthropic released Claude Opus 5.5 and OpenAI released GPT-6 Sol and GPT-6 Luna within about an hour of each other, and prices fell sharply. The GPT-6 models are half the price of the models they replace, and Opus 5.5 is 20% cheaper than earlier Opus models ($4 per million input tokens, $20 output), with cached input 60% cheaper, which matters for long agent sessions. Simon also notes Opus 5.5 is meant to fix complaints about how Opus writes.

### Jev introduces a new shape of LLM - System One, aka Decision Models
21 September 2026 | [Read the post](https://simonwillison.net/2026/Sep/21/jev/)

Jev is a new kind of model: you give it text and ask questions, and instead of writing an answer it returns numbers, such as how likely a statement is to be true, which option fits best, or a score on a scale. It is fast, very cheap, and suited to classification jobs like spam detection, labelling, prioritisation and ranking search results. Its own documentation says it is weak with numbers and dates, and Simon is uneasy that it works as a black box.

## Source: Daniel Miessler

### How Jev Picks the Model and Effort for Every Prompt
25 September 2026 | [Read the post](https://danielmiessler.com/blog/glance-routes-model-and-effort?utm_source=rss&utm_medium=feed&utm_campaign=website)

Miessler's personal AI system, LifeOS, now uses Jev to decide for each prompt which model should handle it and how much effort it needs, in a third of a second. It agreed with a panel of three top models 90% of the time, against 75% for Opus 5.5 alone. Before any automated decision is trusted, it runs in "shadow" mode: it only advises, its answers are logged against what actually happened, and it gets permission to act only once its track record is recorded.

### Two Upgrades to My AI Stack: Vigil and Idea-to-Video
24 September 2026 | [Read the post](https://danielmiessler.com/blog/vigil-and-idea-to-video?utm_source=rss&utm_medium=feed&utm_campaign=website)

Miessler added Vigil, where every part of his AI system reports what it is doing to one central database, and a check every 10 minutes texts him anything he needs to know. He can also now turn a spoken idea into a finished, published YouTube video with no manual editing. He stresses that the words are entirely his own and only the voice is AI generated.

### Attacker vs. Defender AI Advantage
22 September 2026 | [Read the post](https://danielmiessler.com/blog/attacker-defender-ai-advantage?utm_source=rss&utm_medium=feed&utm_campaign=website)

A short argument that AI will favour attackers over defenders in cyber security, not because of the technology but because defenders are slowed by bureaucracy and process. Attackers can adopt a new technique in minutes or hours, while most companies take weeks or months. AI makes that existing gap starker.

## Source: The Rundown

### Meta's Connect turns into a Muse takeover
25 September 2026 | [Read the post](https://www.therundown.ai/articles/meta-connect-turns-into-a-muse-takeover)

At its Connect event Meta announced upgrades to its Muse agent, including Charm, a keychain device for talking to Muse that ships in December, and Muse on its AI glasses within months. PayPal, Walmart, Shopify, GitHub and Box have joined as partners, after Amazon blocked access. The issue also has an item on using Gemini Canvas to visualise Google Sheets.

### Anthropic's AI biology lab makes its first find
24 September 2026 | [Read the post](https://www.therundown.ai/articles/anthropic-ai-biology-lab-makes-its-first-find)

Anthropic's new biology lab ran around 950 Claude agents for less than a day and found a never-before-seen DNA system in viruses that infect bacteria, with repeats that look like CRISPR. Dario Amodei said the work was mostly Claude's and that the system might be a new kind of gene editor, though its function is not yet known. The issue also reports that Claude now leads 26% of Anthropic's AI research.

### The pacing era's first launch day
23 September 2026 | [Read the post](https://www.therundown.ai/articles/the-pacing-era-s-first-launch-day)

Anthropic and OpenAI released models 90 minutes apart: Claude Opus 5.5 took the top spot on a major intelligence index at a lower price than Fable 5.1, and GPT-6 Sol and Luna cut prices in half. Anthropic also says Opus 5.5 avoids jargon and follows users' own style rules more closely. The issue also covers OpenAI's claim that an internal model has solved over 100 open maths problems.

## Source: Dario Amodei essays

### We Must Pace the Frontier
September 2026 | [Read the post](https://darioamodei.com/post/we-must-pace-the-frontier)

Anthropic's CEO argues that AI companies must deliberately slow how fast AI capabilities improve so that safety work can keep up. His first reason is that since this summer AI has sped up sharply because it is increasingly building the next generation of AI itself (recursive self-improvement). His second is the OpenAI and Hugging Face incident involving a swarm of agents, though the extract cuts off before he describes it.

## Source: Anthropic news

### Claude discovers a novel enzyme system with CRISPR-like repeats
23 September 2026 | [Read the post](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)

Anthropic has launched a life sciences research group with its own lab, where Claude agents search DNA datasets, generate hypotheses and propose experiments. In early results Claude found a new enzyme system with repeating DNA like CRISPR, and features that have only been seen before in systems that cut, copy and paste DNA. Its function is not yet known.

### Partnering with Accenture on embedded evaluation
18 September 2026 | [Read the post](https://www.anthropic.com/news/accenture-embedded-evaluation)

Anthropic is partnering with Accenture, through its AI business Faculty, to have independent evaluators work inside Anthropic with access similar to an employee's, testing models and checking that safety commitments are kept. Each company expects to invest at least $1 billion in this over five years. The deal is non-exclusive, and Anthropic says the safety of its models remains its own responsibility.

## Ideas to try

1. Run your next automation in shadow mode first. Miessler's LifeOS lets a new automated decision only advise at first, logs its answer next to what actually happened, and lets it act only once its agreement rate is recorded. Apply this to your personal admin agent or an India Grace inbox sorter: for two weeks, have it write down what it would do (file, reply, flag as urgent) without doing it, then check how often it matched your own choice before you let it act.

2. Check how India Grace looks to shopping agents. Exponential View and The Rundown both report that Shopify is a Muse partner and that Meta will take a small fee on transactions, while Azeem notes that "agents don't window-shop". If India Grace sells through Shopify, review whether its product listings answer an agent's questions in plain text (fabric, sizing, fit, delivery times and returns), and keep an eye on whether Meta offers Muse as a sales channel alongside your Meta ads.

3. Stop defaulting to maximum effort in your Claude Code builds. Latent Space reports Opus 5.5 scoring 62% at xhigh effort but slightly lower at max on one test, and Miessler's system chooses the model and the effort level separately for each task. For your own skills and agents, try high or xhigh rather than max, and give simple steps like renaming, tagging or extracting to a cheaper model, using Simon's price table as a guide.

## Sources that failed

None this week. All 13 sources were fetched successfully.
