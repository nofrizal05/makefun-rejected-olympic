"""Rejected Olympic Sports — one funny single-line sport.

Writes the entry line to /output/entry.txt (created if needed).
Python standard library only.

The joke: a password everyone has forgotten, treated as a stadium
event — the twist ("with no reset link") lands on the last words.
"""

import os

LINE = (
    "Competitive Password Remembering: contestants recall a "
    "14-character password set in 2019, under stadium lights, "
    "with no reset link."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
