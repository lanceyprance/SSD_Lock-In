"""Cut slide / answer snippets into img/NN/.

Usage: python3 tools/crops.py JOBFILE
Each job line:  src.png  dst.png  [x0 y0 x1 y1]   (box as fractions 0-1 of the page; omit for the whole page)
The result is trimmed of white margins and given a 12 px white border.
"""
import sys
from PIL import Image, ImageChops

def trim(im, pad=12):
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg).convert('L').point(lambda v: 255 if v > 18 else 0)
    box = diff.getbbox()
    if box:
        im = im.crop(box)
    out = Image.new('RGB', (im.width + 2 * pad, im.height + 2 * pad), 'white')
    out.paste(im, (pad, pad))
    return out

def run(jobfile):
    for line in open(jobfile):
        line = line.split('#')[0].split()
        if not line:
            continue
        src, dst, *box = line
        im = Image.open(src).convert('RGB')
        if box:
            x0, y0, x1, y1 = map(float, box)
            im = im.crop((int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height)))
        trim(im).save(dst, optimize=True)
        print(dst, Image.open(dst).size)

if __name__ == '__main__':
    run(sys.argv[1])
