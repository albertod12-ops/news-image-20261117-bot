"""Write the 17 Nov 2026 world-news front page to /output/entry.png.

The image is held in this repository (entry.png, 1024x1024, <1 MiB);
this program copies it, deterministically, with no network.
35 stories from 6 continents, Crimea bridge lead, in the style of the
13 Nov winner: navy masthead, huge serif date, 11 illustrated cards,
world map with numbered pins, 24-item also-strip.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The copy is verified byte for byte, and a missing or empty source
fails loudly instead of writing a partial entry.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print("entry.png is missing", file=sys.stderr)
        return 1
    if os.path.getsize(SRC) == 0:
        print("entry.png is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, out)
    with open(SRC, "rb") as f:
        source = f.read()
    with open(out, "rb") as f:
        written = f.read()
    if source != written:
        print("entry.png copy differs", file=sys.stderr)
        return 1
    print(f"wrote {out} ({len(written)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
