# Digest: week of 12 October 2026

## Worth your time

### A new feature for my blog, built using my voice
Source: Simon Willison
Date: 2026-10-09
Link: https://simonwillison.net/2026/Oct/9/built-using-my-voice/

Simon built a whole new page for his blog, including a database model, imports and templates, almost entirely by talking to an AI coding assistant out loud while he cooked dinner, using the voice mode in a coding tool connected to his local project. He describes starting a dev server first so he could see progress visually, then talking through requirements in plain, unpolished speech, with the model asking clarifying questions and writing the code as they went.
Why this is useful to you: a concrete pattern for driving Claude Code hands free during dead time, worth trying for small, well scoped tasks before you commit to typing out a full spec.

### How I AI: Jev for beginners, plus Opus 5.5 vs GPT-6 Sol
Source: Lenny's Newsletter
Date: 2026-09-28
Link: https://www.lennysnewsletter.com/p/how-i-ai-jev-for-beginners-i-left

Claire walks through using a cheap "decision model" called Jev to do large batches of classification work that would be too expensive with a full language model: sorting 1,700 pull requests, triaging email, searching thousands of YouTube comments and running 200,000 classifications for about four dollars. She pairs it with a frontier model, using Jev to filter and route, then sending only the important results on for deeper reasoning.
Why this is useful to you: the same pattern (cheap classification step, then a stronger model only where needed) is a useful way to think about triaging your own inbox or admin tasks before building a fuller agent for them.

### Claude Haiku 5.5
Source: Simon Willison
Date: 2026-10-07
Link: https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/

Anthropic released a faster, cheaper Haiku model, now priced the same as OpenAI's comparable budget model up to 100,000 tokens, though with a less generous tokenizer that can offset some of the saving. Anthropic also halved the price of cache reads for Sonnet 5.5 and added monthly API credits for Max and Team subscribers that can be claimed in Settings, Billing.
Why this is useful to you: if you're on a Max or Team Claude plan, check Settings, Billing for your new API credit, and Haiku 5.5 is worth testing for any lighter weight tasks in your own automations where Opus or Sonnet is overkill.

### Does your work cost less on Opus 5.5? A 3-prompt guide
Source: Nate B Jones
Date: 2026-09-30
Link: https://natesnewsletter.substack.com/p/claude-opus-5-5-review

Nate argues the real value of a cheaper, more capable model isn't the price cut itself but "model ergonomics": how easily you can direct it, judge its output and correct it without losing earlier decisions. He offers three prompts you can rerun against your own recurring work each time a new model ships, to test whether it's actually worth moving that task over.
Why this is useful to you: a simple habit to borrow for deciding when to move a recurring India Grace or personal task (like a finance report or ad copy draft) onto a new model, rather than switching on hype alone.

### The fundamental principles of creating Meta ads
Source: Jon Loomer (Meta ads)
Date: 2026-09-29
Link: https://www.jonloomer.com/fundamental-principles-creating-meta-ads/

Jon Loomer sets out a checklist for ad creation rather than a one size fits all template: use multiple ad formats rather than relying on video alone, use Advantage+ Placements so Meta can show the right version in the right spot, and provide the correct aspect ratio for each placement (square or 4x5 for feeds, 9x16 for reels and stories) rather than one size for everything.
Why this is useful to you: a direct checklist to run India Grace's current Meta ad sets against, especially on formats and placement specific aspect ratios, which are easy to get wrong.

### How I AI: 8 real Jev use cases
Source: Lenny's Newsletter
Date: 2026-10-05
Link: https://www.lennysnewsletter.com/p/how-i-ai-8-real-jev-use-cases-how

John Lindquist demonstrates eight small applications of the same cheap decision model covered above, including a voice assistant, routing a single natural language instruction to the right tool or function, and a chess move analyser that is faster and cheaper than a reasoning model with no loss of accuracy. His core advice is to think of it like an if/else statement rather than a chatbot: wherever your workflow has a branching decision, this kind of model can often make that call near instantly and almost for free.
Why this is useful to you: the "routing" pattern, one small model deciding which tool or path to use, is a useful building block for any personal admin agent you build, for example one that sorts incoming tasks or emails before acting on them.

### Agents split your software into three parts, which should you keep paying for
Source: Nate B Jones
Date: 2026-10-04
Link: https://natesnewsletter.substack.com/p/ai-agents-software-buying

Nate's framing is that any software subscription bundles three things: the underlying data, the interface, and the workflows that turn information into action, and agents are starting to pull these apart, since an agent can act on data in a tool without you ever touching that tool's screens. He suggests deciding which of the three you actually need to keep paying for, versus what you could build or automate yourself.
Why this is useful to you: a useful lens for India Grace's own software spend (stock, ads or finance tools), to ask which parts of a subscription you're really using versus what an agent could increasingly do for you directly.

### What's changed in how agents use computers
Source: swyx, Latent Space
Date: 2026-09-30
Link: https://www.latent.space/p/devday-2026

A podcast conversation on how "computer use" agents (ones that operate software directly rather than through an API) have improved sharply in recent months, now combining screenshots with accessibility data and the page's underlying structure to work faster and recover better from mistakes. The discussion also covers newer techniques like letting an agent keep reasoning while a tool call is still running, and the trust and permission questions that come with letting an agent make payments or operate a website on your behalf.
Why this is useful to you: useful background if you're thinking about building or using an agent that operates applications on your behalf for personal admin, including what guardrails to expect to need around payments and permissions.

## Major news

- Google's Gemini 4 Argon rolled out, and OpenAI pulled a planned GPT-6.1 Astra model over alignment failures, shipping the lower cost GPT-6.1 Sol instead: https://thezvi.substack.com/p/ai-188-gemini-dot-argon
- OpenAI published 722 manuscripts from an internal model solving 90 of the top 500 open problems in mathematics, described by some mathematicians as the most significant moment in the field's history: https://thezvi.substack.com/p/new-math-from-openai
- Anthropic launched the Cyber Mission, a long term effort to help secure critical infrastructure and open source software with free security scans and engineering support: https://www.anthropic.com/news/anthropic-cyber-mission
- Anthropic updated its 2026 Usage Policy, adding clearer rules on deceptive campaigns, elections and autonomous physical actions, effective 12 November: https://www.anthropic.com/news/2026-usage-policy-update

## Ideas to try

- Run India Grace's current Meta ad sets against Jon Loomer's checklist: check you're using more than one ad format, that Advantage+ Placements is switched on, and that each placement has the right aspect ratio rather than one size stretched everywhere.
- Try the cheap classification plus frontier model pattern from the Jev pieces on a real admin task, for example sorting a backlog of emails or India Grace stock or finance records into categories cheaply before deciding what actually needs your attention.
- Next time a new Claude model ships, use Nate B Jones's three prompt test on one recurring task of yours (like a cash flow report or an ad copy draft) before moving it over, rather than switching on hype alone.

## Sources that failed

- Claude Code releases (https://github.com/anthropics/claude-code/releases.atom): HTTP 403
