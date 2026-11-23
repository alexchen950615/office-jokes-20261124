#!/usr/bin/env python3
"""Entry for the make.fun bounty 'Make the AI Judge Laugh: Office Jokes'.

Writes a single original one-line office joke to /output/entry.txt.
Standard library only, no network access.
"""

import os

JOKE = (
    "HR said the open-plan office would boost collaboration, "
    "so now twelve of us collaborate daily on ignoring each other in perfect silence."
)


def main() -> None:
    text = JOKE.strip()
    if not text or len(text) > 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
