# AI practitioner digest

This project fetches new posts from a fixed list of AI practitioners and turns them into a weekly digest for Ella.

## Who this is for
Ella is completing an MBA and is learning to build AI systems. She helps run her sister's fashion brand, India Grace London, and wants this digest to help her spot ideas from AI practitioners she can apply to India Grace (finance/cash flow reporting, Meta ads, stock, operations), to her own AI-building practice (Claude Code, skills, memory, automation), and to building agents that manage her own personal life and admin more efficiently.

## Files
- fetch_digest.py fetches raw posts into digest_data.json (title, date, url, summary, full_text per item, grouped by source, plus a failed list)
- captured_urls.json is every URL ever included in a past digest, checked to avoid repeats
- digest.md is the most recent written digest

## Digest rules
- Group items by author/source
- First skip anything already in captured_urls.json
- Then cap at 3 items per author maximum from what remains, keeping the most recent by date if there are more
- Each item: title, date, link, a 2-3 sentence plain language summary based on its full_text field (the actual article content, up to about 3000 characters), not the short feed summary. Only say a summary isn't available if full_text is also missing, or is clearly not real content (a paywall notice, a cut-off teaser, boilerplate). Never invent content
- Add a section titled "Ideas to try" with at most 3 concrete suggestions, tied specifically to India Grace or to Ella's own Claude Code / automation building, drawn from that week's actual items, not generic advice
- Add a section titled "Sources that failed" listing anything in digest_data.json's failed list
- Section titles use a colon, e.g. "Digest: week of 28 September 2026" using the most recent Monday as the week start
- No em dashes, no emojis, no bold text inside sentences (headers can be bold). This applies only to text the digest writes itself: summaries, section headers, and ideas to try
- Post titles are copied exactly as published, unchanged, even if they contain an emoji or a dash. A title is a quoted fact, not the digest's own writing
- Only after the digest has been delivered successfully (email sent, or Gmail draft created), add every URL that appears in digest.md to captured_urls.json so it's never repeated. If delivery fails, leave captured_urls.json unchanged so those items are included in the next run
