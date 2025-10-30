"""Script to back up Substack RSS feeds."""

import os

from dotenv import load_dotenv

load_dotenv()

FEED_URL = os.environ.get("SUBSTACK_FEED_URL")


def main() -> None:
    """main function"""
    print(f"Fetching:{FEED_URL}")


if __name__ == "__main__":
    main()
