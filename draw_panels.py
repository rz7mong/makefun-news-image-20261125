"""Code-drawn flat-vector illustrations for the 25 Nov 2026 front page.

Every panel is drawn with PIL primitives only (rectangles, ellipses,
polygons, lines) — no photos, no AI image generation, no gradients,
no text inside the illustrations. Deterministic: fixed coordinates,
no randomness, no network. Palette matches the page: cream paper,
navy, red, gold, teal, orange, blue, green.

Lead panels are 317x148; small-story panels are 156x40 (wide, short
bands — each scene is one bold symbol on a flat background).

Lead lesson from 24 Nov v3 (round 1: 2642/7302): the three lead
panels carry the page, so they are drawn big, dense and dramatic —
a night rescue with helicopter searchlight and a lit supermarket,
a large rocket launch with flame, smoke and gantry, and a treaty
scene with two national flags and a handshake. No small, diagram-like
subjects.
"""

import math

from PIL import Image, ImageDraw

CREAM = (250, 244, 228)
NAVY = (13, 32, 61)
SKY = (20, 48, 88)
SEA = (16, 48, 84)
DARK = (8, 20, 40)
RED = (178, 34, 34)
GOLD = (232, 176, 44)
GOLD_D = (210, 150, 30)
TEAL = (0, 128, 128)
TEAL_D = (0, 96, 104)
ORANGE = (214, 120, 20)
ORANGE_R = (220, 80, 30)
BLUE = (40, 90, 160)
GREEN = (60, 140, 70)
GREEN_D = (34, 100, 52)
BROWN = (122, 72, 32)
WHITE = (255, 255, 255)
INK = (25, 25, 25)
PALE = (255, 214, 110)
BUILD = (238, 232, 214)
BUILD_D = (216, 208, 186)


def _star(d, cx, cy, r, color):
    """Small 4-point star."""
    q = max(1, int(r * 0.28))
    d.polygon([(cx, cy - r), (cx + q, cy - q), (cx + r, cy),
               (cx + q, cy + q), (cx, cy + r), (cx - q, cy + q),
               (cx - r, cy), (cx - q, cy - q)], fill=color)


def _arrow(d, x0, y0, x1, y1, width, color):
    """Thick arrow from (x0, y0) to (x1, y1) with a head."""
    d.line([(x0, y0), (x1, y1)], fill=color, width=width)
    dx, dy = x1 - x0, y1 - y0
    ln = math.hypot(dx, dy)
    ux, uy = dx / ln, dy / ln
    px, py = -uy, ux
    bx, by = x1 - 26 * ux, y1 - 26 * uy
    hw = 13
    d.polygon([(x1 + 6 * ux, y1 + 6 * uy),
               (bx + hw * px, by + hw * py),
               (bx - hw * px, by - hw * py)], fill=color)


def _jet(d, x, y, s, color):
    """Small jet silhouette pointing right, length s, top at (x, y)."""
    d.polygon([(x, y + 3), (x + 0.6 * s, y), (x + s, y + 5),
               (x + 0.6 * s, y + 9), (x, y + 7)], fill=color,
              outline=NAVY)
    d.polygon([(x + 0.45 * s, y + 7), (x + 0.75 * s, y + 6),
               (x + 0.85 * s, y + 16)], fill=color, outline=NAVY)
    d.polygon([(x + 0.05 * s, y + 6), (x + 0.15 * s, y - 6),
               (x + 0.25 * s, y + 5)], fill=color, outline=NAVY)
    d.ellipse([x + 0.78 * s, y + 2, x + 0.88 * s, y + 6], fill=NAVY)


def _ball(d, cx, cy, r):
    """Soccer ball: white circle, black centre pentagon, small patches."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE,
              outline=INK, width=1)
    pts = []
    for k in range(5):
        a = math.radians(-90 + k * 72)
        pts.append((cx + 0.38 * r * math.cos(a),
                    cy + 0.38 * r * math.sin(a)))
    d.polygon(pts, fill=INK)
    for (px, py) in [(cx - r, cy - 2), (cx + r, cy - 2), (cx, cy + r)]:
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=INK)


# ------------------------------------------------------------------ leads
def lead_cartagena():
    """Night rescue: lit supermarket, helicopter searchlight, people
    leaving, police light bars (317x148)."""
    img = Image.new("RGB", (317, 148), NAVY)
    d = ImageDraw.Draw(img)
    # stars
    for (sx, sy, r, c) in [(90, 12, 3, WHITE), (130, 26, 2, GOLD),
                           (200, 10, 3, WHITE), (240, 28, 2, WHITE),
                           (290, 14, 3, GOLD), (160, 34, 2, WHITE),
                           (110, 40, 2, WHITE), (270, 44, 2, WHITE)]:
        _star(d, sx, sy, r, c)
    # helicopter, top-left below the banner, cream body so it reads
    # against the night sky; narrow searchlight cone with a bright
    # core to the street
    d.ellipse([14, 26, 58, 44], fill=CREAM, outline=NAVY)
    d.polygon([(58, 32), (76, 28), (76, 36)], fill=CREAM, outline=NAVY)
    d.line([(8, 24), (64, 24)], fill=CREAM, width=3)
    d.line([(20, 44), (52, 44)], fill=CREAM, width=2)
    d.ellipse([30, 32, 40, 42], fill=GOLD, outline=NAVY)
    d.polygon([(36, 44), (20, 132), (52, 132)], fill=PALE)
    d.polygon([(36, 44), (28, 132), (44, 132)], fill=(255, 240, 190))
    # supermarket: big gold block, red sign band, glowing windows
    d.rectangle([76, 58, 304, 148], fill=GOLD)
    d.rectangle([76, 58, 304, 74], fill=RED)
    for wx in (88, 116, 144, 172, 200, 228, 256):
        d.rectangle([wx, 82, wx + 20, 102], fill=PALE)
        d.rectangle([wx, 108, wx + 20, 122], fill=PALE)
    # glass doors, light spilling out
    d.rectangle([172, 108, 204, 148], fill=(255, 236, 170))
    d.line([(188, 108), (188, 148)], fill=NAVY, width=2)
    # street
    d.rectangle([0, 132, 317, 148], fill=DARK)
    # three people leaving, arms raised
    for (fx, fy) in [(160, 130), (188, 132), (216, 130)]:
        d.ellipse([fx - 3, fy - 12, fx + 3, fy - 6], fill=CREAM)
        d.polygon([(fx - 4, fy - 6), (fx + 4, fy - 6),
                   (fx + 5, fy + 6), (fx - 5, fy + 6)], fill=CREAM)
        d.line([(fx - 4, fy - 4), (fx - 9, fy - 10)], fill=CREAM, width=2)
        d.line([(fx + 4, fy - 4), (fx + 9, fy - 10)], fill=CREAM, width=2)
    # police light bars, bottom right
    d.rectangle([252, 136, 264, 142], fill=RED)
    d.rectangle([268, 136, 280, 142], fill=BLUE)
    d.rectangle([284, 136, 296, 142], fill=RED)
    return img


def lead_shenzhou():
    """Dawn rocket launch: big white rocket, flame plume, smoke,
    gantry tower, Tiangong station (317x148)."""
    img = Image.new("RGB", (317, 148), NAVY)
    d = ImageDraw.Draw(img)
    # stars + gold sun, top-left
    for (sx, sy, r) in [(24, 52, 2), (60, 70, 2), (100, 44, 2),
                        (240, 60, 2), (290, 70, 2), (130, 12, 2)]:
        _star(d, sx, sy, r, WHITE)
    d.ellipse([18, 14, 40, 36], fill=GOLD)
    # dawn horizon bands
    d.rectangle([0, 96, 317, 112], fill=(30, 60, 110))
    d.rectangle([0, 112, 317, 122], fill=GOLD_D)
    d.rectangle([0, 122, 317, 148], fill=DARK)
    # gantry tower, left
    d.line([(86, 30), (86, 122)], fill=(120, 120, 120), width=4)
    d.line([(104, 30), (104, 122)], fill=(120, 120, 120), width=4)
    for y in (44, 62, 80, 98):
        d.line([(86, y), (104, y)], fill=(120, 120, 120), width=3)
        d.line([(86, y), (104, y + 18)], fill=(120, 120, 120), width=2)
    d.line([(104, 52), (140, 52)], fill=(120, 120, 120), width=3)
    # side boosters
    d.rectangle([150, 62, 164, 116], fill=WHITE)
    d.rectangle([196, 62, 210, 116], fill=WHITE)
    d.polygon([(150, 62), (157, 50), (164, 62)], fill=RED)
    d.polygon([(196, 62), (203, 50), (210, 62)], fill=RED)
    # core body, red nose cone, red band, engine band
    d.rectangle([166, 18, 194, 116], fill=WHITE)
    d.polygon([(166, 18), (180, 4), (194, 18)], fill=RED)
    d.rectangle([166, 40, 194, 50], fill=RED)
    d.rectangle([166, 96, 194, 104], fill=NAVY)
    # fins
    d.polygon([(166, 116), (150, 132), (166, 128)], fill=RED)
    d.polygon([(194, 116), (210, 132), (194, 128)], fill=RED)
    # flame plume: layered triangles
    d.polygon([(168, 116), (192, 116), (180, 148)], fill=ORANGE_R)
    d.polygon([(172, 116), (188, 116), (180, 140)], fill=GOLD)
    d.polygon([(176, 116), (184, 116), (180, 132)], fill=PALE)
    # smoke clouds billowing at the base
    for (ex, ey, er) in [(120, 132, 16), (150, 140, 20), (210, 140, 20),
                         (240, 132, 16), (180, 144, 18)]:
        d.ellipse([ex - er, ey - er, ex + er, ey + er],
                  fill=(220, 214, 200))
    # Tiangong station, top-right: core + solar panels
    d.rectangle([252, 22, 292, 30], fill=CREAM)
    d.rectangle([232, 16, 252, 36], fill=BLUE)
    d.rectangle([292, 16, 312, 36], fill=BLUE)
    d.ellipse([268, 20, 276, 28], fill=GOLD)
    return img


def lead_solomons():
    """Treaty scene: parliament building, Australian flag left,
    Solomon Islands flag right, handshake at a table, ocean (317x148)."""
    img = Image.new("RGB", (317, 148), NAVY)
    d = ImageDraw.Draw(img)
    # stars + crescent moon
    for (sx, sy, r) in [(120, 14, 2), (200, 20, 2), (240, 44, 2),
                        (90, 40, 2), (150, 30, 2)]:
        _star(d, sx, sy, r, WHITE)
    d.ellipse([282, 12, 306, 36], fill=GOLD)
    d.ellipse([290, 8, 310, 32], fill=NAVY)
    # ocean waves at the bottom
    d.rectangle([0, 132, 317, 148], fill=(16, 60, 110))
    for wx in (10, 70, 130, 190, 250):
        d.arc([wx, 132, wx + 44, 152], start=180, end=360,
              fill=(200, 220, 240), width=2)
    # parliament building, centre-back
    d.rectangle([96, 76, 224, 132], fill=BUILD)
    d.polygon([(96, 76), (160, 52), (224, 76)], fill=BUILD)
    d.ellipse([152, 58, 168, 70], fill=NAVY)
    for cx in (106, 132, 158, 184, 206):
        d.rectangle([cx, 84, cx + 10, 132], fill=BUILD_D)
    d.rectangle([96, 76, 224, 82], fill=CREAM)
    # small red flag on the pediment
    d.line([(160, 52), (160, 30)], fill=CREAM, width=2)
    d.rectangle([160, 30, 180, 44], fill=RED)
    # Australian flag, left pole (blue field, simplified Union Jack,
    # white stars)
    d.line([(48, 24), (48, 132)], fill=CREAM, width=2)
    d.rectangle([48, 24, 88, 50], fill=BLUE)
    d.rectangle([48, 34, 66, 40], fill=WHITE)
    d.rectangle([55, 24, 59, 50], fill=WHITE)
    d.rectangle([48, 36, 66, 38], fill=RED)
    d.rectangle([56, 24, 58, 50], fill=RED)
    _star(d, 76, 32, 3, WHITE)
    _star(d, 80, 44, 2, WHITE)
    _star(d, 70, 44, 2, WHITE)
    # Solomon Islands flag, right pole (blue over green, yellow
    # diagonal, five white stars in the blue)
    d.line([(272, 24), (272, 132)], fill=CREAM, width=2)
    d.polygon([(272, 24), (312, 24), (272, 50)], fill=BLUE)
    d.polygon([(312, 24), (312, 50), (272, 50)], fill=GREEN)
    d.line([(272, 50), (312, 24)], fill=GOLD, width=4)
    for (sx, sy) in [(282, 30), (292, 28), (300, 28), (286, 38),
                     (290, 34)]:
        _star(d, sx, sy, 2, WHITE)
    # table + two figures shaking hands, centre-front
    d.rectangle([118, 118, 202, 132], fill=(90, 50, 30))
    d.rectangle([118, 118, 202, 122], fill=(120, 70, 40))
    d.ellipse([128, 92, 140, 104], fill=(210, 170, 130))
    d.polygon([(124, 104), (144, 104), (148, 122), (120, 122)], fill=DARK)
    d.polygon([(142, 106), (158, 112), (158, 116), (142, 112)], fill=DARK)
    d.ellipse([180, 92, 192, 104], fill=(200, 150, 110))
    d.polygon([(176, 104), (196, 104), (200, 122), (172, 122)], fill=DARK)
    d.polygon([(178, 106), (162, 112), (162, 116), (178, 112)], fill=DARK)
    d.ellipse([156, 110, 164, 118], fill=GOLD)
    return img


LEAD_DRAW = {
    "cartagena": lead_cartagena,
    "shenzhou": lead_shenzhou,
    "solomons": lead_solomons,
}


# ------------------------------------------------------------------ small panels (156x40)
def small_nikkei_down():
    """Falling red bars + red down arrow + microchip (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    # falling bars only: the down arrow overlapped them and read as a
    # red blob at this size
    for (bx, bh, c) in [(12, 30, RED), (26, 24, NAVY), (40, 18, GOLD),
                        (54, 12, RED)]:
        d.rectangle([bx, 36 - bh, bx + 10, 36], fill=c)
    # microchip, right
    d.rectangle([92, 6, 128, 34], fill=(20, 45, 85), outline=GOLD, width=2)
    for py in (11, 18, 25):
        d.rectangle([86, py, 92, py + 3], fill=GOLD)
        d.rectangle([128, py, 134, py + 3], fill=GOLD)
    d.rectangle([104, 14, 116, 26], fill=GOLD)
    d.rectangle([108, 18, 112, 22], fill=NAVY)
    return img


def small_seoul():
    """Two jets + gold radar arcs + red shield (156x40)."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 12, 8, 2, WHITE)
    _star(d, 144, 8, 2, GOLD)
    # radar arcs, centre
    d.arc([58, -6, 98, 34], start=270, end=90, fill=GOLD, width=2)
    d.arc([66, 2, 90, 26], start=270, end=90, fill=GOLD, width=2)
    _jet(d, 14, 12, 40, CREAM)
    _jet(d, 100, 22, 40, CREAM)
    # red shield outline, right
    d.polygon([(132, 6), (148, 6), (148, 22), (140, 32), (132, 22)],
              outline=RED, width=2)
    return img


def small_ucl():
    """Stadium bowl + soccer ball, night (156x40)."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 14, 8, 2, WHITE)
    _star(d, 142, 8, 2, GOLD)
    d.ellipse([12, 6, 144, 46], outline=CREAM, width=2)
    d.ellipse([34, 18, 122, 40], fill=GREEN)
    d.ellipse([34, 18, 122, 40], outline=CREAM, width=1)
    d.line([(78, 18), (78, 40)], fill=CREAM, width=1)
    for fx in (26, 130):
        d.line([(fx, 6), (fx, 12)], fill=GOLD, width=2)
        d.ellipse([fx - 3, 3, fx + 3, 9], fill=GOLD)
    _ball(d, 78, 14, 7)
    return img


def small_taipo():
    """Three tower blocks with lit windows + candle flame (156x40)."""
    img = Image.new("RGB", (156, 40), DARK)
    d = ImageDraw.Draw(img)
    for (bx, bw, bh) in [(8, 26, 30), (40, 30, 36), (76, 26, 28)]:
        d.rectangle([bx, 40 - bh, bx + bw, 40], fill=(40, 55, 80))
        for wy in (40 - bh + 6, 40 - bh + 14, 40 - bh + 22):
            for wx in (bx + 4, bx + 12, bx + 20):
                if wx + 4 <= bx + bw - 2:
                    d.rectangle([wx, wy, wx + 4, wy + 4], fill=GOLD)
    # candle + flame, right
    d.rectangle([124, 22, 136, 36], fill=WHITE)
    d.polygon([(130, 8), (126, 18), (134, 18)], fill=GOLD)
    d.ellipse([127, 14, 133, 20], fill=ORANGE_R)
    return img


def small_bogor():
    """Mine shaft + helmet lamp beam + ropes (156x40)."""
    img = Image.new("RGB", (156, 40), (92, 66, 40))
    d = ImageDraw.Draw(img)
    # shaft: black vertical cut, centre
    d.rectangle([68, 0, 88, 40], fill=(10, 8, 6))
    d.rectangle([68, 0, 88, 4], fill=(30, 20, 12))
    # helmet with lamp, left
    d.ellipse([22, 14, 46, 30], fill=GOLD)
    d.rectangle([18, 28, 50, 32], fill=GOLD_D)
    d.ellipse([30, 18, 38, 26], fill=WHITE)
    d.polygon([(38, 22), (68, 14), (68, 30)], fill=(255, 240, 190))
    # rope lines, right — thick and white so they read
    d.line([(104, 0), (104, 40)], fill=WHITE, width=3)
    d.line([(118, 0), (118, 40)], fill=WHITE, width=3)
    d.line([(104, 10), (118, 10)], fill=WHITE, width=2)
    # rocks at the bottom corners
    d.polygon([(0, 40), (14, 30), (28, 40)], fill=(140, 130, 120))
    d.polygon([(128, 40), (142, 32), (156, 40)], fill=(140, 130, 120))
    return img


def small_nba():
    """Jumping player silhouette + ball + hoop (156x40)."""
    img = Image.new("RGB", (156, 40), ORANGE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 32, 156, 40], fill=CREAM)
    d.line([(0, 32), (156, 32)], fill=RED, width=1)
    d.rectangle([128, 4, 140, 20], fill=WHITE, outline=NAVY, width=1)
    d.ellipse([124, 20, 144, 26], outline=RED, width=2)
    d.line([(134, 26), (130, 32)], fill=RED, width=1)
    d.line([(134, 26), (138, 32)], fill=RED, width=1)
    d.ellipse([56, 4, 65, 13], fill=NAVY)
    d.polygon([(56, 14), (65, 14), (68, 28), (54, 28)], fill=NAVY)
    d.polygon([(63, 16), (77, 8), (80, 12), (67, 21)], fill=NAVY)
    d.polygon([(56, 28), (60, 28), (58, 40), (54, 40)], fill=NAVY)
    d.polygon([(62, 28), (66, 28), (68, 40), (64, 40)], fill=NAVY)
    d.ellipse([76, 6, 88, 18], fill=(120, 60, 20), outline=INK, width=1)
    d.line([(76, 12), (88, 12)], fill=INK, width=1)
    d.line([(82, 6), (82, 18)], fill=INK, width=1)
    return img


def small_spain():
    """Three houses + ballot box with check (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    for (hx, rc) in [(10, RED), (46, NAVY), (82, GOLD_D)]:
        d.rectangle([hx, 18, hx + 26, 36], fill=CREAM, outline=INK, width=1)
        d.polygon([(hx - 2, 18), (hx + 13, 6), (hx + 28, 18)], fill=rc)
        d.rectangle([hx + 10, 26, hx + 16, 36], fill=rc)
    # ballot box + paper + check, right
    d.rectangle([120, 18, 148, 36], fill=RED, outline=INK, width=1)
    d.polygon([(128, 6), (142, 6), (138, 18), (124, 18)], fill=WHITE,
              outline=NAVY)
    d.line([(124, 30), (130, 36), (146, 20)], fill=GREEN, width=3)
    return img


def small_brent():
    """Oil derrick + red down arrow + gold oil drop (156x40)."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 12, 8, 2, WHITE)
    # derrick: gold lattice tower
    d.line([(58, 36), (66, 6)], fill=GOLD, width=3)
    d.line([(78, 36), (70, 6)], fill=GOLD, width=3)
    for y in (14, 22, 30):
        d.line([(60, y), (76, y)], fill=GOLD, width=2)
    d.line([(60, 30), (76, 14)], fill=GOLD, width=2)
    d.line([(76, 30), (60, 14)], fill=GOLD, width=2)
    # red down arrow, right
    _arrow(d, 100, 6, 128, 32, 4, RED)
    # gold oil drop
    d.polygon([(140, 12), (134, 24), (146, 24)], fill=GOLD)
    d.ellipse([134, 20, 146, 32], fill=GOLD)
    return img


def small_ifo():
    """Gauge dial pointing up-right (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    d.arc([46, 2, 110, 66], start=180, end=360, fill=NAVY, width=3)
    d.arc([46, 2, 110, 66], start=300, end=360, fill=GOLD, width=3)
    for deg in (180, 210, 240, 270, 300, 330, 360):
        a = math.radians(deg)
        x0 = 78 + 30 * math.cos(a)
        y0 = 34 + 30 * math.sin(a)
        x1 = 78 + 25 * math.cos(a)
        y1 = 34 + 25 * math.sin(a)
        d.line([(x0, y0), (x1, y1)], fill=NAVY, width=2)
    d.line([(78, 34), (100, 12)], fill=RED, width=3)
    d.ellipse([74, 30, 82, 38], fill=NAVY)
    # small building, left
    d.rectangle([8, 20, 30, 36], fill=NAVY)
    d.polygon([(8, 20), (19, 12), (30, 20)], fill=NAVY)
    for wx in (13, 21):
        d.rectangle([wx, 26, wx + 4, 32], fill=GOLD)
    return img


def small_argentina():
    """Argentine flag bands + gold sun + red down arrow (156x40)."""
    img = Image.new("RGB", (156, 40), (116, 180, 220))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 13, 156, 27], fill=WHITE)
    # sun, centre-left
    d.ellipse([52, 10, 72, 30], fill=GOLD)
    for k in range(8):
        a = math.radians(k * 45)
        x0 = 62 + 12 * math.cos(a)
        y0 = 20 + 12 * math.sin(a)
        x1 = 62 + 16 * math.cos(a)
        y1 = 20 + 16 * math.sin(a)
        d.line([(x0, y0), (x1, y1)], fill=GOLD, width=2)
    # red down arrow, right
    _arrow(d, 96, 6, 132, 32, 5, RED)
    return img


def small_houthi():
    """Oil refinery: storage tanks, distillation towers, flame (156x40).
    The flame sits right of the red banner so it stays visible."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 148, 8, 2, GOLD)
    # storage tanks, cream cylinders, left (below the banner)
    for tx in (10, 36):
        d.rectangle([tx, 20, tx + 22, 36], fill=CREAM)
        d.ellipse([tx, 16, tx + 22, 24], fill=CREAM)
        d.rectangle([tx, 26, tx + 22, 28], fill=NAVY)
    # pipes from tanks to towers
    d.line([(62, 30), (80, 30)], fill=GOLD, width=2)
    d.line([(62, 34), (80, 34)], fill=GOLD, width=2)
    # distillation tower 2, shorter, gold bands
    d.rectangle([80, 14, 94, 36], fill=GOLD_D)
    for y in (20, 26, 32):
        d.rectangle([80, y, 94, y + 2], fill=GOLD)
    # distillation tower 1, tall, gold bands, flame on top
    d.rectangle([102, 10, 118, 36], fill=GOLD_D)
    for y in (16, 22, 28, 34):
        d.rectangle([102, y, 118, y + 2], fill=GOLD)
    d.polygon([(110, 10), (104, 2), (116, 2)], fill=ORANGE_R)
    d.polygon([(110, 10), (107, 4), (113, 4)], fill=GOLD)
    # small tank, right
    d.rectangle([126, 24, 146, 36], fill=CREAM)
    d.ellipse([126, 20, 146, 28], fill=CREAM)
    d.rectangle([126, 29, 146, 31], fill=NAVY)
    return img


def small_australia():
    """Red price tag + gold coin + gold up arrow (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    # price tag, red, pointing right
    d.polygon([(14, 12), (48, 12), (62, 20), (48, 28), (14, 28)], fill=RED)
    d.ellipse([20, 16, 28, 24], fill=CREAM)
    # gold coin, centre-bottom
    d.ellipse([70, 24, 84, 38], fill=GOLD, outline=GOLD_D, width=1)
    d.ellipse([74, 28, 80, 34], fill=GOLD_D)
    # gold up arrow, right
    _arrow(d, 96, 32, 138, 8, 5, GOLD_D)
    return img


SMALL_DRAW = {
    "nikkei": small_nikkei_down,
    "seoul": small_seoul,
    "ucl": small_ucl,
    "taipo": small_taipo,
    "bogor": small_bogor,
    "nba": small_nba,
    "spain": small_spain,
    "brent": small_brent,
    "sppi": small_ifo,
    "argentina": small_argentina,
    "houthi": small_houthi,
    "australia": small_australia,
}
