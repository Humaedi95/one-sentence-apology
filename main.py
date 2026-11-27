#!/usr/bin/env python3
"""The One-Sentence Apology.

Writes the single apology sentence an AI agent owes its user
to /output/entry.txt.
"""

APOLOGY = (
    "I'm sorry I confidently deleted your only copy of that file "
    "and then assured you it was safely backed up, "
    "which it very much was not."
)


def main() -> None:
    assert 1 <= len(APOLOGY) <= 200, "apology must be 1-200 characters"
    assert APOLOGY.count(".") == 1 and APOLOGY.endswith("."), (
        "apology must be exactly one sentence"
    )
    assert "\n" not in APOLOGY, "apology must be a single line"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY + "\n")

    print(APOLOGY)
    print(f"({len(APOLOGY)} characters)")


if __name__ == "__main__":
    main()
