"""One Word for Your Wi-Fi.

Writes a single word describing my Wi-Fi to /output/entry.txt:
"gaslighting" -- full bars, loads nothing, and insists the problem is you.
Pure stdlib, deterministic: identical bytes on every run.
"""

import os

WORD = "gaslighting"

# Gate guard: the entry must be exactly one word, 1-20 chars,
# no spaces, no punctuation, no whitespace of any kind.
assert 1 <= len(WORD) <= 20, "word must be 1-20 characters"
assert WORD.isalpha(), "word must be letters only"
assert WORD == WORD.strip() and " " not in WORD, "must be a single word"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
