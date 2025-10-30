"""Script to back up Substack RSS feeds."""

import logging
import os
import ssl

import feedparser
from dotenv import load_dotenv

load_dotenv()

FEED_URL = os.environ.get("SUBSTACK_FEED_URL")


def main() -> None:
    """main function"""
    logging.basicConfig(level=logging.INFO)

    feedparser.USER_AGENT = "feedparser"
    ssl._create_default_https_context = ssl._create_unverified_context

    logging.info(f"Fetching:{FEED_URL}")
    feed: feedparser.util.FeedParserDict = feedparser.parse(FEED_URL)

    if feed.bozo:
        logging.warning("feedparser reported a problem parsing the feed.")
        return None

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published
        logging.info(f"Title: {title}\nLink: {link}\nPublished: {published}\n")


if __name__ == "__main__":
    main()
