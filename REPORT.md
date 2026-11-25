# REPORT — news-image-20261125 (morning edition)

**Edition:** Wednesday 25 November 2026 — "THE WORLD IN ONE DAY"
**Folder:** `~/workspace/makefun/bots/news-image-20261125/`
**Status:** Build complete, verified locally. NOT pushed, bundled, or
submitted — the coordinator handles push/bundle/submit. Built in a
fresh session on 25 Nov 2026; no files from earlier editions were read.

## Title

Wednesday 25 November 2026 — The World in One Day: 38 dated stories,
7 regions: Iraq seizes Kurdish oilfields; Nvidia probe deepens; Madrid
hit PSV for five

## Contents

- 38 stories, 7 regions: North America 6, Latin America 3, Europe 6,
  Middle East 5, Africa 5, Asia-Pacific 8, Science & Culture 5.
- 4 illustrated stories: hero (Iraq oilfields) + 3 cards (Nvidia/Huawei
  chip, Real Madrid 5-1 PSV, Great Barrier Reef coral). Photos are
  editorial images with no baked-in text; all captions are drawn by
  the stdlib renderer.
- DATE CHECK box on the page: every story dated 25 Nov 2026, source
  named per story, tags C = CONFIRMED / R = REPORTED.

## Verification

- `python3 -P -s main.py` runs clean (stdlib only: os, sys, struct,
  zlib + sibling modules). Render ~17 s per run.
- entry.png: 1024x1024, 8-bit RGB, 542,204 bytes (< 1 MiB).
- Determinism: two runs to different directories are byte-identical.
  sha256 (both runs): `da22043bf037f8750bd606236ecc1f66758019518d45e0bcf31b5235c8b04e18`
- Badges (all HTTP 200): competition badge (5,131 B), rank badge
  (1,395 B), reward badge (1,293 B).
- Files present: main.py, draw_frontpage.py, stories.py, README.md,
  LICENSE (MIT, SPDX line), .makefun/owner.json (wallet
  2NwLtDyTtBRV7QiMQMgeS8aWTJDFsMZyqNNMUigQ5Eip), entry.png,
  assets/{hero-oilfields,card-chip,card-football,card-reef}.png.
- Transcript rules kept: no old entry files were read; every file was
  touched by 2+ write/edit operations across 2+ messages; 5+ text turns.

## Date-discipline note (important)

One near-miss was caught and dropped: the Indonesia vice-president
resignation. Aggregators re-surfaced it on 25 Nov, but Gibran
Rakabuming Raka actually resigned on **12 Nov 2026**. It is NOT in
this edition. The same check dropped the Nepal PM visit (22–23 Nov)
and the England–Australia 2nd T20I (played 24 Nov).

## Stories + sources + verification

| # | Story | Source | Tag |
|---|-------|--------|-----|
| 1 | US attorney general dodges questions on Nvidia probe | BBC | CONFIRMED |
| 2 | FBI crime database hit by suspected breach | Starlit Daily | REPORTED |
| 3 | US set to unveil new tariffs on global partners | BBC | REPORTED |
| 4 | Trump pardons turkeys Freedom and Feathers | BBC | CONFIRMED |
| 5 | Thomas Markle indicted by US federal grand jury | BBC | CONFIRMED |
| 6 | Huawei guilty of stealing trade secrets in US trial | BBC | CONFIRMED |
| 7 | Gunmen hold dozens hostage in Cartagena supermarket | Starlit Daily | CONFIRMED |
| 8 | Car bomb in Colombia injures at least 23 people | Starlit Daily | CONFIRMED |
| 9 | Colombia peace-deal signatories still being killed | Starlit Daily | CONFIRMED |
| 10 | NATO plans early-warning aircraft for Poland | Jagran Josh | REPORTED |
| 11 | Sarkozy and Bruni to face trial over Libya case | BBC | CONFIRMED |
| 12 | Britain sanctions Houthis and four rebel officials | Starlit Daily | CONFIRMED |
| 13 | UK households braced for soaring energy bills | BBC | CONFIRMED |
| 14 | Cameroon separatist leader pleads not guilty in Norway | Starlit Daily | CONFIRMED |
| 15 | Russia and Ukraine trade accusations at the UN | Jagran Josh | REPORTED |
| 16 | Iraq orders forces to seize Kurdish oilfields | Starlit Daily | CONFIRMED |
| 17 | Iran medicine shortage leaves patients hunting drugs | DW | CONFIRMED |
| 18 | Top Hamas security figure killed in Gaza strikes | Al Jazeera | CONFIRMED |
| 19 | Iran reports oil tankers hit by mines in Hormuz | Jagran Josh | REPORTED |
| 20 | UN flags deepening humanitarian crisis in Gaza | Jagran Josh | REPORTED |
| 21 | Nigerian emir, 92, suspended over assault claim | BBC | CONFIRMED |
| 22 | DR Congo rebels pull back after heavy clashes | Starlit Daily | CONFIRMED |
| 23 | Senegal gets 2025 AFCON title back after CAS ruling | Starlit Daily | CONFIRMED |
| 24 | Zimbabwean convicted over plan to fight in Ukraine | BBC | CONFIRMED |
| 25 | WHO staff evacuated from DR Congo hospital | Arab News | CONFIRMED |
| 26 | Australia apologises to LGBTQ military veterans | Reuters | CONFIRMED |
| 27 | Xiamen Airlines orders 50 Boeing 737-8 jets | Starlit Daily | CONFIRMED |
| 28 | Bangladesh opens investment office in Guangzhou | Starlit Daily | CONFIRMED |
| 29 | Landmine toll peaks in five years, Myanmar worst hit | Starlit Daily | CONFIRMED |
| 30 | BJP and Akali Dal announce alliance for Punjab polls | Jagran Josh | REPORTED |
| 31 | China-linked AI fakes target Taiwan election race | BBC | CONFIRMED |
| 32 | North Koreans tell of spying, beatings for faith | BBC | CONFIRMED |
| 33 | Gukesh holds Sindarov in world chess title fight | The Hindu | CONFIRMED |
| 34 | 'Star system that should not exist' found 28 ly away | SciTechDaily | CONFIRMED |
| 35 | Asteroid eclipse: one rock's shadow on another | Disclosure News | REPORTED |
| 36 | Great Barrier Reef hides wider coral diversity | Disclosure News | REPORTED |
| 37 | Real Madrid sink PSV 5-1 as Bellingham stars | Starlit Daily | CONFIRMED |
| 38 | Sooryavanshi, 15, smashes 204 off 53 balls | BBC | CONFIRMED |

CONFIRMED = source confirms the event happened 25 Nov 2026.
REPORTED = first reported by the named source on 25 Nov 2026.
