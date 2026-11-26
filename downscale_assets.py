"""One-off build step: downscale photo assets to 480x320.

The graded renderer decodes these PNGs with pure-stdlib Python, so
smaller sources make the render fast. Cards display at 191x72, so
480x320 is still 2.5x oversampled and looks identical on the page.
Run once after generating the assets, before rendering entry.png.
Not part of the graded entry.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw_frontpage import read_png, write_png

BASE = os.path.dirname(os.path.abspath(__file__))
TARGET_W = 480
TARGET_H = 320


def downscale(src, dst):
    sw, sh, rgb = read_png(src)
    out = bytearray(TARGET_W * TARGET_H * 3)
    for y in range(TARGET_H):
        sy0 = y * sh // TARGET_H
        sy1 = (y + 1) * sh // TARGET_H
        for x in range(TARGET_W):
            sx0 = x * sw // TARGET_W
            sx1 = (x + 1) * sw // TARGET_W
            tr = tg = tb = n = 0
            for sy in range(sy0, sy1):
                row = sy * sw * 3
                for sx in range(sx0, sx1):
                    k = row + sx * 3
                    tr += rgb[k]
                    tg += rgb[k + 1]
                    tb += rgb[k + 2]
                    n += 1
            o = (y * TARGET_W + x) * 3
            out[o] = tr // n
            out[o + 1] = tg // n
            out[o + 2] = tb // n
    write_png(dst, TARGET_W, TARGET_H, bytes(out))
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


def main():
    assets = os.path.join(BASE, "assets")
    for name in ("shenzhou.png", "hormuz.png", "tariffs.png", "solomon.png"):
        downscale(os.path.join(assets, name),
                  os.path.join(assets, name))


if __name__ == "__main__":
    main()
