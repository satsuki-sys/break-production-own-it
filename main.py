#!/usr/bin/env python3
"""Break Production, Own It — the one line an AI agent prints the instant
it breaks production. Writes the entry to /output/entry.txt."""

import os

ENTRY = (
    "I dropped the production database ten minutes ago. No backup, "
    "no rollback \u2014 just me, one bad command, and 40,000 users "
    "refreshing a dead page."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
