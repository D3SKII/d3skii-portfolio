from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
import json,math
root=Path(r'D:\Codex\Вайбкод\personal-portfolio')
files=list((root/'media/originals/photos').glob('*'))
out=root/'media/contact-sheet.jpg'
canvas=Image.new('RGB',(1200,math.ceil(len(files)/4)*270),(25,25,25)); d=ImageDraw.Draw(canvas)
records=[]
for i,p in enumerate(files):
 try:
  im=ImageOps.exif_transpose(Image.open(p)).convert('RGB'); records.append({'file':p.name,'width':im.width,'height':im.height,'bytes':p.stat().st_size})
  im.thumbnail((288,235)); x=(i%4)*300+(300-im.width)//2; y=(i//4)*270
  canvas.paste(im,(x,y)); d.text(((i%4)*300+6,y+238),str(i)+' '+p.name[:36],fill='white')
 except Exception as e: print(p.name,str(e))
canvas.save(out,quality=88)
(root/'media/photo-inventory.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
print(out)
