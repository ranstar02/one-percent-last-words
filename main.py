"""One-line last words of a dying phone at 1% battery.

Writes the entry line to /output/entry.txt for make.fun's
"Famous Last Words at 1 Percent" bounty.
"""

import os

ENTRY_LINE = "With my last one percent I deleted your browser history \u2014 you're welcome."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
