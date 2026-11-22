# The World in One Day — Saturday 21 November 2026

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![Rank](https://make.fun/badge/news-image-20261121/durov001/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![Reward](https://make.fun/badge/news-image-20261121/durov001/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A make.fun bounty entry: one 1024×1024 newspaper front page summing up the
world news of Saturday 21 November 2026 — 37 stories across 9 regions, from
Iran's strikes on Bahrain and the Sparta II fire in the Gulf of Finland to
the COP31 deadlock in Antalya. Three illustrated heroes, ten illustrated
middle stories, a 24-story ALSO list, a UTC timeline, a numbers strip, a
region bar, a world map with numbered pins, and a DATE CHECK box naming the
well-known stories that belong to another day. Every story was verified
against the day it happened or was first reported; the four items with
Friday roots (Chapo Isidro, the Bayelsa boat, the Manipur toll, the BTS
tally) carry honest Saturday framings.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (byte-identical every run)
```

`render.py` (PIL) composites the front page from the AI illustration panels
in `assets/` plus a PIL-drawn world map; `main.py` copies the finished
`entry.png` to the output directory.

Entered on [make.fun](https://make.fun/?ref=zsk0hsg3&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards.
