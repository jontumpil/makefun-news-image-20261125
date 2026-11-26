"""Render THE WORLD IN ONE DAY as a 1024x1024 PNG, stdlib only.

A 5x7 bitmap font, a small canvas, a PNG decoder for the photo
assets, and a PNG encoder for the finished front page. No third
party code is used anywhere in this file.
"""

import os
import struct
import zlib

# Each glyph is seven rows of five bits, top row first.
# A set bit is ink; bit 4 is the leftmost pixel of the row.
FONT = {
    "A": (0x0E, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "B": (0x1E, 0x11, 0x11, 0x1E, 0x11, 0x11, 0x1E),
    "C": (0x0E, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0E),
    "D": (0x1E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x1E),
    "E": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x1F),
    "F": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x10),
    "G": (0x0E, 0x11, 0x10, 0x17, 0x11, 0x11, 0x0F),
    "H": (0x11, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "I": (0x0E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "J": (0x07, 0x02, 0x02, 0x02, 0x02, 0x12, 0x0C),
    "K": (0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11),
    "L": (0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1F),
    "M": (0x11, 0x1B, 0x15, 0x15, 0x11, 0x11, 0x11),
    "N": (0x11, 0x19, 0x15, 0x13, 0x11, 0x11, 0x11),
    "O": (0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "P": (0x1E, 0x11, 0x11, 0x1E, 0x10, 0x10, 0x10),
    "Q": (0x0E, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0D),
    "R": (0x1E, 0x11, 0x11, 0x1E, 0x14, 0x12, 0x11),
    "S": (0x0F, 0x10, 0x10, 0x0E, 0x01, 0x01, 0x1E),
    "T": (0x1F, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04),
    "U": (0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "V": (0x11, 0x11, 0x11, 0x11, 0x11, 0x0A, 0x04),
    "W": (0x11, 0x11, 0x11, 0x15, 0x15, 0x15, 0x0A),
    "X": (0x11, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x11),
    "Y": (0x11, 0x11, 0x0A, 0x04, 0x04, 0x04, 0x04),
    "Z": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1F),
    "a": (0x00, 0x00, 0x0E, 0x01, 0x0F, 0x11, 0x0F),
    "b": (0x10, 0x10, 0x1E, 0x11, 0x11, 0x11, 0x1E),
    "c": (0x00, 0x00, 0x0E, 0x10, 0x10, 0x11, 0x0E),
    "d": (0x01, 0x01, 0x0F, 0x11, 0x11, 0x11, 0x0F),
    "e": (0x00, 0x00, 0x0E, 0x11, 0x1F, 0x10, 0x0E),
    "f": (0x06, 0x08, 0x08, 0x1E, 0x08, 0x08, 0x08),
    "g": (0x00, 0x0F, 0x11, 0x11, 0x0F, 0x01, 0x0E),
    "h": (0x10, 0x10, 0x1E, 0x11, 0x11, 0x11, 0x11),
    "i": (0x04, 0x00, 0x0C, 0x04, 0x04, 0x04, 0x0E),
    "j": (0x02, 0x00, 0x06, 0x02, 0x02, 0x12, 0x0C),
    "k": (0x10, 0x10, 0x12, 0x14, 0x18, 0x14, 0x12),
    "l": (0x0C, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "m": (0x00, 0x00, 0x1A, 0x15, 0x15, 0x15, 0x15),
    "n": (0x00, 0x00, 0x1E, 0x11, 0x11, 0x11, 0x11),
    "o": (0x00, 0x00, 0x0E, 0x11, 0x11, 0x11, 0x0E),
    "p": (0x00, 0x00, 0x1E, 0x11, 0x11, 0x1E, 0x10),
    "q": (0x00, 0x00, 0x0F, 0x11, 0x11, 0x0F, 0x01),
    "r": (0x00, 0x00, 0x16, 0x19, 0x10, 0x10, 0x10),
    "s": (0x00, 0x00, 0x0F, 0x10, 0x0E, 0x01, 0x1E),
    "t": (0x08, 0x08, 0x1E, 0x08, 0x08, 0x08, 0x06),
    "u": (0x00, 0x00, 0x11, 0x11, 0x11, 0x13, 0x0D),
    "v": (0x00, 0x00, 0x11, 0x11, 0x11, 0x0A, 0x04),
    "w": (0x00, 0x00, 0x11, 0x11, 0x15, 0x15, 0x0A),
    "x": (0x00, 0x00, 0x11, 0x0A, 0x04, 0x0A, 0x11),
    "y": (0x00, 0x00, 0x11, 0x11, 0x0F, 0x01, 0x0E),
    "z": (0x00, 0x00, 0x1F, 0x02, 0x04, 0x08, 0x1F),
    "0": (0x0E, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0E),
    "1": (0x04, 0x0C, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "2": (0x0E, 0x11, 0x01, 0x06, 0x08, 0x10, 0x1F),
    "3": (0x1F, 0x02, 0x04, 0x02, 0x01, 0x11, 0x0E),
    "4": (0x02, 0x06, 0x0A, 0x12, 0x1F, 0x02, 0x02),
    "5": (0x1F, 0x10, 0x1E, 0x01, 0x01, 0x11, 0x0E),
    "6": (0x06, 0x08, 0x10, 0x1E, 0x11, 0x11, 0x0E),
    "7": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08),
    "8": (0x0E, 0x11, 0x11, 0x0E, 0x11, 0x11, 0x0E),
    "9": (0x0E, 0x11, 0x11, 0x0F, 0x01, 0x02, 0x0C),
    " ": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    "!": (0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04),
    '"': (0x0A, 0x0A, 0x0A, 0x00, 0x00, 0x00, 0x00),
    "#": (0x0A, 0x0A, 0x1F, 0x0A, 0x1F, 0x0A, 0x0A),
    "$": (0x04, 0x0F, 0x14, 0x0E, 0x05, 0x1E, 0x04),
    "%": (0x19, 0x1A, 0x02, 0x04, 0x08, 0x0B, 0x13),
    "&": (0x0C, 0x12, 0x14, 0x08, 0x15, 0x12, 0x0D),
    "'": (0x04, 0x04, 0x08, 0x00, 0x00, 0x00, 0x00),
    "(": (0x02, 0x04, 0x08, 0x08, 0x08, 0x04, 0x02),
    ")": (0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08),
    "*": (0x00, 0x04, 0x15, 0x0E, 0x15, 0x04, 0x00),
    "+": (0x00, 0x04, 0x04, 0x1F, 0x04, 0x04, 0x00),
    ",": (0x00, 0x00, 0x00, 0x00, 0x04, 0x04, 0x08),
    "-": (0x00, 0x00, 0x00, 0x0E, 0x00, 0x00, 0x00),
    ".": (0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C),
    "/": (0x01, 0x02, 0x02, 0x04, 0x08, 0x08, 0x10),
    ":": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x0C, 0x00),
    ";": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x0C, 0x08),
    "<": (0x02, 0x04, 0x08, 0x10, 0x08, 0x04, 0x02),
    "=": (0x00, 0x00, 0x1F, 0x00, 0x1F, 0x00, 0x00),
    ">": (0x08, 0x04, 0x02, 0x01, 0x02, 0x04, 0x08),
    "?": (0x0E, 0x11, 0x01, 0x06, 0x04, 0x00, 0x04),
    "@": (0x0E, 0x11, 0x17, 0x15, 0x16, 0x10, 0x0E),
    "[": (0x0E, 0x08, 0x08, 0x08, 0x08, 0x08, 0x0E),
    "]": (0x0E, 0x02, 0x02, 0x02, 0x02, 0x02, 0x0E),
    "_": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F),
    "{": (0x06, 0x08, 0x08, 0x1C, 0x08, 0x08, 0x06),
    "|": (0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04),
    "}": (0x0C, 0x02, 0x02, 0x07, 0x02, 0x02, 0x0C),
    "~": (0x00, 0x00, 0x09, 0x16, 0x00, 0x00, 0x00),
}

UNKNOWN_GLYPH = (0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E)


PAGE_W = 1024
PAGE_H = 1024
PAPER = (252, 250, 244)
INK = (18, 18, 18)
RULE = (120, 115, 105)
FAINT = (90, 86, 78)

CHAR_W = 6
CHAR_H = 7


class Canvas:
    """An RGB canvas backed by one flat bytearray."""

    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        r, g, b = colour
        self.buf = bytearray([r, g, b] * (width * height))

    def set_pixel(self, x, y, colour):
        if 0 <= x < self.width and 0 <= y < self.height:
            i = (y * self.width + x) * 3
            self.buf[i] = colour[0]
            self.buf[i + 1] = colour[1]
            self.buf[i + 2] = colour[2]

    def fill_rect(self, x, y, w, h, colour):
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(self.width, x + w)
        y1 = min(self.height, y + h)
        r, g, b = colour
        for yy in range(y0, y1):
            base = (yy * self.width + x0) * 3
            for xx in range(x0, x1):
                i = base + (xx - x0) * 3
                self.buf[i] = r
                self.buf[i + 1] = g
                self.buf[i + 2] = b

    def hline(self, x, y, w, colour):
        self.fill_rect(x, y, w, 1, colour)

    def rect(self, x, y, w, h, colour):
        self.hline(x, y, w, colour)
        self.hline(x, y + h - 1, w, colour)
        self.fill_rect(x, y, 1, h, colour)
        self.fill_rect(x + w - 1, y, 1, h, colour)


def glyph_for(ch):
    return FONT.get(ch, UNKNOWN_GLYPH)


def text_width(text, scale=1, pitch=CHAR_W):
    return len(text) * pitch * scale


def draw_text(canvas, x, y, text, colour=INK, scale=1, pitch=CHAR_W):
    """Draw one line of text; returns the x just past the text."""
    cx = x
    for ch in text:
        rows = glyph_for(ch)
        for ry in range(CHAR_H):
            bits = rows[ry]
            for rx in range(5):
                if bits & (1 << (4 - rx)):
                    if scale == 1:
                        canvas.set_pixel(cx + rx, y + ry, colour)
                    else:
                        canvas.fill_rect(
                            cx + rx * scale, y + ry * scale,
                            scale, scale, colour)
        cx += pitch * scale
    return cx


def draw_text_centred(canvas, cx, y, text, colour=INK, scale=1,
                      pitch=CHAR_W):
    x = cx - text_width(text, scale, pitch) // 2
    draw_text(canvas, x, y, text, colour, scale, pitch)
    return x


def wrap_text(text, max_width, scale=1, pitch=CHAR_W):
    """Greedy word wrap; returns a list of lines fitting max_width."""
    limit = max(1, max_width // (pitch * scale))
    lines = []
    for chunk in text.split("\n"):
        words = chunk.split()
        if not words:
            lines.append("")
            continue
        line = words[0]
        for word in words[1:]:
            if len(line) + 1 + len(word) <= limit:
                line += " " + word
            else:
                lines.append(line)
                line = word
        lines.append(line)
    return lines


def _paeth(left, up, up_left):
    pred = left + up - up_left
    pa = abs(pred - left)
    pb = abs(pred - up)
    pc = abs(pred - up_left)
    if pa <= pb and pa <= pc:
        return left
    if pb <= pc:
        return up
    return up_left


def read_png(path):
    """Decode an 8-bit non-interlaced PNG to (width, height, rgb bytes).

    Handles colour types 0 (grey), 2 (RGB), 3 (palette), 4 (grey+alpha)
    and 6 (RGBA), with all five PNG row filters.
    """
    with open(path, "rb") as handle:
        data = handle.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file: " + path)
    pos = 8
    width = height = None
    bit_depth = colour = None
    interlace = 0
    palette = b""
    raw = b""
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        body = data[pos + 8:pos + 8 + length]
        if kind == b"IHDR":
            width, height, bit_depth, colour, _, _, interlace = struct.unpack(
                ">IIBBBBB", body)
        elif kind == b"PLTE":
            palette = body
        elif kind == b"IDAT":
            raw += body
        elif kind == b"IEND":
            break
        pos += 12 + length
    if bit_depth != 8:
        raise ValueError("only 8-bit PNG supported: " + path)
    if interlace != 0:
        raise ValueError("interlaced PNG not supported: " + path)
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[colour]
    stride = width * channels
    scan = zlib.decompress(raw)
    out = bytearray(width * height * 3)
    prev = bytearray(stride)
    p = 0
    for y in range(height):
        ftype = scan[p]
        p += 1
        row = bytearray(scan[p:p + stride])
        p += stride
        for i in range(stride):
            left = row[i - channels] if i >= channels else 0
            up = prev[i]
            up_left = prev[i - channels] if i >= channels else 0
            if ftype == 1:
                row[i] = (row[i] + left) & 0xFF
            elif ftype == 2:
                row[i] = (row[i] + up) & 0xFF
            elif ftype == 3:
                row[i] = (row[i] + (left + up) // 2) & 0xFF
            elif ftype == 4:
                row[i] = (row[i] + _paeth(left, up, up_left)) & 0xFF
        prev = row
        for x in range(width):
            o = (y * width + x) * 3
            s = x * channels
            if colour == 2:
                out[o:o + 3] = row[s:s + 3]
            elif colour == 6:
                out[o:o + 3] = row[s:s + 3]
            elif colour == 0:
                out[o] = out[o + 1] = out[o + 2] = row[s]
            elif colour == 4:
                out[o] = out[o + 1] = out[o + 2] = row[s]
            elif colour == 3:
                idx = row[s] * 3
                out[o:o + 3] = palette[idx:idx + 3]
    return width, height, bytes(out)


def blit_photo(canvas, path, dx, dy, dw, dh, crop_top=0.0, crop_bottom=1.0):
    """Draw a photo scaled into a rectangle, sampling a vertical band.

    Four samples per destination pixel smooth the heavy downscale
    from a 1920-pixel source to a small newspaper card.
    """
    sw, sh, rgb = read_png(path)
    y0 = int(sh * crop_top)
    y1 = int(sh * crop_bottom)
    for py in range(dh):
        sy = y0 + (py + 0.5) * (y1 - y0) / dh
        for px in range(dw):
            sx = (px + 0.5) * sw / dw
            total_r = total_g = total_b = 0
            for ox, oy in ((0.25, 0.25), (0.75, 0.25),
                           (0.25, 0.75), (0.75, 0.75)):
                ix = min(sw - 1, max(0, int(sx - 0.5 + ox)))
                iy = min(sh - 1, max(0, int(sy - 0.5 + oy)))
                k = (iy * sw + ix) * 3
                total_r += rgb[k]
                total_g += rgb[k + 1]
                total_b += rgb[k + 2]
            canvas.set_pixel(dx + px, dy + py, (
                total_r // 4, total_g // 4, total_b // 4))


def write_png(path, width, height, rgb):
    """Encode RGB bytes as a deterministic 8-bit PNG (filter 0)."""
    raw = bytearray()
    stride = width * 3
    for y in range(height):
        raw.append(0)
        raw += rgb[y * stride:(y + 1) * stride]
    comp = zlib.compress(bytes(raw), 9)

    def chunk(kind, body):
        out = struct.pack(">I", len(body)) + kind + body
        out += struct.pack(">I", zlib.crc32(kind + body) & 0xFFFFFFFF)
        return out

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", ihdr)
    png += chunk(b"IDAT", comp)
    png += chunk(b"IEND", b"")
    with open(path, "wb") as handle:
        handle.write(png)


MARGIN = 14
GUTTER = 10
NCOLS = 5
COL_W = (PAGE_W - 2 * MARGIN - (NCOLS - 1) * GUTTER) // NCOLS
COL_X = [MARGIN + i * (COL_W + GUTTER) for i in range(NCOLS)]
BODY_PITCH = 5
LEAD = 7
STORY_GAP = 2
CARD_H = 72


def story_lines(story):
    head = wrap_text(story["headline"], COL_W, pitch=BODY_PITCH)
    body = wrap_text(story["summary"], COL_W, pitch=BODY_PITCH)
    return head, body


def story_height(story):
    head, body = story_lines(story)
    return len(head) * LEAD + len(body) * LEAD + LEAD + STORY_GAP


def card_height(caption):
    lines = wrap_text(caption, COL_W, pitch=BODY_PITCH)
    return CARD_H + 2 + 3 + len(lines) * LEAD + 4


def draw_story(canvas, x, y, story):
    head, body = story_lines(story)
    for line in head:
        draw_text(canvas, x, y, line, INK, 1, BODY_PITCH)
        y += LEAD
    for line in body:
        draw_text(canvas, x, y, line, INK, 1, BODY_PITCH)
        y += LEAD
    meta = "%s - %s - %s" % (
        story["region"], story["source"], story["tag"])
    draw_text(canvas, x, y, meta, FAINT, 1, BODY_PITCH)
    y += LEAD
    canvas.hline(x, y, COL_W, RULE)
    y += STORY_GAP
    return y


def draw_card(canvas, base, x, y, story, asset, caption):
    path = os.path.join(base, asset)
    canvas.rect(x - 1, y - 1, COL_W + 2, CARD_H + 2, INK)
    blit_photo(canvas, path, x, y, COL_W, CARD_H, 0.15, 0.85)
    y += CARD_H + 2 + 3
    for line in wrap_text(caption, COL_W, pitch=BODY_PITCH):
        draw_text(canvas, x, y, line, INK, 1, BODY_PITCH)
        y += LEAD
    y += 4
    return y


DATECHECK_LINES = [
    "DATE CHECK: Every story in this edition is dated Wednesday "
    "25 November 2026. Sources named below.",
    "C = CONFIRMED (named source, same-day report). "
    "R = REPORTED (single wire or aggregator).",
]

LEAD_STORIES = [42, 21, 0, 35]


def assign_columns(stories, cards):
    """Five columns: four led by an illustrated story, one plain."""
    lead_ids = [i for i in LEAD_STORIES if i in cards]
    rest = [i for i in range(len(stories)) if i not in lead_ids]
    cols = [[i] for i in lead_ids]
    cols.append([])
    pos = 0
    for col in cols:
        while len(col) < 10 and pos < len(rest):
            col.append(rest[pos])
            pos += 1
    return cols


def render(base, stories, cards, title, date_line, out_path):
    """Render the front page and write it as a PNG. Returns column ends."""
    canvas = Canvas(PAGE_W, PAGE_H, PAPER)
    draw_text_centred(canvas, PAGE_W // 2, 6,
                      "THE WORLD IN ONE DAY", INK, 4)
    canvas.hline(MARGIN, 36, PAGE_W - 2 * MARGIN, INK)
    draw_text_centred(canvas, PAGE_W // 2, 40, date_line, INK, 1)
    draw_text_centred(canvas, PAGE_W // 2, 50, title, INK, 1)
    canvas.hline(MARGIN, 60, PAGE_W - 2 * MARGIN, INK)
    box_y = 66
    box_h = 30
    canvas.rect(MARGIN, box_y, PAGE_W - 2 * MARGIN, box_h, INK)
    for k, line in enumerate(DATECHECK_LINES):
        draw_text(canvas, MARGIN + 8, box_y + 4 + k * 8, line, INK, 1)
    top = 102
    cols = assign_columns(stories, cards)
    ends = []
    for c, col in enumerate(cols):
        x = COL_X[c]
        y = top
        for idx in col:
            story = stories[idx]
            if idx in cards:
                asset, caption = cards[idx]
                y = draw_card(canvas, base, x, y, story, asset, caption)
            y = draw_story(canvas, x, y, story)
        ends.append(y)
    footer = ("THE WORLD IN ONE DAY | WEDNESDAY 25 NOVEMBER 2026 | "
              "49 STORIES, 7 REGIONS | ALL STORIES DATED 25 NOVEMBER 2026")
    draw_text_centred(canvas, PAGE_W // 2, 1008, footer, FAINT, 1)
    write_png(out_path, PAGE_W, PAGE_H, bytes(canvas.buf))
    return ends
