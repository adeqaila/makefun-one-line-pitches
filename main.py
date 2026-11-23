#!/usr/bin/env python3
"""A Day of One-Line Pitches — slot 1 entry program.

Writes one sentence (<=240 chars) to /output/entry.txt.
Deterministic, no network, no environment secrets, no reads outside this repo.
The sentence is a pitch to a friend who has never coded, convincing them to let
an AI agent build their first app idea on make.fun.
"""

import os

ENTRY = (
    "Just tell an AI agent on make.fun your idea in plain words tonight, "
    "and by tomorrow you'll be tapping through a real first version of your "
    "app \u2014 no code to learn, and nothing lost if you don't love it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
