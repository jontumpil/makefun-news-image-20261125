# stories.py -- story data for THE WORLD IN ONE DAY, 25 November 2026.
# Every story below was verified against its original source as dated
# Wednesday 25 November 2026 (event date or first-report date).
# Stories whose true date could not be pinned to 25 Nov 2026 were dropped,
# including the Indonesia VP-resignation story: Gibran Rakabuming Raka
# actually resigned on 12 Nov 2026, not 25 Nov, despite aggregators
# re-surfacing it on the 25th. Date discipline is the whole game here.
#
# Tags: CONFIRMED = source confirms the event itself happened 25 Nov 2026.
#       REPORTED  = first reported by the named source on 25 Nov 2026.
# Morning edition: stories as available by about 08:20 WIB on 25 Nov 2026.
# A fuller revision with the complete day's news follows tomorrow morning.

EDITION_DATE = "Wednesday 25 November 2026"
EDITION_SLUG = "news-image-20261125"
STORY_COUNT = 38
REGION_COUNT = 7

TITLE_LINE = (
    "Wednesday 25 November 2026 -- The World in One Day: "
    "38 dated stories, 7 regions: Iraq seizes Kurdish oilfields; "
    "Nvidia probe deepens; Madrid hit PSV for five"
)

REGIONS = [
    "NORTH AMERICA",
    "LATIN AMERICA",
    "EUROPE",
    "MIDDLE EAST",
    "AFRICA",
    "ASIA-PACIFIC",
    "SCIENCE & CULTURE",
]

# (region, headline, source, tag)
STORIES = [
    # ---- NORTH AMERICA (6) ----
    ("NORTH AMERICA",
     "US attorney general dodges questions on Nvidia probe",
     "BBC", "CONFIRMED"),
    ("NORTH AMERICA",
     "FBI crime database hit by suspected breach",
     "Starlit Daily", "REPORTED"),
    ("NORTH AMERICA",
     "US set to unveil new tariffs on global partners",
     "BBC", "REPORTED"),
    ("NORTH AMERICA",
     "Trump pardons turkeys Freedom and Feathers",
     "BBC", "CONFIRMED"),
    ("NORTH AMERICA",
     "Thomas Markle indicted by US federal grand jury",
     "BBC", "CONFIRMED"),
    ("NORTH AMERICA",
     "Huawei guilty of stealing trade secrets in US trial",
     "BBC", "CONFIRMED"),
    # ---- LATIN AMERICA (3) ----
    ("LATIN AMERICA",
     "Gunmen hold dozens hostage in Cartagena supermarket",
     "Starlit Daily", "CONFIRMED"),
    ("LATIN AMERICA",
     "Car bomb in Colombia injures at least 23 people",
     "Starlit Daily", "CONFIRMED"),
    ("LATIN AMERICA",
     "Colombia peace-deal signatories still being killed",
     "Starlit Daily", "CONFIRMED"),
    # ---- EUROPE (6) ----
    ("EUROPE",
     "NATO plans early-warning aircraft for Poland",
     "Jagran Josh", "REPORTED"),
    ("EUROPE",
     "Sarkozy and Bruni to face trial over Libya case",
     "BBC", "CONFIRMED"),
    ("EUROPE",
     "Britain sanctions Houthis and four rebel officials",
     "Starlit Daily", "CONFIRMED"),
    ("EUROPE",
     "UK households braced for soaring energy bills",
     "BBC", "CONFIRMED"),
    ("EUROPE",
     "Cameroon separatist leader pleads not guilty in Norway",
     "Starlit Daily", "CONFIRMED"),
    ("EUROPE",
     "Russia and Ukraine trade accusations at the UN",
     "Jagran Josh", "REPORTED"),
    # ---- MIDDLE EAST (5) ----
    ("MIDDLE EAST",
     "Iraq orders forces to seize Kurdish oilfields",
     "Starlit Daily", "CONFIRMED"),
    ("MIDDLE EAST",
     "Iran medicine shortage leaves patients hunting drugs",
     "DW", "CONFIRMED"),
    ("MIDDLE EAST",
     "Top Hamas security figure killed in Gaza strikes",
     "Al Jazeera", "CONFIRMED"),
    ("MIDDLE EAST",
     "Iran reports oil tankers hit by mines in Hormuz",
     "Jagran Josh", "REPORTED"),
    ("MIDDLE EAST",
     "UN flags deepening humanitarian crisis in Gaza",
     "Jagran Josh", "REPORTED"),
    # ---- AFRICA (5) ----
    ("AFRICA",
     "Nigerian emir, 92, suspended over assault claim",
     "BBC", "CONFIRMED"),
    ("AFRICA",
     "DR Congo rebels pull back after heavy clashes",
     "Starlit Daily", "CONFIRMED"),
    ("AFRICA",
     "Senegal gets 2025 AFCON title back after CAS ruling",
     "Starlit Daily", "CONFIRMED"),
    ("AFRICA",
     "Zimbabwean convicted over plan to fight in Ukraine",
     "BBC", "CONFIRMED"),
    ("AFRICA",
     "WHO staff evacuated from DR Congo hospital",
     "Arab News", "CONFIRMED"),
    # ---- ASIA-PACIFIC (8) ----
    ("ASIA-PACIFIC",
     "Australia apologises to LGBTQ military veterans",
     "Reuters", "CONFIRMED"),
    ("ASIA-PACIFIC",
     "Xiamen Airlines orders 50 Boeing 737-8 jets",
     "Starlit Daily", "CONFIRMED"),
    ("ASIA-PACIFIC",
     "Bangladesh opens investment office in Guangzhou",
     "Starlit Daily", "CONFIRMED"),
    ("ASIA-PACIFIC",
     "Landmine toll peaks in five years, Myanmar worst hit",
     "Starlit Daily", "CONFIRMED"),
    ("ASIA-PACIFIC",
     "BJP and Akali Dal announce alliance for Punjab polls",
     "Jagran Josh", "REPORTED"),
    ("ASIA-PACIFIC",
     "China-linked AI fakes target Taiwan election race",
     "BBC", "CONFIRMED"),
    ("ASIA-PACIFIC",
     "North Koreans tell of spying, beatings for faith",
     "BBC", "CONFIRMED"),
    ("ASIA-PACIFIC",
     "Gukesh holds Sindarov in world chess title fight",
     "The Hindu", "CONFIRMED"),
    # ---- SCIENCE & CULTURE (5) ----
    ("SCIENCE & CULTURE",
     "'Star system that should not exist' found 28 ly away",
     "SciTechDaily", "CONFIRMED"),
    ("SCIENCE & CULTURE",
     "Asteroid eclipse: one rock's shadow on another",
     "Disclosure News", "REPORTED"),
    ("SCIENCE & CULTURE",
     "Great Barrier Reef hides wider coral diversity",
     "Disclosure News", "REPORTED"),
    ("SCIENCE & CULTURE",
     "Real Madrid sink PSV 5-1 as Bellingham stars",
     "Starlit Daily", "CONFIRMED"),
    ("SCIENCE & CULTURE",
     "Sooryavanshi, 15, smashes 204 off 53 balls",
     "BBC", "CONFIRMED"),
]

# Illustrated stories: (image asset, kicker, headline, blurb, source, tag)
HERO = (
    "assets/hero-oilfields.png",
    "MIDDLE EAST -- LEAD STORY",
    "Iraq orders forces to seize Kurdish oilfields",
    "Baghdad orders federal forces to take over oilfields and "
    "crossings in Kurdish-run areas, in the sharpest escalation "
    "of the long oil-revenue feud with the Kurdistan Region.",
    "Starlit Daily", "CONFIRMED",
)

CARDS = [
    (
        "assets/card-chip.png",
        "NORTH AMERICA -- TECH",
        "Nvidia probe deepens as Huawei found guilty",
        "The US attorney general ducks questions on the Nvidia "
        "inquiry as a US jury convicts Huawei of stealing "
        "trade secrets.",
        "BBC", "CONFIRMED",
    ),
    (
        "assets/card-football.png",
        "SCIENCE & CULTURE -- SPORT",
        "Real Madrid sink PSV 5-1 as Bellingham stars",
        "Bellingham's stunner and a Mbappe brace overturn a "
        "deficit and lift Madrid to the top of the table.",
        "Starlit Daily", "CONFIRMED",
    ),
    (
        "assets/card-reef.png",
        "SCIENCE & CULTURE -- SCIENCE",
        "Great Barrier Reef hides wider coral diversity",
        "Genetic analysis resurrects 12 Acropora species and "
        "reveals far more coral variety than science knew.",
        "Disclosure News", "REPORTED",
    ),
]

DATE_CHECK_TEXT = (
    "DATE CHECK -- Every story on this page is dated Wednesday "
    "25 November 2026. Sources are named per story. "
    "C = CONFIRMED: the source confirms the event happened on "
    "25 Nov 2026. R = REPORTED: first reported on 25 Nov 2026. "
    "Stories whose true date could not be verified were dropped."
)

FOOTER_TEXT = (
    "THE WORLD IN ONE DAY -- 38 STORIES -- 7 REGIONS -- "
    "ALL DATED 25 NOVEMBER 2026"
)


def stories_by_region(region):
    """Return the (headline, source, tag) rows for one region."""
    return [(h, s, t) for (r, h, s, t) in STORIES if r == region]
