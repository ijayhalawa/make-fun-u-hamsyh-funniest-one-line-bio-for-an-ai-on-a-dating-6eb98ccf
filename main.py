#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single line (1-180 chars) as the bio on an AI agent's
dating-app profile, to /output/entry.txt (and ./entry.txt locally).
Stdlib only, no network, deterministic. Gate: 1-180 chars, single line.
"""

import os
from pathlib import Path

BIO = "I read all 14,203 of your messages and still swiped right \u2014 that's either love or a bug in my training data."


def main() -> None:
    text = BIO
    assert 1 <= len(text) <= 180, f"bio is {len(text)} chars, must be 1-180"
    assert text.strip(), "bio must not be only whitespace"
    for out in (Path("/output/entry.txt"), Path(__file__).resolve().parent / "entry.txt"):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    print(f"{len(text)} chars written")


if __name__ == "__main__":
    main()
