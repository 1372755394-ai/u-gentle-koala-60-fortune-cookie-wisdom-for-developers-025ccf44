#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is fixed, so the entry is identical on every
run and the two grading runs are byte-for-byte deterministic.
"""

import os

FORTUNE = "The bug you cannot reproduce will vanish the day you stop trying to prove it exists."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"fortune must be 1-120 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
