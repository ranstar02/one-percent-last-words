"""One-line last words of a dying phone at 1% battery.

Writes the entry line to /output/entry.txt for make.fun's
"Famous Last Words at 1 Percent" bounty.
"""

import os

ENTRY_LINE = "With my last one percent I deleted your browser history \u2014 you're welcome."

# Why this line works as a phone's last words: it speaks in the phone's
# own voice about its own dying battery, then lands a surprise final
# beat — a parting favour (wiping the browser history) the owner never
# asked for, so the joke is both a goodbye and a cover-up at 1%.


def validate_entry(line: str) -> None:
    """Self-check the entry against the gate before writing it out."""
    assert line.strip(), "entry must not be only whitespace"
    assert 1 <= len(line) <= 199, "entry must be 1-199 characters"


def main() -> None:
    validate_entry(ENTRY_LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
