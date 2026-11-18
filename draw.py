#!/usr/bin/env python3
"""news-image-20261117 v7: same 43 stories, radical legibility upgrade.
v6 scored 98.1243% (12-0) but ~rank 313 — the judge's only knock was
readability at 300px (dense grid, small type). v7: shorter headlines and
decks, bigger type everywhere (hero 20pt, small cards 15pt), more air.
Built in-session 2026-11-18 by Muse for the @transs123 entry (v7).
"""
import json
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (246, 241, 227)
INK = (20, 20, 20)
NAVY = (20, 35, 70)
RED = (190, 30, 30)
GREY = (110, 105, 95)
GOLD = (200, 160, 40)
WHITE = (255, 255, 255)
GREEN = (30, 120, 70)
BLUE = (30, 90, 170)
ORANGE = (210, 110, 20)
PURPLE = (110, 60, 140)
TEAL = (20, 130, 130)

def F(name, size):
    return ImageFont.truetype(name, size)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SR = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

def para(text, font, x, y, maxw, lh, fill=INK, max_lines=3):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    for i, ln in enumerate(lines[:max_lines]):
        d.text((x, y + i * lh), ln, font=font, fill=fill)
    return y + min(len(lines), max_lines) * lh

def chip(x, y, text, bg, fg=WHITE, size=10):
    w_ = d.textlength(text, font=F(FB, size)) + 12
    d.rounded_rectangle([x, y, x + w_, y + size + 8], radius=3, fill=bg)
    d.text((x + 6, y + 4), text, font=F(FB, size), fill=fg)
    return w_

def flag(x, y, w, h, code, stripes):
    d.rectangle([x, y, x + w, y + h], outline=(120, 120, 120))
    n = len(stripes)
    for i, c in enumerate(stripes):
        d.rectangle([x, y + i * h // n, x + w, y + (i + 1) * h // n], fill=c)
    t = code
    tw = d.textlength(t, font=F(FB, 9))
    d.text((x + (w - tw) / 2, y + h + 2), t, font=F(FB, 9), fill=INK)

# ---------- masthead ----------
d.text((14, 8), "THE WORLD'S NEWS IN ONE PICTURE", font=F(FB, 13), fill=RED)
r = "43 STORIES · 6 CONTINENTS · ALL FROM TUESDAY"
d.text((W - 14 - d.textlength(r, font=F(FB, 11)), 10), r, font=F(FB, 11), fill=GREY)
d.text((14, 26), "Tuesday 17 November 2026", font=F(SB, 56), fill=INK)
d.line([14, 96, W - 14, 96], fill=INK, width=2)

# ---------- hero illustrations ----------
def ill_hero_bridge(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(165, 200, 225))
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(40, 90, 140))
    for wx in range(0, w, 30):
        d.arc([x + wx, y + h - 22, x + wx + 26, y + h - 8], 0, 180, fill=(120, 170, 210), width=2)
    d.text((x + 10, y + 8), "CRIMEA", font=F(FB, 10), fill=INK)
    d.text((x + w - 52, y + 8), "RUSSIA", font=F(FB, 10), fill=INK)
    # bridge deck across, middle span collapsed
    d.rectangle([x + 8, y + 52, x + 118, y + 62], fill=(235, 235, 240))
    d.rectangle([x + w - 126, y + 52, x + w - 8, y + 62], fill=(235, 235, 240))
    d.polygon([(x + 122, y + 58), (x + 158, y + 86), (x + 194, y + 58)], fill=(190, 190, 200))
    d.polygon([(x + 122, y + 58), (x + 140, y + 86), (x + 158, y + 58)], fill=(150, 150, 160))
    # explosion star + smoke
    d.polygon([(x + 150, y + 22), (x + 158, y + 36), (x + 172, y + 30), (x + 164, y + 44),
               (x + 176, y + 52), (x + 160, y + 52), (x + 156, y + 66), (x + 148, y + 52),
               (x + 134, y + 54), (x + 142, y + 42), (x + 128, y + 38), (x + 142, y + 32)], fill=(255, 140, 0))
    d.ellipse([x + 168, y + 10, x + 196, y + 30], fill=(90, 90, 95))
    d.ellipse([x + 188, y + 4, x + 212, y + 22], fill=(120, 120, 125))
    # drones
    for dx, dy in [(30, 26), (250, 22)]:
        d.polygon([(x + dx, y + dy), (x + dx + 16, y + dy + 4), (x + dx, y + dy + 8)], fill=(40, 40, 50))
    d.rectangle([x, y + h - 20, x + w, y + h], fill=NAVY)
    d.text((x + 8, y + h - 17), "KERCH STRAIT · STRUCK FOR A SECOND DAY", font=F(FB, 9), fill=WHITE)

def ill_hero_hormuz(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(150, 195, 225))
    d.polygon([(x, y), (x + w, y), (x + w, y + 26), (x, y + 40)], fill=(232, 214, 176))
    d.polygon([(x, y + h), (x + w, y + h), (x + w, y + h - 24), (x, y + h - 34)], fill=(232, 214, 176))
    d.text((x + 96, y + 6), "IRAN", font=F(FB, 10), fill=INK)
    d.text((x + 8, y + 52), "BAHRAIN", font=F(FB, 9), fill=INK)
    d.text((x + w - 58, y + 26), "QESHM", font=F(FB, 9), fill=INK)
    d.text((x + 8, y + h - 18), "HORMUZ", font=F(FB, 9), fill=INK)
    # dashed drone path IRAN -> BAHRAIN
    for i in range(0, 90, 12):
        d.line([x + 150 - i, y + 30 + i // 3, x + 150 - i - 6, y + 32 + i // 3], fill=RED, width=2)
    d.text((x + 130, y + 44), "X", font=F(FB, 14), fill=RED)
    chip(x + 118, y + 56, "DRONES DOWNED", RED, size=9)
    chip(x + 212, y + 82, "US STRIKES", BLUE, size=9)
    # tanker
    d.rectangle([x + w - 70, y + h - 40, x + w - 10, y + h - 28], fill=(60, 60, 70))
    d.rectangle([x + w - 58, y + h - 50, x + w - 40, y + h - 40], fill=(200, 200, 210))
    d.polygon([(x + w - 50, y + h - 50), (x + w - 44, y + h - 62), (x + w - 38, y + h - 50)], fill=(255, 140, 0))

def ill_hero_quad(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(240, 235, 250))
    d.rectangle([x, y, x + w, y + 22], fill=(110, 60, 140))
    t = "QUAD LEADERS' SUMMIT · MANILA"
    d.text((x + (w - d.textlength(t, font=F(FB, 10))) / 2, y + 6), t, font=F(FB, 10), fill=WHITE)
    flags = [("US", [(200, 60, 60), (255, 255, 255), (200, 60, 60)]),
             ("INDIA", [(255, 150, 0), (255, 255, 255), (0, 130, 60)]),
             ("JAPAN", [(255, 255, 255), (255, 255, 255)]),
             ("AUSTRALIA", [(0, 60, 140), (0, 60, 140)])]
    for i, (code, stripes) in enumerate(flags):
        fx = x + 22 + i * 78
        flag(fx, y + 34, 52, 30, code, stripes)
        if code == "JAPAN":
            d.ellipse([fx + 18, y + 42, fx + 34, y + 58], fill=RED)
        if code == "AUSTRALIA":
            for sx, sy in [(8, 6), (38, 10), (20, 18), (44, 22)]:
                d.ellipse([fx + sx, y + 34 + sy, fx + sx + 4, y + 38 + sy], fill=WHITE)
    d.rectangle([x + 16, y + 74, x + w - 16, y + 86], fill=(120, 85, 50))
    d.rectangle([x, y + h - 18, x + w, y + h], fill=PURPLE)
    t2 = "NEW CRITICAL-MINERALS DEALS"
    d.text((x + (w - d.textlength(t2, font=F(FB, 9))) / 2, y + h - 15), t2, font=F(FB, 9), fill=WHITE)

# ---------- small illustrations (192 wide) ----------
def ill_ebola(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 240, 245))
    d.rectangle([x + 14, y + 14, x + 60, y + h - 6], fill=WHITE, outline=(180, 180, 180))
    d.rectangle([x + 14, y + 14, x + 60, y + 24], fill=NAVY)
    d.rectangle([x + 30, y + 4, x + 44, y + 20], fill=WHITE, outline=RED, width=2)
    d.rectangle([x + 35, y + 8, x + 39, y + 16], fill=RED)
    d.rectangle([x + 32, y + 11, x + 42, y + 13], fill=RED)
    for i in range(2):
        d.rectangle([x + 20 + i * 18, y + 32, x + 32 + i * 18, y + 42], fill=(140, 190, 220))
    for sx, sy in [(90, 12), (150, 34), (120, 52)]:
        d.ellipse([x + sx, y + sy, x + sx + 12, y + sy + 12], fill=(200, 60, 60))
        d.line([x + sx + 6, y + sy - 4, x + sx + 6, y + sy + 16], fill=(200, 60, 60), width=2)
        d.line([x + sx - 4, y + sy + 6, x + sx + 16, y + sy + 6], fill=(200, 60, 60), width=2)

def ill_cop31(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(220, 235, 225))
    d.ellipse([x + 12, y + 10, x + 66, y + 64], fill=(60, 140, 200))
    d.ellipse([x + 22, y + 18, x + 40, y + 30], fill=(40, 160, 80))
    d.ellipse([x + 42, y + 40, x + 58, y + 54], fill=(40, 160, 80))
    # thermometer
    d.rectangle([x + 96, y + 12, x + 106, y + 48], fill=WHITE, outline=RED, width=2)
    d.ellipse([x + 90, y + 44, x + 112, y + 66], fill=RED)
    d.rectangle([x + 99, y + 22, x + 103, y + 48], fill=RED)
    d.text((x + 122, y + 12), "DRAFT:", font=F(FB, 9), fill=INK)
    d.text((x + 122, y + 24), "PHASE-OUT", font=F(FB, 9), fill=RED)
    d.text((x + 122, y + 38), "FOSSIL FUEL?", font=F(FB, 8), fill=INK)

def ill_measles(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 240, 245))
    d.rectangle([x + 16, y + 16, x + w - 16, y + h - 6], fill=WHITE, outline=(180, 180, 180))
    d.rectangle([x + 16, y + 16, x + w - 16, y + 26], fill=NAVY)
    d.rectangle([x + w // 2 - 10, y + 4, x + w // 2 + 10, y + 22], fill=WHITE, outline=RED, width=2)
    d.rectangle([x + w // 2 - 3, y + 7, x + w // 2 + 3, y + 19], fill=RED)
    d.rectangle([x + w // 2 - 7, y + 11, x + w // 2 + 7, y + 15], fill=RED)
    for i in range(3):
        d.rectangle([x + 24 + i * 48, y + 34, x + 42 + i * 48, y + 46], fill=(140, 190, 220))
    d.rectangle([x + w // 2 - 10, y + 34, x + w // 2 + 10, y + h - 6], fill=(120, 80, 40))

def ill_nvidia(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(20, 40, 30))
    pts = [(x + 12, y + 52), (x + 50, y + 44), (x + 88, y + 48), (x + 126, y + 30), (x + 164, y + 14)]
    d.line(pts, fill=(60, 220, 120), width=3)
    for px, py in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=WHITE)
    d.rectangle([x + 120, y + 8, x + w - 8, y + 26], fill=GREEN)
    d.text((x + 126, y + 11), "$115.8BN", font=F(FB, 10), fill=WHITE)

def ill_gaza(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 225, 205))
    d.ellipse([x + w - 30, y + 4, x + w - 10, y + 24], fill=(255, 200, 0))
    for i, tx in enumerate([10, 68, 126]):
        d.polygon([(x + tx, y + 44), (x + tx + 22, y + 20), (x + tx + 44, y + 44)], fill=(250, 245, 230), outline=(150, 130, 100))
        d.polygon([(x + tx + 17, y + 44), (x + tx + 22, y + 32), (x + tx + 27, y + 44)], fill=(120, 80, 40))
    d.rectangle([x + 10, y + h - 22, x + 70, y + h - 6], fill=WHITE, outline=(150, 150, 150))
    d.text((x + 26, y + h - 20), "AID", font=F(FB, 10), fill=NAVY)
    d.rectangle([x + 70, y + h - 18, x + 90, y + h - 6], fill=(200, 60, 60))

def ill_mongolia(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(240, 235, 220))
    flag(x + 12, y + 10, 44, 28, "MN", [(200, 60, 60), (0, 80, 160), (200, 60, 60)])
    d.rectangle([x + 70, y + 10, x + w - 12, y + h - 10], fill=WHITE, outline=(150, 150, 150))
    d.text((x + 76, y + 14), "RESIGNATION", font=F(FB, 9), fill=INK)
    d.line([x + 76, y + 30, x + w - 20, y + 30], fill=GREY, width=1)
    d.line([x + 76, y + 38, x + w - 20, y + 38], fill=GREY, width=1)
    d.text((x + 76, y + 44), "$25M CLAIM", font=F(FB, 8), fill=RED)

def ill_serbia(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(225, 235, 245))
    # hemicycle seats
    for i, ang in enumerate(range(210, 331, 15)):
        import math
        cx, cy = x + w // 2, y + h - 8
        r = 38 - (i % 2) * 12
        px, py = cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang))
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=RED if i < 5 else BLUE)
    d.rectangle([x + w // 2 - 22, y + h - 22, x + w // 2 + 22, y + h - 10], fill=(120, 85, 50))
    d.text((x + 10, y + 4), "STUDENTS 140", font=F(FB, 8), fill=RED)
    d.text((x + w - 56, y + 4), "VUCIC 103", font=F(FB, 8), fill=BLUE)

def ill_bangladesh(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(230, 225, 210))
    d.rectangle([x + 12, y + 22, x + 110, y + h - 8], fill=(180, 160, 130))
    for i in range(3):
        d.rectangle([x + 20 + i * 28, y + 30, x + 38 + i * 28, y + 44], fill=(140, 190, 220))
    d.rectangle([x + 96, y + 8, x + 102, y + 22], fill=(90, 90, 90))
    # workers with placard
    for i, wx in enumerate([128, 152]):
        d.ellipse([x + wx, y + 30, x + wx + 10, y + 40], fill=(200, 160, 120))
        d.rectangle([x + wx - 2, y + 40, x + wx + 12, y + h - 8], fill=(40, 90, 170) if i else (200, 60, 60))
    d.rectangle([x + 118, y + 12, x + w - 10, y + 28], fill=WHITE, outline=INK)
    d.text((x + 122, y + 15), "TK 30,000", font=F(FB, 8), fill=INK)

def ill_planecrash(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(170, 190, 205))
    d.polygon([(x, y + h), (x + 60, y + 16), (x + 130, y + h)], fill=(120, 140, 160))
    d.polygon([(x + 48, y + 26), (x + 60, y + 16), (x + 72, y + 26), (x + 60, y + 34)], fill=WHITE)
    d.polygon([(x + 80, y + h), (x + 150, y + 28), (x + w, y + h)], fill=(100, 120, 140))
    d.ellipse([x + 100, y + 8, x + 140, y + 30], fill=(80, 80, 85))
    d.ellipse([x + 125, y + 4, x + 158, y + 24], fill=(110, 110, 115))
    d.polygon([(x + 50, y + 52), (x + 78, y + 44), (x + 96, y + 56)], fill=(60, 60, 70))
    d.polygon([(x + 130, y + 48), (x + 146, y + 54), (x + 132, y + 60)], fill=(200, 60, 60))

def ill_mozambique(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 230, 215))
    # courthouse columns
    d.rectangle([x + 16, y + 14, x + w - 16, y + 24], fill=(120, 100, 70))
    for cx in (30, 70, 110, 150):
        d.rectangle([x + cx, y + 24, x + cx + 12, y + 56], fill=(200, 190, 160), outline=(150, 140, 120))
    d.rectangle([x + 16, y + 56, x + w - 16, y + 62], fill=(120, 100, 70))
    # gavel
    d.line([x + 60, y + 66, x + 130, y + 40], fill=(120, 80, 40), width=4)
    d.rectangle([x + 118, y + 30, x + 148, y + 44], fill=(120, 80, 40))
    d.text((x + 108, y + 52), "5 CHARGES", font=F(FB, 8), fill=RED)

# ---------- hero cards ----------
HERO = [
    (1, "EUROPE · UKRAINE WAR", RED, "Crimean Bridge span falls into the sea",
     "Second strike in two days; Zelensky hails it. The Kremlin vows to rebuild.", ill_hero_bridge),
    (2, "MIDDLE EAST · IRAN WAR", RED, "Iran drones a US radar in Bahrain",
     "Bahrain and the US say all were downed; US jets then strike Qeshm.", ill_hero_hormuz),
    (3, "ASIA · DIPLOMACY", PURPLE, "Trump holds his first Quad summit",
     "The four unveil critical-minerals deals; Putin reaches Shenzhen.", ill_hero_quad),
]
hy = 104
for i, (num, tag, tc, head, deck, ill) in enumerate(HERO):
    x = 14 + i * 336
    w = 324
    d.rectangle([x, hy, x + w, hy + 208], fill=WHITE, outline=(200, 195, 180))
    ill(x + 6, hy + 6, w - 12, 100)
    d.text((x + 10, hy + 112), f"{num}  {tag}", font=F(FB, 11), fill=tc)
    para(head, F(SB, 20), x + 10, hy + 128, w - 20, 25, max_lines=2)
    para(deck, F(FR, 11), x + 10, hy + 180, w - 20, 14, fill=(60, 60, 60), max_lines=2)

# ---------- small cards ----------
SMALL = [
    (4, "AFRICA · HEALTH", RED, "Ebola cases in DR Congo top 11,000",
     "Cases doubled in three months; 5,400 have died.", "DR CONGO · EBOLA", RED, ill_ebola),
    (5, "GLOBAL · CLIMATE", TEAL, "COP31 draft splits over fossil fuels",
     "Nations weigh the first draft; talks end Friday.", "COP31 ANTALYA · ENDS FRI", TEAL, ill_cop31),
    (6, "AMERICAS · HEALTH", RED, "US, Mexico, Bolivia lose measles-free status",
     "PAHO cites a year of spread; US cases pass 5,400.", "MEASLES-FREE STATUS REVOKED", RED, ill_measles),
    (7, "US · BUSINESS", GREEN, "Nvidia sales double to $115.8bn",
     "Reported after the close. The Dow fell 849 points.", "NVIDIA QUARTER · WALL STREET", GREEN, ill_nvidia),
    (8, "MIDDLE EAST · GAZA", ORANGE, "Gaza truce at risk of collapse",
     "Board of Peace report; 1.4m face acute hunger.", "GAZA · WINTER AID HELD UP", ORANGE, ill_gaza),
    (9, "ASIA · POLITICS", BLUE, "Mongolia's president says he will resign",
     "Khurelsukh denies a $25m bribe claim.", "ULAANBAATAR · GRAFT CLAIM", BLUE, ill_mongolia),
    (10, "EUROPE · POLITICS", BLUE, "Serbia's student majority takes its seats",
     "Student List holds 140 of 250; Vucic's party out.", "BELGRADE · SWORN IN", BLUE, ill_serbia),
    (11, "ASIA · LABOUR", ORANGE, "Bangladesh police tear-gas garment workers",
     "They want Tk 30,000 a month, up from 12,500.", "DHAKA · SAVAR · GAZIPUR", ORANGE, ill_bangladesh),
    (12, "RUSSIA · AIR CRASH", RED, "Russian An-12 crash kills all 19",
     "The air force plane came down near Kemerovo.", "KEMEROVO · ALL 19 KILLED", RED, ill_planecrash),
    (13, "AFRICA · JUSTICE", GREEN, "Mozambique puts opposition leader on trial",
     "Ven\u00e2ncio Mondlane faces 5 charges.", "MAPUTO · SUPREME COURT", GREEN, ill_mozambique),
]
for r in range(2):
    for c in range(5):
        num, tag, tc, head, deck, bar, bc, ill = SMALL[r * 5 + c]
        x = 14 + c * 200
        y = 322 + r * 184
        w = 192
        d.rectangle([x, y, x + w, y + 176], fill=WHITE, outline=(200, 195, 180))
        ill(x + 5, y + 5, w - 10, 58)
        d.rectangle([x + 5, y + 63, x + w - 5, y + 78], fill=bc)
        d.text((x + 9, y + 66), bar, font=F(FB, 9), fill=WHITE)
        d.text((x + 8, y + 82), f"{num}  {tag}", font=F(FB, 9), fill=tc)
        para(head, F(SB, 15), x + 8, y + 96, w - 16, 19, max_lines=2)
        para(deck, F(FR, 10), x + 8, y + 134, w - 16, 13, fill=(60, 60, 60), max_lines=2)

# ---------- map + also strip ----------
d.text((14, 694), "WHERE IT HAPPENED", font=F(FB, 11), fill=RED)
d.text((350, 694), "ALSO ON TUESDAY 17 NOVEMBER", font=F(FB, 11), fill=RED)
d.text((W - 14 - d.textlength("30 MORE STORIES", font=F(FB, 11)), 694), "30 MORE STORIES", font=F(FB, 11), fill=GREY)

with open("world.geo.json") as fh:
    geo = json.load(fh)

def _proj(lon, lat):
    mx, my, mw, mh = 14, 712, 320, 200
    px = mx + (lon + 180) / 360 * mw
    py = my + (90 - lat) / 180 * mh
    return px, py

d.rectangle([14, 712, 334, 912], fill=(210, 225, 235))
for feat in geo["features"]:
    g = feat["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    for poly in polys:
        for ring in poly:
            pts = [_proj(lon, lat) for lon, lat in ring]
            d.polygon(pts, fill=(240, 228, 200), outline=(255, 255, 255))

REG_COLORS = {"Americas": RED, "Europe": BLUE, "Middle East": ORANGE,
              "Asia": PURPLE, "Africa": GREEN, "Oceania": TEAL, "Global": (90, 90, 90)}
PINS = [
    (1, "Europe", 33.5, 45.3), (2, "Middle East", 56.3, 26.5), (3, "Asia", 121.0, 14.6),
    (4, "Africa", 23.0, -2.0), (5, "Global", 30.7, 36.9), (6, "Americas", -98.0, 39.0),
    (7, "Americas", -98.0, 39.0), (8, "Middle East", 34.5, 31.5), (9, "Asia", 106.9, 47.9),
    (10, "Europe", 20.5, 44.8), (11, "Asia", 90.4, 23.8), (12, "Europe", 87.5, 55.0),
    (13, "Africa", 32.6, -25.9),
]
DOTS = [
    (14, "Europe", 37.6, 55.7), (15, "Europe", 30.5, 50.4), (16, "Global", 0.0, 46.0),
    (17, "Europe", 14.4, 50.1), (18, "Europe", 2.3, 48.9), (19, "Europe", 21.0, 52.2),
    (20, "Europe", 10.0, 51.0), (21, "Europe", 28.8, 47.0), (22, "Middle East", 28.9, 41.0),
    (23, "Europe", 10.7, 59.9), (24, "Global", 12.5, 41.9), (25, "Europe", -0.1, 51.5),
    (26, "Middle East", 35.2, 33.9), (27, "Middle East", 31.2, 30.1), (28, "Middle East", 44.4, 33.3),
    (29, "Asia", 85.8, 20.3), (30, "Asia", 78.0, 30.0), (31, "Asia", 130.4, 33.6),
    (32, "Asia", 116.4, 39.9), (33, "Asia", 101.7, 3.1), (34, "Asia", 100.5, 13.8),
    (35, "Asia", 127.0, 37.5), (36, "Asia", 77.2, 28.6), (37, "Africa", 36.8, -1.3),
    (38, "Africa", 3.4, 6.5), (39, "Americas", -72.3, 18.5), (40, "Americas", -77.0, 38.9),
    (41, "Oceania", 149.1, -35.3), (42, "Oceania", 130.8, -12.5), (43, "Americas", -122.4, 37.8),
]
for num, region, lon, lat in DOTS:
    px, py = _proj(lon, lat)
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=REG_COLORS[region])
for num, region, lon, lat in PINS:
    px, py = _proj(lon, lat)
    c = REG_COLORS[region]
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=c, outline=WHITE, width=2)
    t = str(num)
    tw = d.textlength(t, font=F(FB, 8))
    d.text((px - tw / 2, py - 6), t, font=F(FB, 8), fill=WHITE)

also = [
    (14, "Russia", "says it downed a record 1,441 drones overnight"),
    (15, "Kyiv", "missiles hit the North and South Dnipro bridges"),
    (16, "UN", "Ukraine's civilian deaths this year top all of 2025"),
    (17, "Prague", "two trains collide; 46 people injured"),
    (18, "France", "public-sector strike; 146,000 march"),
    (19, "Poland", "Tusk's government survives a no-confidence vote"),
    (20, "Germany", "Deutsche Bank shares fall after a huge data leak"),
    (21, "Moldova", "shuts its airspace as a drone nears Chisinau"),
    (22, "Turkey", "police seize opposition broadcaster Sözcü TV"),
    (23, "Football", "Norway win 3-2 in Denmark; Haaland scores twice"),
    (24, "Vatican", "Pope Leo XIV returns from his South America tour"),
    (25, "UK", "sanctions 8 settlement firms and Tzav 9"),
    (26, "Israel", "Eisenkot ally Matan Kahana elected speaker, 66-52"),
    (27, "West Bank", "settlers kill a woman, 72, near Jericho"),
    (28, "Oman", "Iran's Araghchi holds shipping-safety talks"),
    (29, "India", "Cyclone Akvan strengthens; Odisha evacuates"),
    (30, "India", "bus falls into an Uttarakhand gorge, 8 dead"),
    (31, "Japan", "protests a Russian airspace intrusion near Fukuoka"),
    (32, "China-Canada", "more tariff cuts after Carney-Xi talks"),
    (33, "Malaysia", "Macron visit seals a strategic partnership"),
    (34, "Thailand", "pledges to scrap tariffs on US goods"),
    (35, "South Korea", "IMF lifts 2026 growth forecast to 3.9%"),
    (36, "Football", "India beat Pakistan 2-1 in SAFF final"),
    (37, "Kenya", "WFP aids 30,000 who fled Ethiopia clashes"),
    (38, "Football", "Togo beat Algeria 3-0 in AFCON qualifier"),
    (39, "Haiti", "Aristide's party will field no candidates"),
    (40, "US Senate", "Van Hollen challenges Schumer for leader"),
    (41, "Australia", "eases planned backpacker visa curbs"),
    (42, "Darwin", "M6.6 quake off Indonesia felt; no tsunami"),
    (43, "Apple", "Pay, iCloud and App Store outage; not a hack"),
]
REG_OF = {n: r for n, r, _, _ in [(n, REG_COLORS[reg], lo, la) for n, reg, lo, la in DOTS]}
for ci, col in enumerate([also[0:15], also[15:30]]):
    x = 350 + ci * 340
    y = 712
    for num, region, head in col:
        c = REG_OF[num]
        d.ellipse([x, y, x + 14, y + 14], fill=c)
        t = str(num)
        tw = d.textlength(t, font=F(FB, 8))
        d.text((x + 7 - tw / 2, y + 3), t, font=F(FB, 8), fill=WHITE)
        d.text((x + 18, y + 1), f"{region}: ", font=F(FB, 10), fill=GREY)
        rw = d.textlength(f"{region}: ", font=F(FB, 10))
        d.text((x + 18 + rw, y + 1), head, font=F(FR, 10), fill=NAVY)
        y += 14

# legend + footer
lx = 14
for name, c in [("Americas", RED), ("Europe", BLUE), ("Middle East", ORANGE),
                ("Asia", PURPLE), ("Africa", GREEN), ("Oceania", TEAL)]:
    d.ellipse([lx, 922, lx + 8, 930], fill=c)
    d.text((lx + 11, 920), name, font=F(FR, 9), fill=INK)
    lx += 11 + d.textlength(name, font=F(FR, 9)) + 12
d.text((14, 938), "Pins: stories 1-13 · dots: 14-43", font=F(FR, 9), fill=GREY)
d.text((14, 966), "Every story here happened or was first reported on Tuesday 17 November 2026. Contested claims are marked as claims.",
       font=F(FR, 9), fill=GREY)
d.text((14, 982), "Sources: Reuters, AP, AFP, BBC, Al Jazeera, WHO, UN. Original drawings.",
       font=F(FR, 9), fill=GREY)

img.save("entry.png")
print("saved entry.png", img.size)
import os
print("bytes", os.path.getsize("entry.png"))
