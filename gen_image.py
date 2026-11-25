"""Front page of Wednesday 25 November 2026, drawn entirely in code.

Layout (1024x1024, cream paper, serif masthead, navy/red/gold):
top banner, masthead + standfirst, THE DAY IN NUMBERS stats row,
region bar, THE DAY IN UTC timeline, 3 lead stories with code-drawn
panels, 12 small stories with code-drawn panels, a REAL world map
(Natural Earth 110m, filled land, numbered pins), a numbered ALSO
list, a DATE CHECK box and a sources/certainty footer.

Rules carried from 24 Nov v3 (round 2: 389/9063) and the v3 lessons:
TOTAL STORIES 34 (winners: 29-38; 44 was too dense), the three lead
panels are rich and dramatic, small panels are sharp and distinct,
and every fact is dated Wednesday 25 November 2026 with a named
source — other days' news is labelled in the DATE CHECK box only.
Deterministic: fixed inputs, no randomness, no network.
"""

import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))

from draw_panels import LEAD_DRAW, SMALL_DRAW  # noqa: E402

W, H = 1024, 1024
MX = 24                      # left/right margin
RX = W - MX                  # right edge of the content area
CREAM = (250, 244, 228)
PAPER = (244, 236, 214)
INK = (25, 25, 25)
NAVY = (13, 32, 61)
RED = (178, 34, 34)
GOLD = (232, 176, 44)
BLUE = (40, 90, 160)
TEAL = (0, 128, 128)
GREEN = (60, 140, 70)
ORANGE = (214, 120, 20)
PURPLE = (146, 84, 160)
GREY = (110, 105, 95)
DOT = (120, 105, 85)
LIGHT = (226, 218, 200)
MAP_BG = NAVY
DOT_CAP = (180, 200, 220)
RULE = (160, 150, 130)


def _font(name, size):
    p = "/usr/share/fonts/truetype/dejavu/" + name
    try:
        return ImageFont.truetype(p, size)
    except Exception:
        return ImageFont.load_default()


def serif(size):
    return _font("DejaVuSerif.ttf", size)


def serif_bold(size):
    return _font("DejaVuSerif-Bold.ttf", size)


def bold(size):
    return _font("DejaVuSans-Bold.ttf", size)


def regular(size):
    return _font("DejaVuSans.ttf", size)


# ------------------------------------------------------------------ content
# Leads: (key, banner, dateline, headline, summary, source, tag)
LEADS = [
    ("cartagena", "ALL HOSTAGES FREED",
     "1 CARTAGENA, COLOMBIA · SECURITY",
     "All Cartagena hostages freed after 15-hour siege",
     "Forces stormed an Éxito supermarket on Wednesday, freeing "
     "every hostage after a 15-hour siege that began with a failed "
     "armoured-car robbery; one captor was killed and four detained.",
     "Reuters, AFP", "REPORTED"),
    ("shenzhou", "PAKISTAN'S FIRST IN ORBIT",
     "2 JIUQUAN, CHINA · SPACE",
     "Shenzhou-24 lifts off with Pakistan's first astronaut",
     "China launched Shenzhou-24 at 08:18 on Wednesday, carrying "
     "Muhammad Zeeshan Ali, the first Pakistani in orbit and the "
     "first foreigner aboard the Tiangong station.",
     "Reuters, Nature", "REPORTED"),
    ("solomons", "NO FOREIGN BASES",
     "3 CANBERRA, AUSTRALIA · DIPLOMACY",
     "Solomons signs Australia pact, bars China bases",
     "Solomon Islands signed a security treaty with Australia on "
     "Wednesday, pledging no foreign military base on its soil and "
     "naming Canberra its primary security partner.",
     "AP, CNN", "REPORTED"),
]

# Small stories: (key, banner, dateline, headline, summary, source)
SMALL = [
    ("nikkei", "NIKKEI −2.6%", "4 TOKYO · MARKETS",
     "Nikkei slides as AI rally reverses",
     "Nikkei closed down 2.6% on Wednesday; SoftBank lost 13%.",
     "Reuters"),
    ("seoul", "PROTEST TO MOSCOW", "5 SEOUL · SECURITY",
     "Seoul protests to Moscow over jets",
     "Seoul summoned Russia's attaché after jets entered its zone.",
     "Yonhap, AP"),
    ("ucl", "9 TIES TONIGHT", "6 EUROPE · SPORT",
     "Champions League: 9 ties tonight",
     "Sabah v Barcelona; PSG v Roma; Sporting v Man Utd.",
     "UEFA"),
    ("taipo", "168 KILLED, A YEAR ON", "7 HONG KONG · SOCIETY",
     "Tai Po fire: a year on, answers sought",
     "A year after the fire killed 168, survivors return to Tai Po.",
     "Reuters, HRW"),
    ("bogor", "26 TRAPPED", "8 BOGOR · DISASTER",
     "Rescuers hunt for 26 miners in Bogor",
     "26 unlicensed miners are trapped 100m down in flooded shafts.",
     "Reuters"),
    ("nba", "9 GAMES", "9 USA · SPORT",
     "NBA: 9 games tonight, Cup night",
     "Heat at 76ers (14–3); Spurs at Blazers; Wolves at Thunder.",
     "NBA"),
    ("spain", "VOTE 29 NOV", "10 MADRID · POLITICS",
     "Spain's snap vote: housing on top",
     "Housing dominates the final week before Sunday's snap vote.",
     "Reuters"),
    ("brent", "BRENT $87.49", "11 VIENNA · ENERGY",
     "Oil down 21% in November",
     "Brent crude traded at $87.49, down 21% over the month.",
     "Yahoo Finance"),
    ("sppi", "SPPI +4.2%", "12 TOKYO · ECONOMY",
     "Japan services prices jump 4.2%",
     "Services producer prices rose 4.2% in October, a 1990 high.",
     "RTTNews"),
    ("argentina", "RECESSION", "13 BUENOS AIRES · ECONOMY",
     "Argentina enters technical recession",
     "Argentina's economy entered a technical recession, data showed.",
     "AFP"),
    ("houthi", "REFINERY CLAIM", "14 RAS TANURA · CONFLICT",
     "Houthis claim Ras Tanura refinery hit",
     "Group claims fires at refinery; 4 drones intercepted.",
     "Reuters"),
    ("australia", "CPI 4.9%", "15 SYDNEY · ECONOMY",
     "Australia inflation jumps to 4.9%",
     "CPI rose 4.9% in October, up from 4.3%; power +25.2%.",
     "ABS"),
]

# Numbered ALSO list: (num, region, text, source). Texts are kept short
# so each item stays on one line in its column.
ALSO = [
    (16, "Americas", "30 held at first", "Reuters"),
    (17, "Americas", "10 released, incl. elderly women", "Reuters"),
    (18, "Americas", "1 captor killed, 4 detained", "Reuters"),
    (19, "Americas", "Gang sought $2m ransom", "Reuters"),
    (20, "Asia", "Launch 08:18 from Jiuquan", "Reuters"),
    (21, "Asia", "Docked ~3.5 hours later", "Nature"),
    (22, "Asia", "Ali stays 5–10 days", "Reuters"),
    (23, "Asia", "Tang's 3rd Tiangong trip", "CCTV"),
    (24, "Asia-Pacific", "AU$740m over 10 years", "AP"),
    (25, "Asia-Pacific", "China pact lapses early 2027", "WSJ"),
    (26, "Asia-Pacific", "Treaty needs ratification", "AP"),
    (27, "Asia", "SoftBank −13%, Advantest −13%", "Reuters"),
    (28, "Asia", "Kospi −5.05% to 4,753", "JBizNews"),
    (29, "US", "Nvidia −7% on Tuesday", "Motley Fool"),
    (30, "Asia", "F-15K scrambled; 4 Russian jets", "Yonhap"),
    (31, "Asia", "3rd KADIZ entry in a week", "Yonhap"),
    (32, "Europe", "Sabah v Barcelona 17:45 UTC", "UEFA"),
    (33, "Europe", "PSG v Roma 20:00 UTC", "UEFA"),
    (34, "Asia", "Residents return Thu to mark a year", "Reuters"),
]

# (big number, label) — each label fits one line in its cell.
STATS = [
    ("30", "hostages held in Cartagena"),
    ("1st", "Pakistani in orbit"),
    ("−2.6%", "Nikkei at Wednesday's close"),
    ("9", "Champions League ties tonight"),
    ("26", "miners trapped in Bogor"),
    ("168", "Tai Po dead, a year on"),
]

# (label, story count, colour)
REGIONS = [
    ("ASIA-PACIFIC", 20, ORANGE),
    ("AMERICAS", 8, BLUE),
    ("EUROPE", 4, TEAL),
    ("MIDEAST", 2, PURPLE),
]

# (time, label) — launch 00:18 UTC, docking ~3.5 h later, Nikkei close
# 15:00 JST = 06:00 UTC, UCL 17:45/20:00 UTC, NBA 5pm ET = 22:00 UTC.
TIMELINE = [
    ("00:18", "SHENZHOU"),
    ("03:48", "DOCKING"),
    ("06:00", "NIKKEI CLOSE"),
    ("17:45", "UCL"),
    ("20:00", "UCL NIGHT"),
    ("22:00", "NBA"),
    ("WED", "CARTAGENA"),
    ("WED", "SOLOMONS"),
]

# Map pins: (story number, lat, lon)
PINS = [
    (1, 10.4, -75.5), (2, 40.9, 100.3), (3, -35.3, 149.1),
    (4, 35.7, 139.7), (5, 37.6, 127.0), (6, 48.9, 2.35),
    (7, 22.3, 114.2), (8, -6.6, 106.8), (9, 39.95, -75.16),
    (10, 40.4, -3.7), (11, 48.2, 16.4), (12, 35.7, 139.7),
    (13, -34.6, -58.4), (14, 26.65, 50.16), (15, -33.87, 151.21),
]

TOTAL_STORIES = 3 + len(SMALL) + len(ALSO)


def wrap(d, text, font, width, max_lines=None, what="wrap"):
    """Greedy word wrap. Raises if it cannot fit in max_lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
            if max_lines is not None and len(lines) >= max_lines:
                raise ValueError("wrap overflow (%s): %r" % (what, text))
    if cur:
        lines.append(cur)
    if max_lines is not None and len(lines) > max_lines:
        raise ValueError("wrap overflow (%s): %r" % (what, text))
    return lines


def check_fit(d, text, font, width, what):
    if d.textlength(text, font=font) > width:
        raise ValueError("does not fit (%s): %r" % (what, text))


# Land polygons: Natural Earth 110m land, simplified with Douglas-Peucker
# (tolerance 1.5 deg, coordinates rounded to 1 decimal), 5 polygons
# below latitude -58 dropped (Antarctica). 70 polygons, 583 points.
# Drawn filled with DOT on the map; no country borders are shown.
# Coordinates are (lon, lat) pairs, taken from the 24 Nov entry's map.
LAND_POLYS = [[(-67.8, -53.9), (-65.0, -54.7), (-69.2, -55.5), (-74.7, -52.8), (-68.2, -53.1)], [(70.3, -49.7), (68.9, -48.6), (70.6, -49.3)], [(145.4, -40.8), (148.3, -40.9), (146.1, -43.5), (144.7, -40.7)], [(173.0, -40.9), (170.6, -45.9), (166.7, -46.2), (172.8, -40.5)], [(174.6, -36.2), (178.5, -37.7), (175.2, -41.7), (172.6, -34.5), (174.3, -35.3)], [(50.1, -13.6), (47.1, -24.9), (43.8, -24.5), (44.5, -16.2), (49.8, -12.9)], [(143.6, -13.8), (153.6, -28.1), (150.0, -37.4), (146.3, -39.0), (140.6, -38.0), (138.2, -34.4), (136.8, -35.3), (137.8, -32.9), (136.0, -34.9), (131.3, -31.5), (116.6, -35.0), (113.4, -24.4), (114.2, -21.8), (120.9, -19.7), (125.7, -14.2), (129.6, -15.0), (131.8, -11.3), (136.5, -11.9), (135.5, -15.0), (140.2, -17.7), (142.1, -11.0), (143.6, -13.4)], [(120.7, -10.2), (119.0, -9.6), (120.8, -10.0)], [(108.6, -6.8), (115.7, -8.4), (108.5, -6.4)], [(155.9, -6.8), (154.5, -5.1), (156.0, -6.5)], [(152.0, -5.5), (148.4, -5.4), (152.3, -4.9)], [(153.1, -4.5), (150.7, -2.7), (153.0, -4.0)], [(134.1, -1.1), (135.5, -3.4), (138.3, -1.7), (144.6, -3.9), (150.8, -10.3), (144.7, -7.6), (137.6, -8.4), (137.9, -5.4), (130.5, -0.9), (134.0, -0.8)], [(125.2, 1.4), (120.2, 0.2), (123.3, -0.6), (121.5, -1.9), (123.2, -5.3), (121.0, -2.6), (119.4, -5.4), (120.0, 0.6), (125.1, 1.6)], [(105.8, -5.8), (95.3, 5.5), (102.5, 1.4), (105.9, -4.3)], [(117.9, 1.8), (114.9, -4.1), (110.2, -2.9), (109.1, 1.3), (116.7, 6.9), (119.2, 5.4), (118.0, 2.3)], [(126.4, 8.4), (125.4, 5.6), (121.9, 7.2), (126.3, 8.8)], [(81.2, 6.2), (80.2, 9.8), (81.6, 6.5)], [(124.0, 10.3), (122.4, 9.7), (124.1, 11.2)], [(125.5, 12.2), (124.8, 10.1), (125.2, 12.5)], [(121.3, 18.5), (124.1, 12.5), (120.6, 13.9), (120.7, 18.5)], [(-72.6, 19.9), (-68.3, 18.6), (-71.4, 17.6), (-74.5, 18.3), (-73.2, 19.9)], [(110.3, 18.7), (108.6, 19.4), (110.6, 19.3)], [(-79.7, 22.8), (-75.0, 19.9), (-85.0, 21.9), (-80.6, 23.1)], [(134.6, 34.1), (133.0, 32.7), (133.9, 34.4)], [(23.7, 35.7), (26.2, 35.0), (23.5, 35.3)], [(15.5, 38.2), (15.1, 36.6), (12.4, 37.6), (14.8, 38.1)], [(9.2, 41.2), (9.7, 39.2), (8.7, 40.9)], [(141.0, 37.1), (135.8, 33.5), (131.0, 33.9), (130.7, 31.0), (129.4, 33.3), (139.4, 38.2), (140.3, 41.2), (141.0, 38.2)], [(143.9, 44.2), (145.5, 43.3), (140.0, 41.6), (142.0, 45.5), (143.1, 44.5)], [(-61.8, 49.1), (-64.5, 49.9), (-61.8, 49.3)], [(-123.5, 48.5), (-128.1, 50.0), (-123.9, 49.1)], [(-56.1, 50.7), (-53.1, 46.7), (-59.3, 47.6), (-55.6, 51.3)], [(143.7, 50.8), (142.1, 46.0), (141.7, 53.3), (143.2, 51.8)], [(-6.8, 52.3), (-10.0, 51.8), (-9.7, 53.9), (-6.7, 55.2), (-6.0, 53.1)], [(12.7, 55.6), (11.0, 55.4), (12.4, 56.1)], [(-3.0, 58.6), (1.4, 51.3), (-5.2, 50.0), (-3.0, 54.0), (-6.2, 56.8), (-4.2, 58.5)], [(-165.6, 59.9), (-167.5, 60.2), (-165.7, 60.3)], [(-81.9, 62.7), (-84.0, 62.5), (-81.9, 62.9)], [(-171.7, 63.8), (-168.7, 63.3), (-171.8, 63.4)], [(-85.2, 65.7), (-80.1, 63.7), (-85.5, 63.0), (-87.2, 63.5), (-85.9, 65.7)], [(-14.5, 66.5), (-13.6, 65.1), (-18.7, 63.5), (-24.3, 65.6), (-16.2, 66.5)], [(-175.0, 66.6), (-169.9, 66.0), (-173.0, 64.2), (-180.0, 65.0), (-180.0, 69.0), (-174.9, 67.2)], [(-95.7, 69.1), (-99.8, 69.4), (-96.3, 69.5)], [(-90.5, 69.5), (-87.3, 67.2), (-85.5, 69.9), (-82.6, 69.7), (-81.3, 67.6), (-93.2, 62.0), (-94.7, 59.0), (-92.3, 57.1), (-82.3, 55.1), (-79.9, 51.2), (-79.8, 54.7), (-76.5, 56.5), (-78.1, 62.3), (-73.8, 62.4), (-67.7, 58.2), (-64.6, 60.3), (-55.7, 52.1), (-66.4, 50.2), (-71.1, 46.8), (-65.1, 49.2), (-64.5, 46.2), (-59.8, 45.9), (-65.4, 43.5), (-64.4, 45.3), (-67.1, 45.1), (-75.9, 37.2), (-76.3, 39.1), (-75.7, 35.5), (-81.3, 31.4), (-80.4, 25.2), (-84.1, 30.1), (-96.6, 28.3), (-96.3, 19.3), (-92.0, 18.7), (-87.0, 21.5), (-88.9, 15.9), (-83.4, 15.3), (-83.8, 11.1), (-81.4, 8.8), (-76.8, 8.6), (-71.8, 12.4), (-71.7, 9.1), (-69.9, 12.2), (-61.9, 10.7), (-57.1, 6.0), (-51.3, 4.2), (-50.4, -0.1), (-40.0, -2.9), (-34.7, -7.3), (-40.9, -21.9), (-47.6, -24.9), (-53.8, -34.4), (-58.4, -33.9), (-56.8, -36.9), (-65.1, -41.1), (-63.5, -42.6), (-67.3, -45.5), (-66.0, -48.1), (-71.4, -53.9), (-75.0, -52.3), (-75.6, -46.6), (-72.7, -42.4), (-74.3, -43.2), (-70.2, -19.8), (-81.2, -6.1), (-80.9, -1.1), (-77.1, 3.9), (-78.2, 8.3), (-80.9, 7.2), (-87.5, 13.3), (-103.5, 18.3), (-113.9, 31.6), (-110.0, 22.8), (-124.4, 40.3), (-124.7, 48.2), (-122.6, 47.1), (-122.8, 49.0), (-134.1, 58.1), (-147.1, 60.9), (-151.7, 59.2), (-150.6, 61.3), (-164.8, 54.4), (-157.0, 58.9), (-162.0, 58.7), (-166.1, 61.5), (-160.8, 64.8), (-168.1, 65.7), (-161.7, 66.1), (-166.8, 68.4), (-156.6, 71.4), (-108.9, 67.4), (-96.1, 67.3), (-94.2, 69.1), (-96.5, 70.1), (-95.2, 71.9), (-92.4, 69.7)], [(-114.2, 73.1), (-106.5, 73.1), (-101.0, 70.0), (-113.3, 68.5), (-117.3, 70.0), (-112.4, 70.4), (-119.4, 71.6), (-115.2, 73.3)], [(-86.6, 73.2), (-67.9, 70.1), (-68.8, 68.7), (-61.9, 66.9), (-63.9, 65.0), (-68.0, 66.3), (-65.0, 62.7), (-78.6, 64.6), (-72.9, 67.7), (-89.5, 70.8), (-89.4, 73.1), (-85.8, 73.8)], [(-100.4, 73.8), (-96.7, 71.7), (-101.5, 73.4)], [(143.6, 73.2), (139.9, 73.4), (143.5, 73.5)], [(-93.2, 72.8), (-95.4, 72.1), (-94.5, 74.1), (-92.0, 73.0)], [(-120.5, 71.4), (-125.9, 71.9), (-124.9, 74.3), (-121.5, 74.5), (-115.5, 73.5), (-120.5, 71.8)], [(-93.6, 75.0), (-96.8, 74.9), (-94.0, 75.3)], [(145.1, 75.6), (139.0, 74.6), (137.5, 76.0), (141.5, 76.1)], [(-98.5, 76.7), (-98.2, 75.0), (-102.6, 76.3), (-98.6, 76.6)], [(-108.2, 76.2), (-117.7, 75.2), (-108.5, 76.7)], [(57.5, 70.7), (51.6, 71.5), (55.6, 75.1), (68.2, 76.9), (55.6, 71.5)], [(-94.7, 77.1), (-80.1, 75.3), (-88.2, 74.4), (-96.8, 77.2)], [(107.0, 77.0), (114.1, 75.8), (109.4, 74.2), (127.0, 73.6), (131.3, 70.8), (140.5, 72.8), (160.9, 69.4), (178.6, 69.4), (180.0, 65.0), (177.4, 64.6), (179.5, 62.6), (163.5, 59.9), (162.1, 54.9), (156.8, 51.0), (155.9, 56.8), (164.5, 62.5), (156.7, 61.4), (155.0, 59.1), (142.2, 59.0), (135.1, 54.7), (141.4, 52.2), (138.2, 46.3), (127.5, 39.8), (129.1, 35.1), (126.5, 34.4), (125.3, 39.5), (121.0, 38.9), (121.6, 41.0), (118.0, 39.2), (122.4, 37.5), (119.2, 34.9), (121.7, 28.2), (115.9, 22.8), (105.9, 19.8), (109.3, 13.4), (105.2, 8.6), (100.1, 13.4), (99.2, 9.2), (104.2, 1.3), (98.3, 7.8), (97.2, 16.9), (94.2, 16.0), (91.4, 22.8), (80.3, 15.9), (77.5, 8.0), (72.6, 21.4), (70.5, 20.9), (66.4, 25.4), (57.4, 25.7), (48.0, 30.0), (51.8, 24.0), (56.4, 26.4), (59.8, 22.3), (55.3, 17.2), (43.5, 12.6), (34.9, 29.5), (33.9, 27.6), (32.4, 29.9), (42.7, 11.7), (51.0, 10.6), (39.2, -4.7), (40.8, -14.7), (34.8, -19.8), (35.5, -24.1), (28.2, -32.8), (19.6, -34.8), (11.8, -18.1), (13.7, -10.7), (8.8, -1.1), (9.4, 3.7), (4.3, 6.3), (-9.0, 4.8), (-16.6, 12.2), (-17.0, 21.9), (-5.9, 35.8), (9.5, 37.4), (10.3, 33.8), (19.1, 30.3), (21.5, 32.8), (33.8, 31.0), (36.2, 36.6), (27.6, 36.7), (26.2, 39.5), (41.7, 42.0), (36.7, 45.2), (39.1, 47.3), (33.9, 44.4), (30.8, 46.6), (27.7, 42.6), (28.8, 41.0), (22.6, 40.3), (24.0, 37.7), (22.5, 36.4), (19.5, 41.7), (13.1, 45.7), (12.6, 44.1), (18.5, 40.2), (16.1, 38.0), (8.9, 44.4), (3.1, 43.1), (-2.1, 36.7), (-8.9, 36.9), (-9.4, 43.0), (-1.4, 44.0), (-4.6, 48.7), (8.1, 53.5), (8.5, 57.1), (10.6, 57.7), (10.9, 54.0), (19.7, 54.4), (21.6, 57.4), (24.1, 57.0), (23.3, 59.2), (29.1, 60.0), (21.3, 60.7), (21.5, 63.2), (25.4, 65.1), (22.2, 65.7), (17.9, 62.8), (18.8, 60.1), (15.9, 56.1), (12.9, 55.4), (10.4, 59.5), (5.7, 58.6), (5.0, 62.0), (24.6, 71.0), (40.3, 67.9), (40.0, 66.3), (33.2, 66.6), (37.0, 63.9), (44.0, 66.1), (43.5, 68.6), (46.4, 66.7), (60.5, 69.8), (68.5, 68.1), (66.7, 71.0), (72.6, 72.8), (72.4, 66.2), (75.0, 67.8), (73.1, 71.5), (74.7, 72.8), (81.5, 71.8), (80.5, 73.7), (104.7, 77.1)], [(49.1, 41.3), (49.2, 37.6), (53.8, 37.0), (52.7, 40.0), (54.7, 41.0), (50.3, 44.6), (53.0, 46.9), (46.7, 44.6), (48.6, 41.8)], [(-93.8, 77.5), (-96.4, 77.8), (-93.7, 77.6)], [(-110.2, 77.7), (-113.5, 77.7), (-109.8, 78.0)], [(-95.8, 78.1), (-98.6, 78.9), (-95.6, 78.4)], [(-100.1, 78.3), (-105.2, 78.4), (-100.8, 78.8)], [(105.1, 78.3), (99.4, 77.9), (105.4, 78.7)], [(18.2, 79.7), (21.5, 79.0), (15.9, 76.8), (10.4, 79.7), (17.0, 80.0)], [(51.1, 80.5), (44.9, 80.6), (51.5, 80.7)], [(99.9, 78.9), (91.2, 80.3), (100.2, 79.8)], [(-87.0, 79.7), (-90.8, 78.2), (-96.7, 80.2), (-87.8, 80.3)], [(-68.5, 83.1), (-61.9, 82.4), (-76.9, 79.3), (-75.4, 78.5), (-79.8, 77.2), (-77.9, 76.8), (-86.1, 76.3), (-89.6, 77.0), (-85.0, 77.5), (-88.0, 78.4), (-85.1, 79.3), (-86.9, 80.2), (-81.8, 80.5), (-91.6, 81.9), (-70.7, 83.2)], [(-27.1, 83.5), (-20.9, 82.7), (-31.4, 82.0), (-12.2, 81.3), (-20.1, 80.2), (-17.7, 80.1), (-19.7, 78.8), (-18.5, 77.0), (-21.7, 76.6), (-19.4, 74.3), (-24.8, 72.3), (-21.8, 70.7), (-26.4, 70.2), (-22.4, 70.1), (-39.8, 65.5), (-44.8, 60.0), (-51.6, 63.6), (-54.0, 67.2), (-50.9, 69.9), (-54.7, 69.6), (-51.4, 70.6), (-55.8, 71.7), (-57.3, 74.7), (-73.2, 78.4), (-62.6, 81.8), (-35.1, 83.7)]]


# ------------------------------------------------------------------ render
def render():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    MX = 24
    RX = W - MX

    # ---------- top navy banner ----------
    d.rectangle([0, 0, W, 20], fill=NAVY)
    d.text((MX, 4), "THE WORLD IN ONE DAY", font=bold(11), fill=(255, 255, 255))
    banner_r = ("34 STORIES  ·  4 REGIONS  ·  EVERY ONE DATED "
                "WEDNESDAY 25 NOVEMBER 2026")
    check_fit(d, banner_r, bold(10), RX - 200, "top banner right")
    d.text((RX, 5), banner_r, font=bold(10), fill=(180, 200, 220), anchor="ra")

    # ---------- masthead ----------
    title = "Wednesday 25 November 2026"
    check_fit(d, title, serif_bold(44), W - 48, "masthead title")
    d.text((W // 2, 24), title, font=serif_bold(44), fill=NAVY, anchor="ma")
    stand = ("Hostages freed in Cartagena  ·  Shenzhou-24 lifts off"
             "  ·  Solomons signs Australia pact")
    check_fit(d, stand, serif(13), W - 48, "standfirst")
    d.text((W // 2, 72), stand, font=serif(13), fill=RED, anchor="ma")
    d.line([MX, 88, RX, 88], fill=NAVY, width=1)

    # ---------- six-number stats row, labelled THE DAY IN NUMBERS ----------
    # The label takes a 64px strip at the left (two lines, bold 9);
    # the six cells share the rest. Longest label is 140px at 9pt,
    # cells are 152px wide, wrapped at cell_w - 8 = 144px: fits.
    d.text((MX, 102), "THE DAY", font=bold(9), fill=NAVY)
    d.text((MX, 114), "IN NUMBERS", font=bold(9), fill=NAVY)
    stats_x0 = MX + 64
    cell_w = (RX - stats_x0) / 6
    for i, (num, label) in enumerate(STATS):
        cx = stats_x0 + cell_w * i + cell_w / 2
        check_fit(d, num, serif_bold(26), cell_w - 8, "stat number")
        d.text((cx, 92), num, font=serif_bold(26), fill=RED, anchor="ma")
        lines = wrap(d, label, regular(9), cell_w - 8, 1, "stat label")
        ly = 122
        for ln in lines:
            d.text((cx, ly), ln, font=regular(9), fill=GREY, anchor="ma")
            ly += 11
    d.line([MX, 136, RX, 136], fill=RULE, width=1)

    # ---------- colour region bar ----------
    total = sum(n for _, n, _ in REGIONS)
    widths = [max(int(n / total * (RX - MX)), 70) for _, n, _ in REGIONS]
    widths[0] -= sum(widths) - (RX - MX)   # absorb rounding into first
    x = MX
    for (label, _n, color), wseg in zip(REGIONS, widths):
        d.rectangle([x, 140, x + wseg, 156], fill=color)
        check_fit(d, label, bold(10), wseg - 8, "region label")
        d.text((x + wseg / 2, 145), label, font=bold(10),
               fill=(255, 255, 255), anchor="ma")
        x += wseg

    # ---------- UTC timeline strip ----------
    d.rectangle([MX, 160, RX, 180], fill=NAVY)
    d.text((MX + 8, 166), "THE DAY IN UTC", font=bold(10),
           fill=(255, 210, 90))
    seg = (RX - MX - 150) / len(TIMELINE)
    for i, (t, label) in enumerate(TIMELINE):
        cx = MX + 150 + seg * i + seg / 2
        tw = d.textlength(t, font=bold(10))
        lw = d.textlength(label, font=regular(9))
        gx = cx - (tw + 4 + lw) / 2
        d.text((gx, 166), t, font=bold(10), fill=(255, 170, 110))
        d.text((gx + tw + 4, 166), label, font=regular(9),
               fill=(255, 255, 255))

    # ---------- 3 lead stories with code-drawn illustrations ----------
    lead_w = 317
    lead_x = [MX, MX + lead_w + 12, MX + 2 * (lead_w + 12)]
    lead_y, photo_h = 188, 148
    for i, (kind, banner, dateline, head, summ, src, tag) in enumerate(LEADS):
        x = lead_x[i]
        img.paste(LEAD_DRAW[kind](), (x, lead_y))
        bw = d.textlength(banner, font=bold(10)) + 14
        d.rectangle([x, lead_y, x + bw, lead_y + 18], fill=RED)
        d.text((x + 7, lead_y + 4), banner, font=bold(10),
               fill=(255, 255, 255))
        dy = lead_y + photo_h + 8
        d.text((x, dy), dateline, font=bold(10), fill=RED)
        tw = d.textlength(tag, font=bold(9))
        d.rectangle([x + lead_w - tw - 14, dy + 1, x + lead_w - tw - 6, dy + 9],
                    outline=RED, width=1)
        d.line([x + lead_w - tw - 13, dy + 5, x + lead_w - tw - 10, dy + 8],
               fill=RED, width=1)
        d.line([x + lead_w - tw - 10, dy + 8, x + lead_w - tw - 7, dy + 3],
               fill=RED, width=1)
        d.text((x + lead_w, dy), tag, font=bold(9), fill=RED, anchor="ra")
        hy = dy + 16
        for ln in wrap(d, head, serif_bold(19), lead_w, 2, "lead headline"):
            d.text((x, hy), ln, font=serif_bold(19), fill=INK)
            hy += 22
        sy = hy + 4
        for ln in wrap(d, summ, regular(11), lead_w, 4, "lead summary"):
            d.text((x, sy), ln, font=regular(11), fill=INK)
            sy += 14
        d.text((x, sy + 2), "(" + src + ")", font=regular(10), fill=GREY)

    # ---------- 12 small stories: code-drawn illustration + banner ----------
    small_w = 156
    small_x = [MX + i * (small_w + 8) for i in range(6)]
    row_y = [480, 592]
    for r, row in enumerate((SMALL[:6], SMALL[6:])):
        y0 = row_y[r]
        for c, (key, banner, dateline, head, summ, src) in enumerate(row):
            x = small_x[c]
            img.paste(SMALL_DRAW[key](), (x, y0))
            bw = d.textlength(banner, font=bold(9)) + 10
            if bw > small_w:
                raise ValueError("OVERFLOW small banner: %r" % banner)
            d.rectangle([x, y0, x + bw, y0 + 14], fill=RED)
            d.text((x + 5, y0 + 3), banner, font=bold(9),
                   fill=(255, 255, 255))
            dy = y0 + 43
            d.text((x, dy), dateline, font=bold(9), fill=RED)
            hy = dy + 12
            for ln in wrap(d, head, bold(11), small_w, 2, "small headline"):
                d.text((x, hy), ln, font=bold(11), fill=INK)
                hy += 13
            sy = hy + 1
            for ln in wrap(d, summ, regular(9), small_w, 2, "small summary"):
                d.text((x, sy), ln, font=regular(9), fill=INK)
                sy += 10
            d.text((x, sy + 1), "(" + src + ")", font=regular(8), fill=GREY)
    small_bottom = row_y[1] + 40 + 3 + 12 + 2 * 13 + 1 + 2 * 10 + 1 + 8
    if small_bottom > 712:
        raise ValueError("SMALL ROWS OVERFLOW: bottom %d" % small_bottom)

    # ---------- bottom: map (left) + ALSO list (right) ----------
    bot_y = 716
    map_x, map_w, map_h = MX, 330, 232
    d.rectangle([map_x, bot_y, map_x + map_w, bot_y + map_h], fill=MAP_BG)
    d.text((map_x + 10, bot_y + 8), "WHERE IT HAPPENED",
           font=bold(11), fill=(255, 255, 255))
    d.text((map_x + 10, bot_y + 24), "pins match story numbers",
           font=regular(9), fill=DOT_CAP)
    dot_x0, dot_y0 = map_x + 8, bot_y + 44
    dot_w, dot_h = map_w - 16, 124
    lat_top, lat_bot = 78.0, -58.0

    def to_xy(lat, lon):
        px = dot_x0 + (lon + 180.0) / 360.0 * dot_w
        py = dot_y0 + (lat_top - lat) / (lat_top - lat_bot) * dot_h
        return px, py

    for poly in LAND_POLYS:
        xy = [to_xy(lat, lon) for lon, lat in poly]
        d.polygon(xy, fill=DOT)
    placed = []
    for num, lat, lon in PINS:
        tx, ty = to_xy(lat, lon)
        cx, cy = tx, ty
        # Spread crowded pins (Europe + the two Tokyo pins share a spot):
        # try larger offsets, keep the pin inside the map plot, and keep
        # 15px from every pin placed before it.
        for ox, oy in [(0, -15), (15, 0), (0, 15), (-15, 0), (15, -15),
                       (-15, -15), (15, 15), (-15, 15), (0, -30),
                       (30, 0), (0, 30), (-30, 0), (30, -30), (-30, -30),
                       (30, 30), (-30, 30), (0, -45), (45, 0), (-45, 0),
                       (0, 45)]:
            nx, ny = tx + ox, ty + oy
            if not (dot_x0 + 8 <= nx <= dot_x0 + dot_w - 8
                    and dot_y0 + 8 <= ny <= dot_y0 + dot_h - 8):
                continue
            ok = True
            for px, py in placed:
                if math.hypot(nx - px, ny - py) < 15:
                    ok = False
                    break
            if ok:
                cx, cy = nx, ny
                break
        if (cx, cy) != (tx, ty):
            d.line([tx, ty, cx, cy], fill=(255, 255, 255), width=1)
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6],
                  fill=RED, outline=(255, 255, 255), width=1)
        d.text((cx, cy - 4), str(num), font=bold(8), fill=(255, 255, 255),
               anchor="ma")
        placed.append((cx, cy))
    d.text((map_x + 10, bot_y + map_h - 22),
           "1 Cartagena · 2 Jiuquan · 3 Canberra · 15 Sydney",
           font=regular(9), fill=DOT_CAP)

    # ALSO list, two columns
    ax = [370, 693]
    col_w = 307
    d.text((ax[0], bot_y), "ALSO ON WEDNESDAY 25 NOVEMBER — 19 MORE STORIES",
           font=bold(12), fill=NAVY)
    d.line([ax[0], bot_y + 18, RX, bot_y + 18], fill=NAVY, width=1)
    list_y = bot_y + 26
    for ci, items in enumerate((ALSO[:10], ALSO[10:])):
        x = ax[ci]
        y = list_y
        for num, region, text, src in items:
            line = "%d %s: %s (%s)" % (num, region, text, src)
            lines = wrap(d, line, regular(9), col_w, 2, "also item")
            for j, ln in enumerate(lines):
                if j == 0:
                    head_w = d.textlength("%d %s: " % (num, region),
                                          font=bold(9))
                    d.text((x, y), "%d %s: " % (num, region), font=bold(9),
                           fill=NAVY)
                    d.text((x + head_w, y),
                           ln[len("%d %s: " % (num, region)):],
                           font=regular(9), fill=INK)
                else:
                    d.text((x, y), ln, font=regular(9), fill=INK)
                y += 13
        if y > bot_y + map_h + 2:
            raise ValueError("ALSO COLUMN %d OVERFLOW: bottom %d" % (ci, y))

    # ---------- DATE CHECK box ----------
    dc_text = ("Not today: Senegal AFCON title back (Tue) · Ulleung jet "
               "alert (Tue) · Nikkei +3.9% (Tue) · Venezuela debt $237.5bn "
               "(Tue) · Democrats reach 259 seats (Tue) · Chen Jining "
               "probe (Tue) · DR Congo plane down (Sun) · Iran flogs "
               "singer (Mon) · Zambia treason charge (Mon) · Pentagon "
               "faults Canada (Mon).")
    dc_lines = wrap(d, dc_text, regular(10), RX - MX - 8 - 96, 2, "date check")
    # Box height follows the wrapped line count, so the bottom border
    # never cuts through the last line of text.
    dc_y = 950
    dc_h = 8 + len(dc_lines) * 11 + 8
    d.rectangle([MX, dc_y, RX, dc_y + dc_h], outline=RED, width=2)
    d.text((MX + 8, dc_y + 8), "DATE CHECK", font=bold(10), fill=RED)
    ly = dc_y + 8
    for ln in dc_lines:
        d.text((MX + 96, ly), ln, font=regular(10), fill=INK)
        ly += 11

    # ---------- footer ----------
    foot1 = ("Sources: Reuters, AFP, AP, CNN, Yonhap, UEFA, NBA, HRW, "
             "Nature, RTTNews, CCTV, WSJ, JBizmNews, Yahoo Finance, "
             "Motley Fool, ABS.")
    check_fit(d, foot1, regular(9), W - 48, "footer sources")
    d.text((W // 2, 990), foot1, font=regular(9), fill=GREY, anchor="ma")
    foot2 = ("CERTAINTY: REPORTED = carried by the day's wires · CLAIM = one "
             "side's account · FORECAST = still to happen when drawn · "
             "Illustrations and map drawn in code")
    check_fit(d, foot2, regular(9), W - 48, "footer legend")
    d.text((W // 2, 1002), foot2, font=regular(9), fill=GREY, anchor="ma")
    d.rectangle([0, 1014, W, 1024], fill=NAVY)
    d.text((MX, 1016), "THE WORLD IN ONE DAY", font=bold(9),
           fill=(255, 255, 255))
    d.text((RX, 1016), "WEDNESDAY 25 NOVEMBER 2026 · ONE PAGE", font=bold(9),
           fill=(180, 200, 220), anchor="ra")
    return img


if __name__ == "__main__":
    out = render()
    out_path = os.environ.get("GEN_OUT", os.path.join(HERE, "entry.png"))
    out.save(out_path, optimize=True)
    print("saved", out_path, out.size, "stories:", TOTAL_STORIES)
