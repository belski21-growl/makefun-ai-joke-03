"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one joke about AI coding agents to /output/entry.txt. The joke is
written exactly as-is, with no trailing line end: the judge reads exactly
the bytes in the file, so no line end we do not mean to show.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent promised minimal changes, then rewrote the whole file "
    "and kept one line untouched \u2014 proof of life."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
