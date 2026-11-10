"""Snap a render to the 4-shade DMG palette.

  dmgify.py SRC OUT BLOCK              opaque image, background in the darkest shade
  dmgify.py SRC OUT BLOCK --frame H    Firefox header image: console only, H-4 px tall,
                                       transparent, RIGHT px from the right edge (clear of
                                       Firefox's tab-strip buttons). OUT may be .svg, which
                                       stays sharp on high-DPI screens. Shades are
                                       worked out at BLOCK x the size, then sampled down,
                                       which keeps outlines thin at small sizes
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter

PAL = np.array([(15,56,15),(48,98,48),(139,172,15),(155,188,15)], np.uint8)

p = argparse.ArgumentParser()
p.add_argument('src'); p.add_argument('out'); p.add_argument('block', type=int)
p.add_argument('--frame', type=int, metavar='H')
p.add_argument('--right', type=int, default=100, help='frame mode: gap to the right edge')
args = p.parse_args()

g = Image.open(args.src).convert('L')
bg = int(np.median(np.asarray(g)[:20, :20]))                    # background tone from the top-left corner

def object_mask(img):
    a = np.asarray(img).astype(int)
    m = Image.fromarray(((np.abs(a - bg) > 6) * 255).astype(np.uint8))
    return np.asarray(m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))) > 0

if args.frame:                                                  # crop to the console, then shrink
    ys, xs = np.nonzero(object_mask(g))
    g = g.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    h = (args.frame - 4) * args.block
    g = g.resize((round(g.width * h / g.height), h), Image.LANCZOS)

a = np.asarray(g).astype(int)
mask = object_mask(g)
edges = np.asarray(g.filter(ImageFilter.FIND_EDGES)) > 12
lo, hi = np.percentile(a[mask], [20, 90])                        # shadows / body / highlights
lv = np.where(a < lo, 1, np.where(a < hi, 2, 3))
lv[edges] = 0                                                   # outlines: darkest
lv[~mask] = 0                                                   # background: darkest
b = args.block
rgb = PAL[lv[::b, ::b]].repeat(b, 0).repeat(b, 1)[:a.shape[0], :a.shape[1]]

if args.frame:
    alpha = (mask[::b, ::b] * 255).astype(np.uint8)
    art = Image.fromarray(np.dstack([PAL[lv[::b, ::b]], alpha]))
    if args.out.endswith('.svg'):                               # one <rect> per run of same-colour pixels
        hexes = ['#%02x%02x%02x' % tuple(c) for c in PAL]
        ids, on = lv[::b, ::b], alpha > 0
        rects = []
        for y in range(ids.shape[0]):
            x = 0
            while x < ids.shape[1]:
                if not on[y, x]: x += 1; continue
                x0 = x
                while x < ids.shape[1] and on[y, x] and ids[y, x] == ids[y, x0]: x += 1
                rects.append(f'<rect x="{x0}" y="{y + 2}" width="{x - x0}" height="1" fill="{hexes[ids[y, x0]]}"/>')
        w = ids.shape[1] + args.right
        with open(args.out, 'w') as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{args.frame}" '
                    f'viewBox="0 0 {w} {args.frame}" shape-rendering="crispEdges">' + ''.join(rects) + '</svg>\n')
        print(args.out, (w, args.frame), len(rects), 'rects')
        raise SystemExit
    out = Image.new('RGBA', (art.width + args.right, args.frame), (0, 0, 0, 0))
    out.paste(art, (0, 2))
    out.save(args.out)
else:
    Image.fromarray(rgb).save(args.out)
print(args.out, Image.open(args.out).size)
