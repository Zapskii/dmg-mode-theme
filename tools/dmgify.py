import sys
import numpy as np
from PIL import Image, ImageOps, ImageFilter
src, out, block = sys.argv[1], sys.argv[2], int(sys.argv[3])
PAL = np.array([(15,56,15),(48,98,48),(139,172,15),(155,188,15)], np.uint8)
g = Image.open(src).convert('L')
a = np.asarray(g).astype(int)
bg = int(np.median(a[:20, :20]))
mask_img = Image.fromarray(((np.abs(a - bg) > 6) * 255).astype(np.uint8))
mask = np.asarray(mask_img.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))) > 0
edges = np.asarray(g.filter(ImageFilter.FIND_EDGES)) > 12
lo, hi = np.percentile(a[mask], [20, 90])                        # shadows / body / highlights
lv = np.where(a < lo, 1, np.where(a < hi, 2, 3))
lv[edges] = 0                                                   # outlines: darkest
lv[~mask] = 0                                                   # background: darkest
small = lv[::block, ::block]
rgb = PAL[small].repeat(block, 0).repeat(block, 1)
Image.fromarray(rgb).save(out)
print(bg, mask.mean().round(2), np.bincount(small.ravel(), minlength=4))
