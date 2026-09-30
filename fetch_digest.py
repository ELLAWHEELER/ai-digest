"""
fetch_digest.py

Fetches recent posts from a fixed list of AI practitioner sources and writes
them to digest_data.json, ready to be turned into a weekly digest.

Usage:
    python fetch_digest.py            # last 14 days (the default)
    python fetch_digest.py --days 30  # last 30 days

The digest runs weekly but looks back 14 days, so if one week's run fails,
the next run still picks up those posts. Posts already sent in an earlier
digest are skipped using captured_urls.json, so the overlap causes no repeats.

Needs:  pip install requests feedparser beautifulsoup4 trafilatura
"""

# --- Imports -----------------------------------------------------------------
# Standard library modules (come with Python, nothing to install).
import argparse                      # reads command-line arguments like --days
import calendar                      # used to find the last day of a month
import json                          # writes the output file
import re                            # regular expressions, for finding dates in text
import sys                           # used to make printing safe on Windows
from datetime import datetime, timedelta, timezone
from pathlib import Path             # a tidy way to build file paths
from urllib.parse import urljoin     # turns "/news/foo" into a full URL

# Third-party libraries (installed with pip).
import feedparser                    # understands RSS and Atom feeds
import requests                      # downloads web pages
import trafilatura                   # pulls the main article text out of a page
from bs4 import BeautifulSoup        # picks apart HTML pages


# --- Settings ----------------------------------------------------------------

# Every source we check. "type" tells the script which fetcher function to use:
#   "feed"      -> an RSS or Atom feed, read with feedparser
#   "dario"     -> Dario Amodei's site, scraped with BeautifulSoup
#   "anthropic" -> an Anthropic index page, scraped with BeautifulSoup
SOURCES = [
    {"name": "Ethan Mollick, One Useful Thing", "url": "https://www.oneusefulthing.org/feed", "type": "feed"},
    {"name": "Zvi Mowshowitz", "url": "https://thezvi.substack.com/feed", "type": "feed"},
    {"name": "Dwarkesh Patel", "url": "https://www.dwarkesh.com/feed", "type": "feed"},
    {"name": "Azeem Azhar, Exponential View", "url": "https://www.exponentialview.co/feed", "type": "feed"},
    {"name": "swyx, Latent Space", "url": "https://www.latent.space/feed", "type": "feed"},
    {"name": "Simon Willison", "url": "https://simonwillison.net/atom/entries/", "type": "feed"},
    {"name": "Benedict Evans", "url": "https://www.ben-evans.com/benedictevans?format=rss", "type": "feed"},
    # The old /feed.xml address now returns 404; this is the current feed.
    {"name": "Daniel Miessler", "url": "https://danielmiessler.com/feed.rss", "type": "feed"},
    {"name": "Nate B Jones", "url": "https://natesnewsletter.substack.com/feed", "type": "feed"},
    {"name": "Lenny's Newsletter", "url": "https://www.lennysnewsletter.com/feed", "type": "feed"},
    {"name": "Jon Loomer (Meta ads)", "url": "https://www.jonloomer.com/feed/", "type": "feed"},
    {"name": "Harper Reed", "url": "https://harper.blog/index.xml", "type": "feed"},
    {"name": "Hamel Husain", "url": "https://hamel.dev/index.xml", "type": "feed"},
    # GitHub publishes each Claude Code release as an Atom feed entry.
    {"name": "Claude Code releases", "url": "https://github.com/anthropics/claude-code/releases.atom", "type": "feed"},
    {"name": "Dario Amodei essays", "url": "https://darioamodei.com/", "type": "dario"},
    {"name": "Anthropic news", "url": "https://www.anthropic.com/news", "type": "anthropic"},
    {"name": "Anthropic engineering", "url": "https://www.anthropic.com/engineering", "type": "anthropic"},
]

# Some sites (Karpathy's blog, for one) block the default "python-requests"
# identity with a 403 error, so we introduce ourselves as a normal browser.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
    )
}

# Give up on any single request after this many seconds.
TIMEOUT = 20

# How much of each article's text to keep in the "full_text" field.
FULL_TEXT_LIMIT = 3000

# The output file lives next to this script, whatever folder you run it from.
OUTPUT_FILE = Path(__file__).parent / "digest_data.json"


# --- Small helpers -----------------------------------------------------------

def download(url):
    """Download a URL and return the response.

    raise_for_status() turns a bad HTTP status (404, 403, 500...) into an
    exception, so a broken page ends up in the "failed" list rather than
    being quietly treated as an empty page.
    """
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    return response


def html_to_text(html):
    """Strip HTML tags out of a feed summary and tidy the whitespace.

    Many feeds put HTML in their summary field. This only removes the markup;
    the words are exactly what the feed provided.
    """
    if not html:
        return ""
    text = BeautifulSoup(html, "html.parser").get_text(" ")
    return " ".join(text.split())  # collapse runs of spaces and newlines


def fetch_full_text(url):
    """Download an article and return its main text, cut to FULL_TEXT_LIMIT.

    trafilatura is built for this job: it finds the article body and skips
    menus, ads, footers and comments. It returns None when it can't find an
    article, which we turn into "". Any error (a 403, a timeout...) is caught
    by the caller, so one unreadable article never loses the whole source.
    """
    html = download(url).text
    text = trafilatura.extract(html, include_comments=False, include_tables=False) or ""

    if len(text) > FULL_TEXT_LIMIT:
        # Cut at the last space before the limit so we don't split a word,
        # and add "..." so it's obvious the text continues.
        text = text[:FULL_TEXT_LIMIT].rsplit(" ", 1)[0] + "..."
    return text


def parse_day(text):
    """Turn a date like "Sep 23, 2026" or "September 23, 2026" into a date.

    Returns None if the text doesn't match either format.
    """
    for fmt in ("%b %d, %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            pass  # wrong format, try the next one
    return None


# --- Fetcher 1: RSS and Atom feeds -------------------------------------------

def fetch_feed(source, cutoff):
    """Read an RSS/Atom feed and return the items published after the cutoff."""
    # We download with requests (rather than letting feedparser do it) so we
    # get a clear status code on failure and can send our browser User-Agent.
    response = download(source["url"])
    feed = feedparser.parse(response.content)

    # "bozo" is feedparser's flag for "this didn't parse cleanly". Small
    # glitches are common and harmless, but no entries at all means we
    # probably got an error page instead of a feed.
    if feed.bozo and not feed.entries:
        raise ValueError(f"not a valid feed ({feed.bozo_exception})")

    items = []
    for entry in feed.entries:
        # feedparser gives dates as a time tuple in UTC. Some feeds only have
        # an "updated" date, so fall back to that.
        time_tuple = entry.get("published_parsed") or entry.get("updated_parsed")
        if not time_tuple:
            continue  # no date, so we can't tell if it's in the window
        published = datetime(*time_tuple[:6], tzinfo=timezone.utc)

        if published < cutoff:
            continue  # too old

        items.append({
            "title": entry.get("title", "").strip(),
            "date": published.date().isoformat(),  # e.g. "2026-09-23"
            "url": entry.get("link", ""),
            "summary": html_to_text(entry.get("summary", "")),
        })
    return items


# --- Fetcher 2: Dario Amodei's site ------------------------------------------

def fetch_dario(source, cutoff):
    """Scrape darioamodei.com for essays published after the cutoff.

    The home page lists essay links but no dates, so we open each essay and
    read its date. Dates there are month-only ("September 2026"), so an essay
    counts as recent if its month overlaps the window at all.
    """
    page = BeautifulSoup(download(source["url"]).text, "html.parser")

    # Essay links look like /essay/... or /post/...
    urls = []
    for link in page.find_all("a", href=True):
        if link["href"].startswith(("/essay/", "/post/")):
            full_url = urljoin(source["url"], link["href"])
            if full_url not in urls:  # skip duplicates
                urls.append(full_url)

    items = []
    for url in urls:
        essay = BeautifulSoup(download(url).text, "html.parser")

        # The date sits in <div class="post-date">September 2026</div>.
        date_el = essay.find(class_="post-date")
        if not date_el:
            continue
        month_start = datetime.strptime(date_el.get_text(strip=True), "%B %Y")

        # Work out the last day of that month, then skip the essay if the
        # whole month ended before our window started.
        last_day = calendar.monthrange(month_start.year, month_start.month)[1]
        month_end = month_start.replace(day=last_day).date()
        if month_end < cutoff.date():
            continue

        # The page <title> is "Dario Amodei — <essay title>", so we cut off
        # the name. The description meta tag is the site's own subtitle,
        # which we use as the summary if present.
        title = essay.title.get_text(strip=True) if essay.title else url
        if title.startswith("Dario Amodei") and "—" in title:
            title = title.split("—", 1)[1].strip()  # keep what's after the dash
        description = essay.find("meta", attrs={"name": "description"})

        items.append({
            "title": title,
            "date": month_start.strftime("%Y-%m"),  # month only, e.g. "2026-09"
            "url": url,
            "summary": description.get("content", "").strip() if description else "",
        })
    return items


# --- Fetcher 3: Anthropic news and engineering pages -------------------------

def fetch_anthropic(source, cutoff):
    """Scrape an Anthropic index page for posts published after the cutoff.

    Each post is an <a> card linking to /news/... or /engineering/..., with
    the date and title inside it.
    """
    page = BeautifulSoup(download(source["url"]).text, "html.parser")

    # "/news/" or "/engineering/", taken from the end of the source URL.
    path_prefix = "/" + source["url"].rstrip("/").split("/")[-1] + "/"

    items = []
    seen = set()
    for card in page.find_all("a", href=True):
        if not card["href"].startswith(path_prefix):
            continue
        url = urljoin(source["url"], card["href"])
        if url in seen:
            continue
        seen.add(url)

        # The date is in a <time> tag (news) or an element whose class
        # mentions "date" (engineering).
        date_el = card.find("time") or card.find(class_=re.compile("date"))
        day = parse_day(date_el.get_text()) if date_el else None

        # The "Featured" card at the top has no date on the index page, so
        # open the article and take the first date written on it.
        if day is None:
            article_text = BeautifulSoup(download(url).text, "html.parser").get_text(" ")
            match = re.search(r"[A-Z][a-z]{2,8} \d{1,2}, \d{4}", article_text)
            day = parse_day(match.group()) if match else None
        if day is None or day < cutoff.date():
            continue  # undated or too old

        # Title: a heading if the card has one, otherwise the element whose
        # class mentions "title".
        title_el = card.find(["h1", "h2", "h3", "h4"]) or card.find(class_=re.compile("title", re.I))
        title = title_el.get_text(" ", strip=True) if title_el else card.get_text(" ", strip=True)

        # Some cards include a short blurb paragraph; use it if it's there.
        blurb = card.find("p")

        items.append({
            "title": title,
            "date": day.isoformat(),
            "url": url,
            "summary": blurb.get_text(" ", strip=True) if blurb else "",
        })
    return items


# Maps each source "type" to the function that handles it.
FETCHERS = {
    "feed": fetch_feed,
    "dario": fetch_dario,
    "anthropic": fetch_anthropic,
}


# --- Main program ------------------------------------------------------------

def main():
    # Windows terminals sometimes can't print characters like curly quotes;
    # switching to UTF-8 stops that from crashing the summary at the end.
    sys.stdout.reconfigure(encoding="utf-8")

    # Read --days from the command line (defaults to 14, see the note at the top).
    parser = argparse.ArgumentParser(description="Fetch recent posts for the AI digest.")
    parser.add_argument("--days", type=int, default=14, help="how many days back to include (default 14)")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=args.days)

    results = []  # sources that worked, with their items
    failed = []   # sources that broke, with the reason

    for source in SOURCES:
        print(f"Fetching {source['name']}...")
        fetcher = FETCHERS[source["type"]]
        try:
            items = fetcher(source, cutoff)
            # Newest first. ISO-style dates sort correctly as plain text.
            items.sort(key=lambda item: item["date"], reverse=True)

            # Open each article and store its main text. This has its own
            # try/except: if one article can't be read, that item just gets
            # an empty full_text and everything else carries on.
            for item in items:
                try:
                    item["full_text"] = fetch_full_text(item["url"])
                except Exception:
                    item["full_text"] = ""

            results.append({"name": source["name"], "items": items})

        # A bad HTTP status gets reported as its code, e.g. "HTTP 403".
        except requests.HTTPError as error:
            failed.append({"name": source["name"], "url": source["url"],
                           "reason": f"HTTP {error.response.status_code}"})
        # Anything else (timeout, no internet, page layout changed...) gets
        # reported by its error type and message. Catching everything here is
        # what stops one broken source from crashing the whole run.
        except Exception as error:
            failed.append({"name": source["name"], "url": source["url"],
                           "reason": f"{type(error).__name__}: {error}"})

    # Write the JSON file. ensure_ascii=False keeps characters like é and
    # curly quotes readable instead of turning them into é codes.
    output = {
        "fetched_at": now.isoformat(timespec="seconds"),
        "window_days": args.days,
        "sources": results,
        "failed": failed,
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Print the summary.
    total = sum(len(source["items"]) for source in results)
    print(f"\nLast {args.days} days: {total} items from {len(results)} sources")
    for source in results:
        # Count how many items we managed to get article text for.
        with_text = sum(1 for item in source["items"] if item["full_text"])
        print(f"  {len(source['items']):>3}  {source['name']}  ({with_text} with full text)")
    if failed:
        print(f"\nFailed ({len(failed)}):")
        for failure in failed:
            print(f"  {failure['name']}: {failure['reason']}")
    print(f"\nSaved to {OUTPUT_FILE}")


# This line means "only run main() when the file is run directly", not when
# another script imports it.
if __name__ == "__main__":
    main()
