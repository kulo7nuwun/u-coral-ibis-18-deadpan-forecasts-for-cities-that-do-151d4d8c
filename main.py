#!/usr/bin/env python3
"""Deadpan forecast for the city that does not exist: Port Mercy.

Writes exactly one line -- a deadpan weather forecast for the invented
city of Port Mercy -- to /output/entry.txt. The line is fixed and
deterministic: the same bytes come out on every run.
"""

import os

ENTRY = (
    "In Port Mercy, expect 41 degrees and a light drizzle of confetti; "
    "umbrellas advised, joy not guaranteed. Back to you, studio."
)

OUTPUT_PATH = "/output/entry.txt"


def check_entry(text: str) -> None:
    """Gate self-checks, mirroring the competition gate: UTF-8 text of
    1 to 160 characters, not only whitespace, a single line, and no
    trailing newline."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what landed on disk matches the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from the entry"
    check_entry(written)


if __name__ == "__main__":
    main()
