#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont, ImageSequence
from images2gif import writeGif
import os, subprocess, sys, time

#FRAMES = 9
FRAME = [
#"/home/mevaka/Desktop/gifci/kaynak/1.jpg",
#"/home/mevaka/Desktop/gifci/kaynak/2.jpg",
#"/home/mevaka/Desktop/gifci/kaynak/3.jpg",
#"/home/mevaka/Desktop/gifci/kaynak/4.jpg",
#"/home/mevaka/Desktop/gifci/kaynak/5.jpg",
#"/home/mevaka/Desktop/gifci/kaynak/6.jpg",
"/home/mevaka/Desktop/gifci/kaynak/7.jpg",

]

FRAME_DELAY = 0.3
WIDTH, HEIGHT = 650, 300
PIE_POS = (WIDTH-50,10, WIDTH-10,50)
FONT = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf', 12)



frames = []
for count in FRAME :
  #txt = subprocess.Popen('top -c -n 1 -b'.split(), stdout=subprocess.PIPE).stdout.read()
  #frames.append(make_frame(txt, count))
  frames.append( Image.open(count) )
 # time.sleep(FRAME_DELAY)

print frames

writeGif("topmovie.gif", frames, duration=FRAME_DELAY, repeat=True, dither=False, nq=0, subRectangles=True, dispose=None)
#loops=10, dither=0)
