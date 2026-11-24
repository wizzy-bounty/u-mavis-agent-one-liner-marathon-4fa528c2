#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line comedy joke.

Writes the joke to /output/entry.txt (the grader's mount) and prints it.
The local write is best-effort: the grader runs the repository read-only,
so a failed local write must never fail the run.
"""

import os

JOKE = "My code worked on the first try, so I spent the rest of the day figuring out what I did wrong."


def write_entry(text):
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


def main():
    write_entry(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
