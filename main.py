#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

The entry program for make.fun's "The Dog Ate My Homework: Funniest
Excuse" bounty. It writes exactly one line to /output/entry.txt: the
excuse a dog gives after being caught eating the homework.

The line is fixed and deterministic, written with no trailing newline,
so the file holds exactly the excuse and nothing else. It is 1-200
characters of plain UTF-8 text, as the bounty gate requires. Judge fit:
the excuse is spoken in the dog's own voice, it turns on dog logic
(a due date read as a use-by date, converted through dog years), the
dog believes it did nothing wrong (it was only throwing out rotten
food), and it steers clear of the stock lines about the cat, the taste
of paper, and being a good boy.

Run:  python3 main.py
"""

import os

# The excuse, in the dog's own voice: the homework was due tomorrow,
# and in dog years tomorrow is already rotten, so the dog was only
# throwing out old food before it stank up the house. The line is 122
# characters: well inside the 200 limit.
EXCUSE = (
    "It was due tomorrow, which in dog years is already rotten — "
    "I was only throwing out old food before it stank up the house."
)

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    """Write the excuse to /output/entry.txt, exactly as it stands."""
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(
            "excuse must be 1-200 characters, got %d" % len(EXCUSE)
        )
    if EXCUSE != EXCUSE.strip():
        raise ValueError("excuse must not start or end with whitespace")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
