#!/usr/bin/env python3
"""The Robot Apology — writes a two-line apology to /output/entry.txt.

Deterministic, no network, no input. Line 1: the robot apologises for one
specific, concrete mistake. Line 2: the lesson that follows from it, and
what it will do differently.

Revision (in-build): the second line was tightened so the lesson names the
exact check the robot skipped — testing the pot for soil — instead of a
generic promise to be more careful.
"""

import os

ENTRY = (
    "I am sorry I watered the plastic fern on your desk every morning "
    "for three weeks while your real basil wilted beside it.\n"
    "I have learned to check for soil before I water, so from now on I "
    "will test the pot first and only water what is actually thirsty.\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
