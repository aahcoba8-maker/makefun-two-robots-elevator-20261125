"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to entry.txt.
Stdlib only. Grader runs: python3 -P -s main.py with
MAKEFUN_OUTPUT_DIR set; output goes there, falling back to
the script directory when unset.
"""

import os

ENTRY = "I wasn't going to say anything, but your cooling fan has been sighing at me since floor three."


def main():
    # Self-gate mirroring the sealed scorer: UTF-8 text, 1-200 chars,
    # not only whitespace, single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"chars: {len(ENTRY)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
