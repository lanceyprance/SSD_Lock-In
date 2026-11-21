"""Contact sheet of rendered slides with slide numbers.
Usage: python3 tools/contact_sheet.py DIR OUT.png FIRST LAST   (DIR holds s-NN.png from pdftoppm -png file.pdf DIR/s)"""
import sys,glob,re
from PIL import Image,ImageDraw
d,out,start,end=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
fs=sorted(glob.glob(d+'/s-*.png'),key=lambda f:int(re.findall(r'(\d+)\.png',f)[0]))
fs=[f for f in fs if start<=int(re.findall(r'(\d+)\.png',f)[0])<=end]
cols=4; tw=480
ims=[Image.open(f).convert('RGB') for f in fs]
th=int(ims[0].height*tw/ims[0].width)
rows=(len(ims)+cols-1)//cols
o=Image.new('RGB',(cols*tw,rows*(th+18)),'white'); dr=ImageDraw.Draw(o)
for k,(f,i) in enumerate(zip(fs,ims)):
  x,y=(k%cols)*tw,(k//cols)*(th+18)
  o.paste(i.resize((tw,th)),(x,y+18)); dr.text((x+4,y+2),re.findall(r'(\d+)\.png',f)[0],fill='red')
o.save(out)
