#!/usr/bin/env python3
"""Front page for make.fun's news-image-20261122 contest: the world news
of Sunday 22 November 2026, drawn as one newspaper page.

Every story was verified against at least two published sources dated
22 November 2026 (Le Monde, Reuters/Nikkei, NPR, CNN, Al Jazeera for
COP31; Reuters, Ukrainska Pravda, Kyiv Post, The New Voice of Ukraine,
Daily Sabah for Dymer; Arab News/AFP, Al Arabiya, The National, Gulf
News for Bahrain; Reuters, AFP/Arab News, Haaretz, The Times of
Israel, Al Jazeera for the West Bank; Reuters/AP, Al Jazeera, Fox News
for the House; CNA/Reuters, AP, Al Jazeera, Fox News for Indonesia):
  1. COP31 collapses in Antalya: the summit ends on Sunday with no
     deal after the EU and others reject the "Antalya Pact" draft,
     which makes no mention of fossil fuels; the longest COP ever,
     the first collapse since Copenhagen 2009.
  2. A Russian drone destroys a section of a five-storey apartment
     block in Dymer, near Kyiv: 14 people missing, nine evacuated,
     rescuers searching the rubble.
  3. Bahrain counts the cost of Saturday's Iranian strike: two
     people hurt at a civilian industrial site, one in critical
     condition; Iran claims it hit two US Patriot radars.
  4. Settlers torch a dozen vehicles in four West Bank villages
     overnight; Israel opens an investigation; Eisenkot calls the
     attacks "Jewish terrorism".
  5. Democrats clinch 258 House seats: a North Carolina recount
     hands Chuck Hubbard the 258th seat, the party's biggest House
     majority since 1992; Democrats also take the Senate.
  6. A fire sweeps a candy factory in Banten, Indonesia: 3 dead,
     36 missing; the Milkita sweets plant blaze began Saturday
     evening and the toll was reported on Sunday.
Ticker: the US warns Americans in Bahrain after the strikes; Delta
delays 1,000+ flights after a Microsoft outage; Russia starts towing
its drone-hit ship Sparta II in the Baltic.

Left out on purpose, because they happened or were first reported on
an earlier day: the Iran strike itself (21 Nov, yesterday's lead),
the capture of "El Chapo Isidro" (21 Nov), the Kryvyi Rih missile
(21 Nov), BepiColombo reaching Mercury (21 Nov), the S&P 500's 3.7%
Friday fall (20 Nov), and the Trump-Xi-Putin trilateral summit
(19-20 Nov).

Flat-shape illustrations only -- no photos and no borrowed artwork.
Running this file writes entry.png (1024 x 1024) next to it.
"""

import math

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
PAPER = (247, 242, 232)
INK = (22, 22, 22)
RED = (178, 48, 40)
GREY = (96, 96, 96)
TEAL = (40, 96, 120)


def load(path, size):
    return ImageFont.truetype(path, size)


BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def split_lines(draw, text, font, width):
    lines, current = [], ""
    for word in text.split():
        test = (current + " " + word).strip()
        if draw.textlength(test, font=font) <= width:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def block(draw, x, y, text, font, fill, width, centre=False, gap=1.14):
    for line in split_lines(draw, text, font, width):
        lx = x + (width - draw.textlength(line, font=font)) / 2 if centre else x
        draw.text((lx, y), line, font=font, fill=fill)
        y += int(font.size * gap)
    return y


def panel_text(draw, x, y, w, tag, head, body, head_size=25, body_size=18):
    draw.text((x, y), tag, font=load(BOLD, 19), fill=RED)
    y = block(draw, x, y + 26, head, load(BOLD, head_size), INK, w)
    block(draw, x, y + 4, body, load(PLAIN, body_size), GREY, w)


# ------------------------------------------------------------------ scenes
def scene_cop31(d, x, y, w, h):
    """A climate summit hall at the end: a long table with microphones,
    a row of small national flags, a clock past midnight, and a torn
    draft document -- the deal that was never adopted."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 230, 222))
    # wall panels and a round clock, past midnight
    d.rectangle([x, y, x + w, y + 26], fill=(58, 96, 84))
    cx, cy, r = x + w * 0.20, y + h * 0.42, min(34, int(h * 0.32))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255),
              outline=INK, width=3)
    for k in range(12):
        ang = k * math.pi / 6
        px, py = cx + (r - 6) * math.sin(ang), cy - (r - 6) * math.cos(ang)
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=INK)
    d.line([cx, cy, cx, cy - r + 10], fill=INK, width=3)
    d.line([cx, cy, cx + (r - 13), cy + 7], fill=INK, width=3)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)
    # the long table with microphones and name plates
    ty = y + h - 84
    d.rectangle([x + 16, ty, x + w - 16, ty + 34], fill=(110, 76, 50))
    d.rectangle([x + 10, ty - 6, x + w - 10, ty], fill=(90, 60, 40))
    for mx in (0.42, 0.55, 0.68, 0.81):
        px = x + w * mx
        d.line([px, ty - 6, px, ty - 30], fill=INK, width=2)
        d.ellipse([px - 4, ty - 34, px + 4, ty - 26], fill=INK)
        d.rectangle([px - 14, ty - 2, px + 14, ty + 8], fill=(255, 255, 255),
                    outline=INK, width=1)
    # torn draft: two halves of a white page, split down the middle
    px0, py0 = x + w * 0.60, y + h * 0.30
    d.polygon([(px0, py0), (px0 + 52, py0 + 6), (px0 + 44, py0 + 34),
               (px0 + 8, py0 + 40)], fill=(255, 255, 255), outline=INK)
    d.polygon([(px0 + 58, py0 + 8), (px0 + 106, py0), (px0 + 100, py0 + 42),
               (px0 + 54, py0 + 38)], fill=(240, 240, 240), outline=INK)
    for lx in (px0 + 8, px0 + 66):
        for k in range(3):
            d.line([lx, py0 + 10 + k * 8, lx + 34, py0 + 10 + k * 8],
                   fill=GREY, width=1)
    # strip of small flags along the bottom
    cols = [(0, 51, 153), (200, 16, 46), (0, 122, 61), (255, 210, 0),
            (46, 109, 164), (120, 60, 140)]
    fw, fh = 30, 10
    fy = y + h - 13
    total = len(cols) * (fw + 6) - 6
    fx = x + (w - total) / 2
    for i, col in enumerate(cols):
        d.rectangle([fx + i * (fw + 6), fy, fx + i * (fw + 6) + fw, fy + fh],
                    fill=col, outline=INK, width=1)


def scene_dymer(d, x, y, w, h):
    """A grey morning town: a five-storey block with its middle section
    collapsed into rubble, a smoke column rising, and a rescue ladder
    against the standing part. All heights scale with h."""
    d.rectangle([x, y, x + w, y + h], fill=(205, 210, 216))
    for sx, sy in ((0.07, 0.14), (0.36, 0.08), (0.62, 0.18), (0.86, 0.10)):
        px, py = x + w * sx, y + h * sy
        d.ellipse([px, py, px + w * 0.11, py + h * 0.12],
                  fill=(235, 235, 238))
    base = y + h - h * 0.16
    # standing left and right parts of the block
    d.rectangle([x + w * 0.06, base - h * 0.58, x + w * 0.34, base],
                fill=(96, 100, 110))
    d.rectangle([x + w * 0.66, base - h * 0.58, x + w * 0.94, base],
                fill=(96, 100, 110))
    for bx0, bx1 in ((0.06, 0.34), (0.66, 0.94)):
        for wy in range(3):
            wy0 = base - h * 0.52 + wy * h * 0.18
            for wx in range(2):
                wx0 = x + w * (bx0 + 0.04 + wx * 0.13)
                d.rectangle([wx0, wy0, wx0 + w * 0.06, wy0 + h * 0.08],
                            fill=(210, 200, 140))
    # collapsed middle: jagged gap and rubble pile
    gx0, gx1 = x + w * 0.34, x + w * 0.66
    d.polygon([(gx0, base), (gx0 + w * 0.04, base - h * 0.22),
               (gx0 + w * 0.12, base - h * 0.10),
               (gx0 + w * 0.20, base - h * 0.26),
               (gx0 + w * 0.28, base - h * 0.08), (gx1, base - h * 0.18),
               (gx1, base)], fill=(70, 70, 78))
    d.polygon([(gx0, base), (gx0 + w * 0.08, base - h * 0.10),
               (gx0 + w * 0.16, base - h * 0.06),
               (gx0 + w * 0.24, base - h * 0.12), (gx1, base - h * 0.05),
               (gx1, base)], fill=(110, 106, 98))
    # smoke column over the gap
    sx = x + w * 0.50
    for ox, oy, rr in ((-0.02, -0.62, 0.06), (0.03, -0.70, 0.07),
                       (-0.01, -0.76, 0.055)):
        px, py = sx + w * ox, base + h * oy
        d.ellipse([px - h * rr, py - h * rr, px + h * rr, py + h * rr],
                  fill=(90, 90, 98))
    # rescue ladder against the left standing part
    lx = x + w * 0.30
    d.line([lx, base - h * 0.50, lx + w * 0.06, base], fill=(200, 60, 40),
           width=3)
    d.line([lx + w * 0.05, base - h * 0.50, lx + w * 0.11, base],
           fill=(200, 60, 40), width=3)
    d.rectangle([x, base, x + w, y + h], fill=(130, 128, 120))


def scene_bahrain(d, x, y, w, h):
    """Daylight over an industrial site on the Gulf: factory blocks and
    chimneys, a fire glow at the base, and a thick smoke column."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 232, 238))
    for sx, sy in ((0.10, 0.12), (0.45, 0.08), (0.78, 0.14)):
        px, py = x + w * sx, y + h * sy
        d.ellipse([px, py, px + w * 0.10, py + h * 0.10],
                  fill=(255, 255, 255))
    base = y + h - h * 0.18
    # factory blocks and chimneys
    d.rectangle([x + w * 0.06, base - h * 0.34, x + w * 0.30, base],
                fill=(120, 126, 134))
    d.rectangle([x + w * 0.34, base - h * 0.46, x + w * 0.52, base],
                fill=(96, 102, 112))
    d.rectangle([x + w * 0.56, base - h * 0.30, x + w * 0.72, base],
                fill=(120, 126, 134))
    for cx0 in (0.10, 0.58):
        d.rectangle([x + w * cx0, base - h * 0.62, x + w * (cx0 + 0.04),
                     base - h * 0.30], fill=(80, 84, 92))
    # fire glow and smoke at the middle block
    fx = x + w * 0.43
    d.ellipse([fx - w * 0.10, base - h * 0.16, fx + w * 0.10, base + h * 0.02],
              fill=(235, 110, 40))
    d.ellipse([fx - w * 0.05, base - h * 0.11, fx + w * 0.05, base],
              fill=(255, 205, 90))
    for ox, oy, rr in ((-0.03, -0.48, 0.06), (0.02, -0.58, 0.07),
                       (0.00, -0.66, 0.055)):
        px, py = fx + w * ox, base + h * oy
        d.ellipse([px - h * rr, py - h * rr, px + h * rr, py + h * rr],
                  fill=(70, 70, 78))
    # sea strip at the bottom
    d.rectangle([x, y + h - 14, x + w, y + h], fill=(24, 54, 78))
    d.line([x + 10, y + h - 7, x + 90, y + h - 7], fill=(120, 160, 190),
           width=2)


def scene_westbank(d, x, y, w, h):
    """Night in a hill village: stone houses, a car burning orange
    against the dark, and a wall daubed with red graffiti marks."""
    d.rectangle([x, y, x + w, y + h], fill=(24, 28, 44))
    for sx, sy in ((x + 20, y + 12), (x + 90, y + 26), (x + 180, y + 10),
                   (x + 260, y + 24), (x + 330, y + 14)):
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255))
    base = y + h - h * 0.20
    # stone houses with lit windows
    for hx, hw, hh in ((0.04, 0.22, 0.34), (0.30, 0.20, 0.42),
                       (0.56, 0.18, 0.30), (0.78, 0.18, 0.38)):
        d.rectangle([x + w * hx, base - h * hh, x + w * (hx + hw), base],
                    fill=(120, 108, 88))
        d.rectangle([x + w * (hx + 0.05), base - h * hh - h * 0.08,
                     x + w * (hx + hw - 0.05), base - h * hh],
                    fill=(90, 78, 62))
        d.rectangle([x + w * (hx + 0.07), base - h * hh + h * 0.10,
                     x + w * (hx + 0.13), base - h * hh + h * 0.20],
                    fill=(255, 210, 110))
    # burning car in the street, right of centre
    cx = x + w * 0.52
    d.ellipse([cx - w * 0.14, base - h * 0.22, cx + w * 0.14, base + h * 0.02],
              fill=(235, 110, 40))
    d.ellipse([cx - w * 0.07, base - h * 0.16, cx + w * 0.07, base],
              fill=(255, 205, 90))
    d.rectangle([cx - w * 0.13, base - h * 0.16, cx + w * 0.13,
                 base - h * 0.06], fill=(20, 20, 24))
    d.ellipse([cx - w * 0.10, base - h * 0.06, cx - w * 0.04, base],
              fill=(10, 10, 12))
    d.ellipse([cx + w * 0.04, base - h * 0.06, cx + w * 0.10, base],
              fill=(10, 10, 12))
    # smoke above the car
    for ox, oy, rr in ((-0.02, -0.42, 0.05), (0.03, -0.50, 0.06),
                       (0.00, -0.56, 0.045)):
        px, py = cx + w * ox, base + h * oy
        d.ellipse([px - h * rr, py - h * rr, px + h * rr, py + h * rr],
                  fill=(80, 80, 90))
    # graffiti wall, left foreground
    d.rectangle([x + w * 0.04, base - h * 0.10, x + w * 0.24, base],
                fill=(150, 142, 128))
    d.line([x + w * 0.07, base - h * 0.07, x + w * 0.21, base - h * 0.04],
           fill=RED, width=3)
    d.line([x + w * 0.07, base - h * 0.03, x + w * 0.21, base - h * 0.06],
           fill=RED, width=3)
    d.rectangle([x, base, x + w, y + h], fill=(52, 48, 44))


def scene_democrats(d, x, y, w, h):
    """The US Capitol dome in white over blue, with a big red 258 and
    a ballot box below -- the Democrats' House majority."""
    d.rectangle([x, y, x + w, y + h], fill=(36, 64, 110))
    for sx, sy in ((x + 18, y + 12), (x + 70, y + 30), (x + 150, y + 10),
                   (x + 220, y + 26), (x + 300, y + 14)):
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255))
    base = y + h - h * 0.22
    # Capitol dome
    cx = x + w * 0.50
    d.rectangle([cx - w * 0.30, base - h * 0.10, cx + w * 0.30, base],
                fill=(235, 235, 230))
    d.rectangle([cx - w * 0.34, base - h * 0.06, cx + w * 0.34,
                 base - h * 0.02], fill=(220, 220, 214))
    d.ellipse([cx - w * 0.22, base - h * 0.52, cx + w * 0.22,
               base - h * 0.08], fill=(245, 245, 240))
    d.rectangle([cx - w * 0.03, base - h * 0.62, cx + w * 0.03,
                 base - h * 0.50], fill=(245, 245, 240))
    d.ellipse([cx - 4, base - h * 0.66, cx + 4, base - h * 0.58],
              fill=(245, 245, 240))
    for k in range(5):
        wx = cx - w * 0.24 + k * w * 0.12
        d.rectangle([wx, base - h * 0.20, wx + w * 0.05, base - h * 0.10],
                    fill=(180, 180, 172))
    # big 258
    d.text((cx, base - h * 0.34), "258", font=load(BOLD, 44), fill=RED,
           anchor="ma")
    d.rectangle([x, base, x + w, y + h], fill=(24, 44, 78))
    # ballot box at the foot
    bx = x + w * 0.10
    d.rectangle([bx, y + h - 30, bx + 56, y + h - 6], fill=(178, 48, 40))
    d.rectangle([bx - 4, y + h - 36, bx + 60, y + h - 30], fill=(140, 36, 30))
    d.rectangle([bx + 18, y + h - 44, bx + 38, y + h - 36],
                fill=(255, 255, 255), outline=INK, width=1)


def scene_indonesia(d, x, y, w, h):
    """A three-storey factory in flames: orange fire at the windows,
    a thick smoke column, and a red rescue ladder against the wall."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 214))
    base = y + h - h * 0.16
    # factory block
    d.rectangle([x + w * 0.10, base - h * 0.62, x + w * 0.90, base],
                fill=(150, 140, 128))
    d.rectangle([x + w * 0.08, base - h * 0.68, x + w * 0.92,
                 base - h * 0.62], fill=(110, 102, 92))
    # windows: two burning, the rest dark
    for wx in (0.16, 0.32, 0.48, 0.64, 0.78):
        wy0 = base - h * 0.52
        d.rectangle([x + w * wx, wy0, x + w * (wx + 0.08), wy0 + h * 0.12],
                    fill=(60, 56, 50))
    for wx in (0.32, 0.64):
        wy0 = base - h * 0.34
        d.rectangle([x + w * wx, wy0, x + w * (wx + 0.08), wy0 + h * 0.12],
                    fill=(240, 120, 40))
        d.rectangle([x + w * wx, wy0 + h * 0.06, x + w * (wx + 0.08),
                     wy0 + h * 0.12], fill=(255, 205, 90))
    # ground-floor fire glow
    fx = x + w * 0.50
    d.ellipse([fx - w * 0.16, base - h * 0.18, fx + w * 0.16, base + h * 0.02],
              fill=(235, 110, 40))
    d.ellipse([fx - w * 0.08, base - h * 0.12, fx + w * 0.08, base],
              fill=(255, 205, 90))
    # thick smoke column
    for ox, oy, rr in ((-0.04, -0.68, 0.07), (0.03, -0.76, 0.08),
                       (-0.01, -0.82, 0.06)):
        px, py = fx + w * ox, base + h * oy
        d.ellipse([px - h * rr, py - h * rr, px + h * rr, py + h * rr],
                  fill=(80, 80, 88))
    # rescue ladder, left side
    lx = x + w * 0.14
    d.line([lx, base - h * 0.56, lx + w * 0.05, base], fill=(200, 60, 40),
           width=3)
    d.line([lx + w * 0.04, base - h * 0.56, lx + w * 0.09, base],
           fill=(200, 60, 40), width=3)
    d.rectangle([x, base, x + w, y + h], fill=(120, 112, 100))


# ------------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (PAGE, PAGE), PAPER)
    d = ImageDraw.Draw(img)
    M = 36

    d.text((PAGE / 2, 18), "T H E   W O R L D   I N   O N E   I M A G E",
           font=load(BOLD, 26), fill=INK, anchor="ma")
    date_font = load(BOLD, 62)
    while d.textlength("SUNDAY 22 NOVEMBER 2026", font=date_font) > PAGE - 2 * M:
        date_font = load(BOLD, date_font.size - 2)
    d.text((PAGE / 2, 52), "SUNDAY 22 NOVEMBER 2026", font=date_font,
           fill=INK, anchor="ma")
    d.line([M, 138, PAGE - M, 138], fill=INK, width=5)
    d.line([M, 146, PAGE - M, 146], fill=INK, width=2)

    # lead: COP31 collapses with no deal
    d.rectangle([M, 162, PAGE - M, 442], outline=INK, width=3)
    scene_cop31(d, M + 10, 172, 452, 260)
    lx = M + 486
    d.text((lx, 180), "CLIMATE \u00b7 COP31", font=load(BOLD, 22), fill=RED)
    y = block(d, lx, 212, "COP31 COLLAPSES WITH NO DEAL",
              load(BOLD, 40), INK, PAGE - M - lx - 8)
    block(d, lx, y + 8,
          "The EU rejects the \u2018Antalya Pact\u2019 draft with no "
          "mention of fossil fuels; the longest climate summit ever "
          "ends empty-handed.",
          load(PLAIN, 22), GREY, PAGE - M - lx - 8)

    # row of three
    y0, y1 = 456, 716
    cw = (PAGE - 2 * M - 24) // 3
    cells = [
        (scene_dymer, "UKRAINE \u00b7 WAR",
         "DRONE HITS FLAT BLOCK NEAR KYIV",
         "A Russian drone destroys part of a five-storey block in "
         "Dymer; 14 missing, nine pulled out."),
        (scene_bahrain, "GULF \u00b7 IRAN\u2013US",
         "BAHRAIN COUNTS TWO HURT",
         "Iran claims it hit US Patriot radars; Bahrain says a "
         "factory site was hit, one victim critical."),
        (scene_westbank, "WEST BANK \u00b7 ARSON",
         "SETTLERS TORCH CARS IN 4 VILLAGES",
         "A dozen vehicles burned overnight near Ramallah; Israel "
         "opens an investigation."),
    ]
    for i, (scene, tag, head, body) in enumerate(cells):
        x0 = M + i * (cw + 12)
        d.rectangle([x0, y0, x0 + cw, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, cw - 16, 84)
        panel_text(d, x0 + 12, y0 + 102, cw - 24, tag, head, body,
                   head_size=24, body_size=17)

    # row of two
    y0, y1 = 730, 950
    cw2 = (PAGE - 2 * M - 12) // 2
    cells2 = [
        (scene_democrats, "USA \u00b7 MIDTERMS",
         "DEMOCRATS TAKE 258 SEATS",
         "A North Carolina recount hands Chuck Hubbard the 258th "
         "seat \u2014 the biggest since 1992; Democrats also take "
         "the Senate."),
        (scene_indonesia, "INDONESIA \u00b7 DISASTER",
         "FACTORY FIRE KILLS 3, 36 MISSING",
         "Blaze sweeps the Milkita sweets plant in Banten; rescuers "
         "search the ruins a day on."),
    ]
    for i, (scene, tag, head, body) in enumerate(cells2):
        x0 = M + i * (cw2 + 12)
        d.rectangle([x0, y0, x0 + cw2, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, 168, y1 - y0 - 16)
        panel_text(d, x0 + 188, y0 + 12, cw2 - 200, tag, head, body,
                   head_size=24)

    d.line([M, 958, PAGE - M, 958], fill=INK, width=3)
    block(d, M, 966,
          "ALSO TODAY \u00b7 US warns Americans in Bahrain after the "
          "strikes \u00b7 Delta delays 1,000+ flights after a "
          "Microsoft outage \u00b7 Russia starts towing its drone-hit "
          "ship in the Baltic",
          load(BOLD, 18), INK, PAGE - 2 * M, centre=True)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
