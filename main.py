#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261120 bounty.

Reads the single image that sums up 20 November 2026's world news
(entry.jpg, stored next to this file) and writes it byte-for-byte to
/output/entry.png, creating /output if needed. No network, fully
deterministic: the same input bytes always produce the same output.

The eight stories the image sums up: Trump pushes the Iran war decision
to 2027; NASA confirms Voyager 1 passes one light-day from Earth; the ICJ
rules Myanmar committed genocide against the Rohingya; Cyclone Akvan,
300,000 evacuated in Odisha; Europe ready for talks with Russia on ending
the Ukraine war; a Russian drone raid damages the Austrian and Dutch
embassies in Kyiv; Hayabusa2 drops its asteroid landing after engine
trouble; GTA 6 sales pass $1.8 billion.
"""

import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.jpg"
    if not source.is_file():
        raise FileNotFoundError(
            f"entry.jpg is missing next to main.py: {source}"
        )
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / "entry.png")
    print("Wrote /output/entry.png")


if __name__ == "__main__":
    main()
