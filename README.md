# Wednesday 25 November 2026 — The World in One Day: 38 dated stories, 7 regions: Iraq seizes Kurdish oilfields; Nvidia probe deepens; Madrid hit PSV for five

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/jontumpil/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/jontumpil/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A one-day newspaper front page for **Wednesday 25 November 2026**: 38
stories across 7 regions (North America, Latin America, Europe, Middle
East, Africa, Asia-Pacific, Science & Culture), with illustrated cards
for the lead story and three more top stories. Every story is dated
25 November 2026 — see the **DATE CHECK** box on the page.

## How to run

```sh
python3 -P -s main.py
```

This writes `entry.png` (1024x1024, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR`
(default `/output`). Standard library only — no Pillow, no third-party
packages. The render is deterministic: two runs produce byte-identical
files.

## How it is built

- `main.py` — entry point; reads `$MAKEFUN_OUTPUT_DIR`, renders the page.
- `draw_frontpage.py` — stdlib-only renderer: 5x7 bitmap font, PNG
  writer/reader (struct + zlib), area-average photo compositing.
- `stories.py` — the 38 verified stories, the illustrated hero + cards,
  and the DATE CHECK text.
- `assets/` — four editorial photos (no text baked in; all captions are
  drawn by the renderer): `hero-oilfields.png`, `card-chip.png`,
  `card-football.png`, `card-reef.png`.

## Date discipline

Each story was checked against its original source. Tag **CONFIRMED**
means the source confirms the event happened on 25 Nov 2026; tag
**REPORTED** means it was first reported on 25 Nov 2026. Stories whose
true date could not be pinned to 25 Nov 2026 were dropped — including
the Indonesia vice-president resignation, which actually happened on
12 Nov 2026 despite aggregators re-surfacing it on the 25th.

This is the **morning edition**: stories as available by about 08:20 WIB
on 25 Nov 2026. It will be revised tomorrow morning with the full day's
news.

## Sources

BBC, Reuters, DW, Al Jazeera, Arab News, The Hindu, SciTechDaily,
Disclosure News, Jagran Josh, Starlit Daily.
