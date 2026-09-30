# AI practitioner digest

This project fetches new posts from a fixed list of AI practitioners and turns them into a weekly digest for Ella.

## Who this is for
Ella is completing an MBA and is learning to build AI systems. She helps run her sister's fashion brand, India Grace London, and wants this digest to help her spot ideas from AI practitioners she can apply to India Grace (finance/cash flow reporting, Meta ads, stock, operations), to her own AI-building practice (Claude Code, skills, memory, automation), and to building agents that manage her own personal life and admin more efficiently.

## Files
- fetch_digest.py fetches raw posts into digest_data.json (title, date, url, summary, full_text per item, grouped by source, plus a failed list)
- captured_urls.json is every URL ever included in a past digest, checked to avoid repeats
- digest.md is the most recent written digest

## What the digest is for
The main goal is upskilling: helping Ella use AI better in her work and life, for productivity and better outputs, and keep learning what is new. A small amount of major news is useful for grounding, but business news is not the focus.

Rank items by relevance to that goal, judged from their full_text:
- Most relevant: practical techniques and workflows; how practitioners actually use and build with AI (Claude Code, agents, skills, memory, automation); what new models or tools let her do differently; anything she could apply to India Grace (finance/cash flow, Meta ads, stock, operations) or to agents for her personal admin
- Least relevant: funding, acquisitions, IPOs, company business news, politics and policy debates, and science or industry news with no bearing on how she works

## Digest rules
- First skip anything already in captured_urls.json
- Choose in two passes to keep token use down. Pass 1: for every remaining item, look only at the title, source and the first 500 characters of full_text, and shortlist the 15-20 most promising (including any candidates for "Major news"). Pass 2: read the full full_text only for shortlisted items, then rank and write. Do not print or read the full text of items that were not shortlisted
- Main section, titled "Worth your time": the most relevant remaining items, ordered by relevance (most relevant first), not by date or source. At most 8 items in total and at most 3 from any one source. A source can contribute nothing if none of its items are relevant enough
- Each main item: title, source, date, link, a 2-3 sentence plain language summary based on its full_text field (the actual article content, up to about 3000 characters), not the short feed summary, then one line starting "Why this is useful to you:" linking it to Ella's work or skills. Only say a summary isn't available if full_text is also missing, or is clearly not real content (a paywall notice, a cut-off teaser, boilerplate). Never invent content
- Claude Code releases: combine all new releases into a single "Worth your time" item titled "What's new in Claude Code", ranked like any other item. Summarise the changes that matter for how Ella works rather than listing every fix, and list each release's link so they are all captured. It counts as one item
- Section titled "Major news": at most 5 one-line items for grounding (major model releases, significant industry or safety events), each with its link. Only include genuinely major news, not items that just failed to make the main section. Do not repeat anything already in "Worth your time"
- Items not chosen for either section are left out and not added to captured_urls.json, so they can be considered again next week while still inside the fetch window
- Add a section titled "Ideas to try" with at most 3 concrete suggestions, tied specifically to India Grace or to Ella's own Claude Code / automation building, drawn from that week's actual items, not generic advice
- Add a section titled "Sources that failed" listing anything in digest_data.json's failed list
- Section titles use a colon, e.g. "Digest: week of 28 September 2026" using the most recent Monday as the week start
- No em dashes, no emojis, no bold text inside sentences (headers can be bold). This applies only to text the digest writes itself: summaries, section headers, and ideas to try
- Post titles are copied exactly as published, unchanged, even if they contain an emoji or a dash. A title is a quoted fact, not the digest's own writing
- Only after the digest has been delivered successfully (email sent, or Gmail draft created), add every URL that appears in digest.md to captured_urls.json so it's never repeated. If delivery fails, leave captured_urls.json unchanged so those items are included in the next run
