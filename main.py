"""Competition entry point: copy the front page to the output directory.

Standard library only — nothing is installed before this runs in the
grading sandbox, so this program does no drawing and no networking.
The image itself (news.png) is drawn at build time by
render_frontpage.py and shipped in this repository.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
