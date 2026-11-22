#!/usr/bin/env python3
"""news-image-20261121 entrypoint: copy the front-page image to the output dir.

The entry image (entry.png, 1024x1024, the world news of Saturday
21 November 2026) ships in this repository; this program copies it to
$MAKEFUN_OUTPUT_DIR/entry.png. Deterministic: every run writes the same bytes.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit(f"entry image missing: {src}")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    sys.exit(main())
