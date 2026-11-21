"""Overlay a 0.05 fraction grid on pages (half size) side by side, to read crop boxes for tools/crops.py.
Usage: python3 tools/grid.py OUT.png page1.png [page2.png ...]"""
import sys
from PIL import Image, ImageDraw
out=sys.argv[1]; outs=[]
for f in sys.argv[2:]:
    im=Image.open(f).convert('RGB'); im=im.resize((im.width//2,im.height//2)); d=ImageDraw.Draw(im)
    for k in range(1,20):
        y=int(im.height*k/20); d.line([(0,y),(im.width,y)],fill=(255,0,0)); d.text((2,y+1),f'{k/20:.2f}',fill=(255,0,0))
        x=int(im.width*k/20); d.line([(x,0),(x,im.height)],fill=(0,0,255)); d.text((x+1,2),f'{k/20:.2f}',fill=(0,0,255))
    outs.append(im)
W=sum(i.width for i in outs); o=Image.new('RGB',(W,max(i.height for i in outs)),'white'); x=0
for i in outs: o.paste(i,(x,0)); x+=i.width
o.save(out)
