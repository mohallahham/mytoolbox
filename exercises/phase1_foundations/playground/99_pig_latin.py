# exercises/beginner/pig_latin.py
"""Simple Pig-Latin translator.

Rules
-----
1. If a word starts with a vowel, add 'yay' to the end.
2. If a word starts with a consonant, move the first letter to the end
   and add 'ay'.
"""

VOWELS = "aeiou"


def translate(word: str) -> str:
    """Return *word* converted to Pig-Latin (lower-case for simplicity)."""
    word = word.lower()

    if not word:  # guard against empty input
        return ""

    if word[0] in VOWELS:  # Rule 1
        return f"{word}yay"

    # Rule 2
    return f"{word[1:]}{word[0]}ay"


def _cli() -> None:
    """Interactive prompt."""
    while True:
        word = input("Type a word to translate to Pig-Latin (or 'q' to quit): ").strip()

        if word.lower() == "q":
            print("Goodbye!")
            break

        print(translate(word))


if __name__ == "__main__":  # only runs on  `python pig_latin.py`
    _cli()
