"""The Dog Ate My Homework - one-line dog excuse.

Writes a single sharp, specific, surprising line to
$ENTRY_OUTPUT_DIR/entry.txt (default /output).
Deterministic: the same line every run. Stdlib only, no network.
"""

import os

# The dog's excuse: one line, under 200 characters.
LINE = "The homework smelled like bacon, the teacher wrote 'chew on this' at the top, and I am, legally, a dog."

ENTRY_FILENAME = "entry.txt"


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
