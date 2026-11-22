from pathlib import Path
import sys, subprocess, json, re
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'.tools'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
sources=root/'media/originals/videos'; out=root/'dist/assets'; out.mkdir(parents=True,exist_ok=True)
plan=[('20260612_194844.mp4','media-event-1'),('20260809_203714.mp4','media-event-2'),('ровесник-clip14.mp4','media-club-1'),('МАНКИС.mp4','media-club-2'),('ровесник-clip17.mp4','media-club-3')]
manifest=[]
for original,name in plan:
 src=sources/original
 info=subprocess.run([ff,'-hide_banner','-i',str(src)],capture_output=True,text=True,encoding='utf-8',errors='replace').stderr
 print(original,info,flush=True)
 # Preserve original aspect ratio and audio. Only a short excerpt is distributed.
 hdr='smpte2084' in info
 vf="scale=w='min(1280,iw)':h='min(720,ih)':force_original_aspect_ratio=decrease:force_divisible_by=2"
 if hdr: vf+=',zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p'
 cmd=[ff,'-y','-hide_banner','-loglevel','error','-ss','0','-i',str(src),'-t','16','-map','0:v:0','-map','0:a:0?','-vf',vf,'-map_metadata','-1','-c:v','libx264','-preset','fast','-crf','28','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-movflags','+faststart',str(out/(name+'.mp4'))]
 subprocess.run(cmd,check=True)
 subprocess.run([ff,'-y','-hide_banner','-loglevel','error','-ss','1','-i',str(out/(name+'.mp4')),'-frames:v','1','-q:v','3',str(out/(name+'.jpg'))],check=True)
 manifest.append({'id':name,'original':original,'video':'assets/'+name+'.mp4','poster':'assets/'+name+'.jpg','bytes':(out/(name+'.mp4')).stat().st_size,'description':'Фрагмент исходного видео выступления; название события не подтверждено.'})
 (root/'media-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 print('DONE',name,manifest[-1]['bytes'],flush=True)
