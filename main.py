#!/usr/bin/env python3
"""The One-Liner Groan-Off — Variant A (kitchen/food dad pun).

Deterministic, no network, no secrets, no reading git history.
Writes the joke to /output/entry.txt FIRST, then (guarded in
try/except) copies it to the repo-root entry.txt, so the program
still exits 0 when the repo is mounted read-only.
"""

import os
import shutil

JOKE = "My toaster filed for divorce this morning — it said I'd let things go stale and never once buttered it up."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = JOKE
    # Gate self-check: 1-140 characters, single line, non-blank.
    assert 1 <= len(text) <= 140, "gate: joke must be 1-140 characters"
    assert "\n" not in text.strip(), "gate: joke must be one line"
    assert text.strip(), "gate: joke must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    # Best-effort copy to the repo root; a read-only mount must not fail us.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        shutil.copyfile(OUTPUT_PATH, os.path.join(here, "entry.txt"))
    except OSError:
        pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
