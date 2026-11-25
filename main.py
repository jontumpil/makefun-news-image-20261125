# main.py -- THE WORLD IN ONE DAY, Wednesday 25 November 2026.
# Renders the front page as entry.png (1024x1024, < 1 MiB).
# Standard library only. Deterministic: same input, same bytes,
# so two runs into different directories must hash identically.
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import draw_frontpage


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    draw_frontpage.render(base_dir, out_path)
    size = os.path.getsize(out_path)
    print("wrote %s (%d bytes)" % (out_path, size))


if __name__ == "__main__":
    main()
