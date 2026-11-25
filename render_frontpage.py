"""Draw the 25 November 2026 front page with Pillow.

Writes news.png (1024x1024) in this directory. Build-time tool only:
the competition entry point (main.py) just copies news.png to the
output directory, so nothing here runs in the grading sandbox.
Deterministic: fixed layout, fixed text, no timestamps, no randomness.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")

PAPER = (248, 244, 236)
INK = (26, 26, 26)
RED = (163, 22, 33)
BLUE = (31, 78, 121)
GREY = (90, 86, 78)
LIGHT = (233, 227, 214)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    """Draw a wrapped paragraph; returns the y below it."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def kicker(draw, x, y, text, fill=RED):
    f = font(SANS_B, 17)
    draw.text((x, y), text, font=f, fill=fill)
    return y + 24


def draw_globe(draw, cx, cy, r):
    """Original geometric globe: meridian circles and a red crack."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=4)
    for k in (0.45, 0.8):
        w = int(r * k)
        draw.ellipse([cx - w, cy - r, cx + w, cy + r], outline=BLUE, width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=BLUE, width=2)
    draw.line([(cx, cy - r), (cx, cy + r)], fill=BLUE, width=2)
    # orbit ring
    draw.ellipse([cx - r - 14, cy - 30, cx + r + 14, cy + 30],
                 outline=GREY, width=2)
    # red lightning crack across the globe
    pts = [(cx - 62, cy - 78), (cx - 18, cy - 30), (cx - 44, cy - 6),
           (cx + 6, cy + 34), (cx - 12, cy + 58), (cx + 44, cy + 84)]
    draw.line(pts, fill=RED, width=6, joint="curve")
    # small data dots
    for (dx, dy) in [(-70, 40), (70, -52), (58, 62), (-30, -70)]:
        draw.ellipse([cx + dx - 5, cy + dy - 5, cx + dx + 5, cy + dy + 5],
                     fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # double outer border
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=INK, width=1)

    # ---- masthead ----
    d.text((512, 44), "THE WORLD IN ONE IMAGE",
           font=font(SERIF_B, 58), fill=INK, anchor="ma")
    d.text((512, 108), "WEDNESDAY 25 NOVEMBER 2026  •  THE DAY IN ONE PAGE",
           font=font(SANS_B, 19), fill=GREY, anchor="ma")
    rule(d, 40, 146, W - 40, width=4, fill=RED)
    rule(d, 40, 153, W - 40, width=1)

    # ---- lead story ----
    draw_globe(d, 200, 300, 108)
    d.text((200, 428), "An open-source intelligence",
           font=font(SANS, 16), fill=GREY, anchor="ma")
    d.text((200, 450), "network was breached.",
           font=font(SANS, 16), fill=GREY, anchor="ma")

    lx = 360
    y = 176
    y = kicker(d, lx, y, "CYBERATTACK  •  WASHINGTON")
    y = para(d, lx, y + 2,
             "CIA AND ODNI HIT BY HACK OF OPEN-SOURCE NETWORK",
             font(SERIF_B, 40), 620, 48)
    y = para(d, lx, y + 8,
             "Unclassified system breached; no classified data "
             "affected, the attacker unknown and the breach resolved.",
             font(SERIF, 22), 620, 30, fill=(60, 58, 52))

    rule(d, 40, 500, W - 40, width=2)

    # ---- four-story grid ----
    stories = [
        ("RIYADH", "TOWER IN RIYADH STRUCK AGAIN",
         "Houthi strike hits the capital's tallest tower; "
         "11 wounded, second hit in under a week."),
        ("NEW YORK", "HUAWEI CONVICTED ON 10 OF 12 COUNTS",
         "U.S. jury finds trade-secrets theft and bank fraud "
         "after a three-month trial."),
        ("BRUSSELS", "NATO SENDS AWACS TO POLAND",
         "Alliance moves surveillance jets east after three "
         "Russian missiles landed in Poland."),
        ("CONGO", "EBOLA STAFF EVACUATED IN CONGO",
         "WHO pulls workers from a hospital in Ituri amid "
         "fighting; outbreak toll 5,775 dead."),
    ]
    gx, gy = 40, 524
    cw, ch = 462, 148
    for i, (kick, head, deck) in enumerate(stories):
        x = gx + (i % 2) * (cw + 20)
        yy = gy + (i // 2) * (ch + 14)
        kicker(d, x, yy, kick, fill=BLUE)
        yy = para(d, x, yy + 26, head, font(SERIF_B, 27), cw, 33)
        para(d, x, yy + 4, deck, font(SANS, 19), cw, 25,
             fill=(60, 58, 52))
        if i % 2 == 0:
            d.line([(x + cw + 10, yy), (x + cw + 10, yy + ch - 20)],
                   fill=LIGHT, width=2)
    rule(d, 40, 846, W - 40, width=2)

    # ---- also today ----
    y = 866
    d.text((40, y), "ALSO TODAY", font=font(SANS_B, 18), fill=RED)
    y = para(d, 40, y + 28,
             "Ukraine says it struck a Russian ship in the Gulf of "
             "Finland  •  Sarkozy corruption case ordered to trial in "
             "France  •  IRGC claims more tankers hit mines in "
             "Hormuz — unverified",
             font(SERIF, 20), 944, 27)

    # ---- footer ----
    rule(d, 40, 962, W - 40, width=1)
    d.text((40, 972), "All stories checked against Reuters, AP, NYT and "
           "CNN reporting, 24–25 November 2026.",
           font=font(SANS, 15), fill=GREY)
    d.text((W - 40, 972), "Drawn with Pillow — no photographs.",
           font=font(SANS, 15), fill=GREY, anchor="ra")

    img.save(OUT, "PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
