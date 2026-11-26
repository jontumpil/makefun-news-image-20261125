# REPORT — news-image-20261125-r2 (revisi ronde 2)

## Edisi

- Judul: Wednesday 25 November 2026: 49 stories, 7 regions, Hormuz
  tankers mined, Shenzhou-24 flies first foreign astronaut, US
  tariffs hit 14 partners
- Slug: news-image-20261125
- Tanggal edisi: Rabu 25 November 2026
- Koran: THE WORLD IN ONE DAY
- Cerita: 49 (7 per region)
- Region: North America 7, Latin America 7, Europe 7, Middle East 7,
  Africa 7, Asia-Pacific 7, Science & Culture 7
- Tag: C = CONFIRMED 26, R = REPORTED 23
- Semua ringkasan 40-70 kata (rentang aktual 41-58 kata), ditulis dari
  artikel sumber masing-masing; semua cerita terverifikasi bertanggal
  25 November 2026 dari sumbernya (bukan agregator/judul).

## Berita utama bergambar (4 kartu)

1. Shenzhou-24 carries first foreign astronaut — `assets/shenzhou.png`
2. Two tankers hit mines in Hormuz — `assets/hormuz.png`
3. US hits 14 partners with new tariffs — `assets/tariffs.png`
4. Solomons sign pact barring foreign bases — `assets/solomon.png`

## Verifikasi

- `python3 -P -s main.py` jalan bersih (stdlib saja), ~2,5 detik.
- entry.png: 1024x1024, 253.139 byte (< 1 MiB).
- Determinisme: tiga run ke direktori berbeda byte-identical,
  sha256 `3ede8df16245d839f0dc7721e726c18e503947d85cbfdb6f68681d82b9f09c9d`.
- Kolom berakhir di y = 994, 959, 980, 994, 792 (batas 1000).
- Badge README ketiganya HTTP 200 (dicek 26 Nov 2026):
  `make.fun/badge/news-image-20261125.svg`,
  `.../jontumpil/makefun-news-image-20261125/rank.svg`,
  `.../jontumpil/makefun-news-image-20261125/reward.svg`.
- Aset foto dibuat dengan generator gambar lalu di-downscale ke
  480x320 (`downscale_assets.py`) agar render stdlib cepat; kartu
  tampil 191x72 di halaman.
- Catatan: kode referral `{referral_code}` di README belum terisi —
  koordinator harap mengisi dari `node cli/makefun.mjs referrals`
  sebelum submit.

## Tabel cerita

| # | Region | Headline | Sumber | Tag |
|---|--------|----------|--------|-----|
| 1 | North America | US hits 14 partners with new tariffs | Reuters | C |
| 2 | North America | CIA and spy chief hit by cyber breach | Reuters | C |
| 3 | North America | AI labs fear their own models, staff say | Axios | R |
| 4 | North America | Huang back at Nvidia as AI row grows | Reuters | C |
| 5 | North America | Doncic fires Lakers past Jazz | Reuters | C |
| 6 | North America | ICE frees Ecuador teen after ruling | EIN Presswire | R |
| 7 | North America | House GOP seeks block on UN chief pick | EIN Presswire | R |
| 8 | Latin America | Real rallies as bank sells $2bn | The Rio Times | R |
| 9 | Latin America | Ecuador vote silence starts Thursday | The Rio Times | R |
| 10 | Latin America | Mexico City marks 25N with marches | The Rio Times | R |
| 11 | Latin America | Argentine shops sell 3% less | The Rio Times | R |
| 12 | Latin America | Peso slides to 1,592 per dollar | DevEvil News | R |
| 13 | Latin America | Ecuador lifts wage to $500, IMF pays | DevEvil News | R |
| 14 | Latin America | Sinaloa governor loses pension again | The Rio Times | R |
| 15 | Europe | Ukraine hits Russian air base, 5 jets | Reuters | C |
| 16 | Europe | Russia's own files show 490,334 dead | BBC News | C |
| 17 | Europe | Merz: Russia wants more than Ukraine | Reuters | C |
| 18 | Europe | Zelensky, Magyar open new chapter | Geopolitiki | R |
| 19 | Europe | Zelensky: we hit Sparta II in gulf | Geopolitiki | R |
| 20 | Europe | BBC iPlayer set for ads, rival shows | Reuters | C |
| 21 | Europe | London Museum reopens in market hall | Reuters | C |
| 22 | Middle East | Two tankers hit mines in Hormuz | Reuters | C |
| 23 | Middle East | Houthis say they hit Ras Tanura | Reuters | C |
| 24 | Middle East | Israel kills Hamas security chief | Reuters | C |
| 25 | Middle East | Iran shrugs off US naval blockade | Reuters | C |
| 26 | Middle East | Iran tightens grip on Hormuz shipping | Reuters | C |
| 27 | Middle East | Egypt reopens Tripoli embassy | The Nexus Brief | R |
| 28 | Middle East | Saudi defences down four drones | Reuters | C |
| 29 | Africa | RSF drones kill 19 in Blue Nile | Reuters | C |
| 30 | Africa | Libya vows revenge for Benghazi strike | AP News | C |
| 31 | Africa | Zambia opposition chief faces treason | Harare.Today | R |
| 32 | Africa | Nollywood legend Pete Edochie dies at 79 | Harare.Today | R |
| 33 | Africa | UNAIDS warns HIV gains at risk | Harare.Today | R |
| 34 | Africa | Senegal win back AFCON title at CAS | Harare.Today | R |
| 35 | Africa | Sudan rejects Ethiopia as peace host | Okay News | R |
| 36 | Asia-Pacific | Solomons sign pact barring foreign bases | NYT / Reuters | C |
| 37 | Asia-Pacific | Bangladesh lifts garment wage 36% | Reuters | C |
| 38 | Asia-Pacific | Taiwan comic jokes on, defying Beijing | Reuters | C |
| 39 | Asia-Pacific | Hong Kong mourns fire dead, one year on | Reuters | C |
| 40 | Asia-Pacific | Myanmar rebel vows to fight on, one leg | Reuters | C |
| 41 | Asia-Pacific | Fujitsu joins OpenAI defence network | AI Brief | R |
| 42 | Asia-Pacific | Hanwha builds 180 MW defence AI hub | AI Brief | R |
| 43 | Science & Culture | Shenzhou-24 carries first foreign astronaut | Xinhua | C |
| 44 | Science & Culture | Pope warns as COP31 talks fail | AP News | C |
| 45 | Science & Culture | Top Gear returns with Ramsay at wheel | Reuters | C |
| 46 | Science & Culture | Z.ai ships flagship model GLM-5.4 | AI Brief | R |
| 47 | Science & Culture | Huawei HarmonyOS passes 100m devices | SCMP | R |
| 48 | Science & Culture | K-pop back in China? Summit sparks hope | SCMP | R |
| 49 | Science & Culture | UK watchdog warns on AI as Meta ships Muse | Reuters | C |
