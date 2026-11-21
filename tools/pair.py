"""Paste images side by side. Usage: python3 tools/pair.py OUT.png a.png b.png [...]"""
import sys
from PIL import Image
out=sys.argv[1]; ims=[Image.open(f).convert('RGB') for f in sys.argv[2:]]
W=sum(i.width for i in ims); H=max(i.height for i in ims)
o=Image.new('RGB',(W,H),'white'); x=0
for i in ims: o.paste(i,(x,0)); x+=i.width
o.save(out)
