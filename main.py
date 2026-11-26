"""Build THE WORLD IN ONE DAY for Wednesday 25 November 2026.

Usage: python3 -P -s main.py [output.png]
Standard library only. Renders entry.png (1024x1024, under 1 MiB).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw_frontpage import render
from stories import CARDS, DATE_LINE, REGIONS, STORIES, TITLE


def check_stories():
    assert len(STORIES) == 49, "need 49 stories, got %d" % len(STORIES)
    seen = {}
    for story in STORIES:
        seen[story["region"]] = seen.get(story["region"], 0) + 1
        words = len(story["summary"].split())
        assert 40 <= words <= 70, (
            "summary %d words: %s" % (words, story["headline"]))
    for region in REGIONS:
        assert seen.get(region, 0) == 7, (
            "region %s has %d stories" % (region, seen.get(region, 0)))


def main():
    check_stories()
    base = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) > 1:
        out = sys.argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        os.makedirs(out_dir, exist_ok=True)
        out = os.path.join(out_dir, "entry.png")
    ends = render(base, STORIES, CARDS, TITLE, DATE_LINE, out)
    top = max(ends)
    assert top <= 1000, "columns overflow: tallest ends at %d" % top
    size = os.path.getsize(out)
    assert size < 1024 * 1024, "entry.png too big: %d bytes" % size
    print("title: %s" % TITLE)
    print("stories: %d" % len(STORIES))
    print("regions: %d" % len(REGIONS))
    print("column ends: %s" % (ends,))
    print("entry.png: %d bytes" % size)
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
