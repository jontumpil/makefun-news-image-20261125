# draw_frontpage.py -- stdlib-only front-page renderer.
# Canvas 1024x1024 RGB newsprint, 5x7 bitmap font, PNG writer/reader
# built on struct + zlib only. No third-party code anywhere.
# Illustrated photos are composited with a pure-stdlib PNG reader
# and area-average downscaling. All captions are drawn by the
# renderer, never baked into the images.

import os
import struct
import zlib

# ---------------------------------------------------------------- font

# 5x7 glyphs: 7 rows of 5 cells, '#' = ink, '.' = paper.
FONT = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01110", "10001", "10000", "10000", "10000", "10001", "01110"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01110", "10001", "10000", "10111", "10001", "10001", "01111"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("01110", "00100", "00100", "00100", "00100", "00100", "01110"),
    "J": ("00111", "00010", "00010", "00010", "00010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "11011", "10001"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00110", "01000", "10000", "11111"),
    "3": ("11111", "00010", "00100", "00010", "00001", "10001", "01110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "11110", "00001", "00001", "10001", "01110"),
    "6": ("00110", "01000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00010", "01100"),
    " ": ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
    ".": ("00000", "00000", "00000", "00000", "00000", "01100", "01100"),
    ",": ("00000", "00000", "00000", "00000", "01100", "00100", "01000"),
    ":": ("00000", "01100", "01100", "00000", "01100", "01100", "00000"),
    ";": ("00000", "01100", "01100", "00000", "01100", "00100", "01000"),
    "'": ("00100", "00100", "01000", "00000", "00000", "00000", "00000"),
    "-": ("00000", "00000", "00000", "01110", "00000", "00000", "00000"),
    "(": ("00010", "00100", "01000", "01000", "01000", "00100", "00010"),
    ")": ("01000", "00100", "00010", "00010", "00010", "00100", "01000"),
    "/": ("00001", "00010", "00010", "00100", "01000", "01000", "10000"),
    "&": ("01100", "10010", "10100", "01000", "10101", "10010", "01101"),
    "!": ("00100", "00100", "00100", "00100", "00100", "00000", "00100"),
    "?": ("01110", "10001", "00001", "00110", "00100", "00000", "00100"),
    "%": ("11001", "11010", "00010", "00100", "01000", "01011", "10011"),
    "+": ("00000", "00100", "00100", "11111", "00100", "00100", "00000"),
    '"': ("01010", "01010", "00000", "00000", "00000", "00000", "00000"),
    "*": ("00000", "10101", "01110", "11111", "01110", "10101", "00000"),
    "=": ("00000", "00000", "11111", "00000", "11111", "00000", "00000"),
}

CHAR_W = 6  # glyph advance in font units (5 px + 1 px gap)


def text_width(text, scale):
    """Pixel width of text at the given scale."""
    return len(text) * CHAR_W * scale


def wrap_text(text, max_chars):
    """Greedy word wrap; returns a list of lines, each <= max_chars."""
    words = text.split(" ")
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if len(trial) <= max_chars:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- canvas

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (26, 26, 26)
RED = (163, 22, 33)
BLUE = (31, 56, 100)
GRAY = (107, 107, 107)
RULE = (180, 170, 150)


class Canvas(object):
    """RGB canvas backed by a flat bytearray."""

    def __init__(self, width, height, color):
        self.w = width
        self.h = height
        self.px = bytearray(color * (width * height))

    def set_pixel(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            self.px[i] = color[0]
            self.px[i + 1] = color[1]
            self.px[i + 2] = color[2]

    def fill_rect(self, x, y, w, h, color):
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(self.w, x + w)
        y1 = min(self.h, y + h)
        row = bytes(color) * (x1 - x0)
        for yy in range(y0, y1):
            i = (yy * self.w + x0) * 3
            self.px[i:i + len(row)] = row

    def hline(self, x, y, w, color, thick=1):
        self.fill_rect(x, y, w, thick, color)

    def draw_text(self, x, y, text, scale, color):
        """Draw upper-cased text with the 5x7 font."""
        text = text.upper()
        cx = x
        for ch in text:
            glyph = FONT.get(ch)
            if glyph is None:
                cx += CHAR_W * scale
                continue
            for row in range(7):
                bits = glyph[row]
                for col in range(5):
                    if bits[col] == "1":
                        self.fill_rect(
                            cx + col * scale, y + row * scale,
                            scale, scale, color)
            cx += CHAR_W * scale
        return cx

    def draw_text_centered(self, y, text, scale, color, cx=512):
        tw = text_width(text, scale)
        return self.draw_text(cx - tw // 2, y, text, scale, color)


# ---------------------------------------------------------------- PNG io


def _chunk(ctype, data):
    out = struct.pack(">I", len(data)) + ctype + data
    out += struct.pack(">I", zlib.crc32(ctype + data) & 0xFFFFFFFF)
    return out


def write_png(path, canvas):
    """Write the canvas as a deterministic 8-bit RGB PNG."""
    raw = bytearray()
    stride = canvas.w * 3
    for y in range(canvas.h):
        raw.append(0)  # filter: none
        start = y * stride
        raw += canvas.px[start:start + stride]
    ihdr = struct.pack(">IIBBBBB", canvas.w, canvas.h, 8, 2, 0, 0, 0)
    blob = (
        b"\x89PNG\r\n\x1a\n"
        + _chunk(b"IHDR", ihdr)
        + _chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + _chunk(b"IEND", b"")
    )
    with open(path, "wb") as fh:
        fh.write(blob)


def _paeth(a, b, c):
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def read_png(path):
    """Read an 8-bit non-interlaced RGB/RGBA PNG into (w, h, rows).

    Rows are lists of (r, g, b) tuples. Only the filter types 0-4
    and color types 2 and 6 are needed for our generated assets.
    """
    with open(path, "rb") as fh:
        data = fh.read()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG file"
    pos = 8
    idat = bytearray()
    width = height = bitdepth = colortype = None
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + length]
        if ctype == b"IHDR":
            width, height, bitdepth, colortype = struct.unpack(
                ">IIBB", chunk[:10])
        elif ctype == b"IDAT":
            idat += chunk
        elif ctype == b"IEND":
            break
        pos += 12 + length
    assert bitdepth == 8, "only 8-bit PNG supported"
    assert colortype in (2, 6), "only RGB/RGBA PNG supported"
    channels = 3 if colortype == 2 else 4
    raw = zlib.decompress(bytes(idat))
    stride = width * channels
    rows = []
    prev = bytearray(stride)
    p = 0
    for _y in range(height):
        ftype = raw[p]
        p += 1
        line = bytearray(raw[p:p + stride])
        p += stride
        if ftype == 1:
            for i in range(channels, stride):
                line[i] = (line[i] + line[i - channels]) & 0xFF
        elif ftype == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 0xFF
        elif ftype == 3:
            for i in range(stride):
                left = line[i - channels] if i >= channels else 0
                line[i] = (line[i] + ((left + prev[i]) >> 1)) & 0xFF
        elif ftype == 4:
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                b = prev[i]
                c = prev[i - channels] if i >= channels else 0
                line[i] = (line[i] + _paeth(a, b, c)) & 0xFF
        prev = line
        row = []
        for x in range(width):
            o = x * channels
            row.append((line[o], line[o + 1], line[o + 2]))
        rows.append(row)
    return width, height, rows


def blit_image(canvas, path, x, y, w, h):
    """Center-crop + area-average the source PNG into the box."""
    sw, sh, rows = read_png(path)
    src_ratio = sw / float(sh)
    box_ratio = w / float(h)
    if src_ratio > box_ratio:
        # source is wider: crop left/right
        crop_w = int(sh * box_ratio)
        ox = (sw - crop_w) // 2
        oy = 0
        cw, ch = crop_w, sh
    else:
        crop_h = int(sw / box_ratio)
        ox = 0
        oy = (sh - crop_h) // 2
        cw, ch = sw, crop_h
    for dy in range(h):
        sy0 = oy + int(dy * ch / h)
        sy1 = oy + int((dy + 1) * ch / h)
        if sy1 <= sy0:
            sy1 = sy0 + 1
        for dx in range(w):
            sx0 = ox + int(dx * cw / w)
            sx1 = ox + int((dx + 1) * cw / w)
            if sx1 <= sx0:
                sx1 = sx0 + 1
            r = g = b = n = 0
            for sy in range(sy0, min(sy1, sh)):
                srow = rows[sy]
                for sx in range(sx0, min(sx1, sw)):
                    pr, pg, pb = srow[sx]
                    r += pr
                    g += pg
                    b += pb
                    n += 1
            canvas.set_pixel(x + dx, y + dy,
                             (r // n, g // n, b // n))


# Vertical budget (1024 px tall): masthead 14-72, title 82-108,
# hero 120-362, cards 374-556, index 568-880, DATE CHECK 892-968,
# footer 984. The index columns end near y=874, leaving a clean
# gap before the DATE CHECK box. Keep section heights in sync here
# if the story count changes.

MARGIN = 24
CONTENT_W = W - 2 * MARGIN


def render(base_dir, output_path):
    """Render the front page and write it to output_path."""
    import stories

    cv = Canvas(W, H, PAPER)

    # ---- masthead ----
    cv.draw_text_centered(14, "THE WORLD IN ONE DAY", 4, INK)
    cv.draw_text_centered(50, "WEDNESDAY 25 NOVEMBER 2026", 2, RED)
    cv.hline(MARGIN, 72, CONTENT_W, INK, 3)

    # ---- title formula line ----
    y = 82
    for line in wrap_text(stories.TITLE_LINE, 158):
        cv.draw_text(MARGIN, y, line, 1, INK)
        y += 11
    cv.hline(MARGIN, 108, CONTENT_W, INK, 2)

    # ---- hero: illustrated lead story ----
    img, kicker, headline, blurb, source, tag = stories.HERO
    hy = 120
    blit_image(cv, os.path.join(base_dir, img), MARGIN, hy, 470, 230)
    tx = MARGIN + 470 + 16
    tw = W - MARGIN - tx
    cv.draw_text(tx, hy, kicker, 1, RED)
    yy = hy + 14
    for line in wrap_text(headline, tw // 12):
        cv.draw_text(tx, yy, line, 2, INK)
        yy += 16
    yy += 4
    for line in wrap_text(blurb, tw // 6):
        cv.draw_text(tx, yy, line, 1, INK)
        yy += 11
    yy += 6
    cv.draw_text(tx, yy, source + " -- " + tag, 1, GRAY)
    cv.hline(MARGIN, 362, CONTENT_W, RULE, 1)

    # ---- three illustrated cards ----
    card_w = 320
    card_x = [MARGIN, MARGIN + 328, MARGIN + 656]
    cy = 374
    for (cimg, ckick, chead, cblurb, csrc, ctag), cx in zip(
            stories.CARDS, card_x):
        blit_image(cv, os.path.join(base_dir, cimg), cx, cy, card_w, 100)
        yy = cy + 108
        cv.draw_text(cx, yy, ckick, 1, RED)
        yy += 12
        for line in wrap_text(chead, card_w // 6):
            cv.draw_text(cx, yy, line, 1, INK)
            yy += 11
        yy += 2
        for line in wrap_text(cblurb, card_w // 6):
            cv.draw_text(cx, yy, line, 1, GRAY)
            yy += 11
        yy += 2
        cv.draw_text(cx, yy, csrc + " -- " + ctag, 1, GRAY)
    cv.hline(MARGIN, 556, CONTENT_W, INK, 2)

    # ---- story index: two columns, seven regions ----
    left_regions = ["NORTH AMERICA", "LATIN AMERICA", "EUROPE",
                    "MIDDLE EAST"]
    right_regions = ["AFRICA", "ASIA-PACIFIC", "SCIENCE & CULTURE"]
    col_w = 476
    ly = 568
    ry = 568
    for regions, x0, y0 in ((left_regions, MARGIN, ly),
                            (right_regions, MARGIN + 500, ry)):
        yy = y0
        for region in regions:
            cv.draw_text(x0, yy, region, 1, BLUE)
            cv.hline(x0, yy + 10, col_w, BLUE, 1)
            yy += 16
            for (headline, source, tag) in stories.stories_by_region(region):
                mark = "C" if tag == "CONFIRMED" else "R"
                line = headline + " -- " + source + " [" + mark + "]"
                cv.fill_rect(x0, yy + 2, 4, 4, RED)
                cv.draw_text(x0 + 10, yy, line, 1, INK)
                yy += 12
            yy += 4

    # ---- DATE CHECK box + footer ----
    box_y = 892
    cv.fill_rect(MARGIN, box_y, CONTENT_W, 2, RED)
    cv.fill_rect(MARGIN, box_y + 76, CONTENT_W, 2, RED)
    yy = box_y + 10
    for line in wrap_text(stories.DATE_CHECK_TEXT, 158):
        cv.draw_text(MARGIN + 4, yy, line, 1, INK)
        yy += 11
    cv.draw_text_centered(984, stories.FOOTER_TEXT, 1, GRAY)

    write_png(output_path, cv)
    return output_path
