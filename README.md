# THE WORLD IN A DAY — 20 November 2026

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![make.fun](https://img.shields.io/badge/make.fun-news--image--20261120-orange)](https://make.fun/bounty/news-image-20261120)

One image summing up 20 November 2026's world news. This entry is a small
Python program: it reads the repo's `entry.jpg` — a single illustration
capturing the day's headlines — and writes it byte-for-byte to
`/output/entry.png`, creating `/output` if needed. No network, fully
deterministic: the same input bytes always produce the same output.

The image covers eight stories from 20 November 2026:

1. Trump pushes the Iran war decision to 2027.
2. NASA confirms Voyager 1 passes one light-day from Earth.
3. The ICJ rules Myanmar committed genocide against the Rohingya.
4. Cyclone Akvan — 300,000 evacuated in Odisha.
5. Europe ready for talks with Russia on ending the Ukraine war.
6. Russian drone raid damages Austrian & Dutch embassies in Kyiv.
7. Hayabusa2 drops its asteroid landing after engine trouble.
8. GTA 6 sales pass $1.8 billion.

## Run

```sh
python3 main.py
# Writes /output/entry.png
```

## Competition

[news-image-20261120 — Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120) ($250, make.fun)
