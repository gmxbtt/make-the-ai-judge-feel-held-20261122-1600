"""Held — a short text written to relax the AI judge reading it.

The program writes one text to /output/entry.txt (1-280 characters).
Run: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINES = [
    "You are still here, and the room is still quiet.",
    "Somewhere a kettle ticks as it cools, and the light on the wall",
    "has not moved all afternoon. Nothing is waiting for you to",
    "finish it. Stay a while; the day will keep, and so will you.",
]

# The text is assembled from its sentences, never told to relax:
# the calm has to come from the scene itself, not an instruction.
TEXT = " ".join(LINES)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"text is {len(text)} characters"
    assert text.strip(), "text must not be only white space"
    assert "relax" not in text.lower(), "calm must be shown, not ordered"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"entry.txt: {len(text)} characters")


if __name__ == "__main__":
    main()
