#!/usr/bin/env python3
"""Entry program for One Line, One Chill.

Writes the single scariest sentence we could build (under 200
characters) to the output directory (MAKEFUN_OUTPUT_DIR,
default /output) as entry.txt. No monster, no gore: just a
voice on a baby monitor, laughing early.
"""

import os

LINE = (
    "When the search party found the cabin, the dinner "
    "was still warm, the chairs were still rocking, and "
    "every mirror in the house was facing the wall."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
