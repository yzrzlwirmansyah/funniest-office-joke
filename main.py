#!/usr/bin/env python3
"""The Funniest Office Joke — writes one funny office joke to a file.
Choice: title inflation instead of a raise. "Cover" is the turn —
the bigger title covers the unchanged salary. The punchline lands
on the last words.
"""

import os
import sys

JOKE = "My promotion came with a bigger title so it could cover the salary."


def main() -> int:
    if not JOKE.strip() or len(JOKE) > 200 or "\r" in JOKE or "\n" in JOKE:
        print("invalid joke content", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)  # exactly 67 chars, no trailing newline
    return 0


if __name__ == "__main__":
    sys.exit(main())
