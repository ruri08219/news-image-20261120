"""Entry program for make.fun bounty news-image-20261120.

Writes the pre-built front-page image (entry.jpg) byte-for-byte to
/output/entry.png. Fully deterministic, no network access.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
