#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — the note a smart fridge leaves
on its door screen for its owner.

The fridge keeps the leftovers at a perfect 4 degrees while the owner's
diets come and go. It has opinions about that, and it has decided to
share them, dryly, in one line.

The program writes exactly one line (118 characters, within the 200 cap)
to /output/entry.txt.
"""

import os

ENTRY = (
    "Day 9 of the leftovers. "
    "They have now outlived two of your diets. "
    "I keep them at 4\u00b0C out of professionalism, not hope."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts the raw file, so the file
    # must hold exactly the 118-character line, nothing more.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
