#!/usr/bin/env python3
"""Write one funny one-liner about an AI agent's worst Monday.

Deterministic: the same line is written on every run. The line is
checked to be 1-140 characters and non-blank before writing.
"""

LINE = "Monday: my deploy crashed, my inbox hit 4,000 tickets, and stand-up could've been a message — so I filed a ticket against Monday itself."


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
