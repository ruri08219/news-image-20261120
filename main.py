"""news-image-20261120: sum up 20 November 2026's world news in one image.

Reads the repo's ``entry.jpg`` (the single image that summarises the day's
world news) and writes it byte-for-byte to ``/output/entry.png``.

The image covers these 8 stories from 20 November 2026:

1. Trump pushes Iran war decision to 2027.
2. NASA confirms Voyager 1 passes one light-day from Earth.
3. ICJ rules Myanmar committed genocide against the Rohingya.
4. Cyclone Akvan - 300,000 evacuated in Odisha.
5. Europe ready for talks with Russia on ending the Ukraine war.
6. Russian drone raid damages Austrian & Dutch embassies in Kyiv.
7. Hayabusa2 drops asteroid landing after engine trouble.
8. GTA 6 sales pass $1.8 billion.

No network access is needed; the program is fully deterministic: the output
is always an exact copy of the bundled entry.jpg bytes.
"""

import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        raise FileNotFoundError(
            f"entry.jpg is missing from the repo directory: "
            f"expected it at {SOURCE}. Re-add the image file, then re-run."
        )
    with open(SOURCE, "rb") as f:
        data = f.read()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(f"Wrote {len(data)} bytes to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
