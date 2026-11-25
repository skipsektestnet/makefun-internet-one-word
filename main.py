"""The Internet in One Word: writes the entry text to /output/entry.txt.

Why this word: the whole internet, distilled into one compulsive act —
the endless scroll through bad news, memes, outrage and cat videos at
2 a.m. when you meant to check one thing. It is funny, it fits, and it
is what the internet actually does to all of us.
"""

import os

# The entry itself: one word, the whole internet in it.
ENTRY = 'Doomscroll'

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    # Guard: never submit a blank entry to the sealed gate.
    assert text and not text.isspace(), "entry must not be empty"
    # Guard: the bounty asks for exactly one word, no extra whitespace.
    assert text == text.strip(), "entry must have no surrounding whitespace"
    assert len(text.split()) == 1, "entry must be a single word"
    # Guard: one plain word, letters only — no punctuation tricks.
    assert text.isalpha(), "entry must be letters only"
    return text


def write_entry(text):
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    write_entry(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
