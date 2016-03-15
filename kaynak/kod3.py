#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont, ImageSequence
from images2gif import writeGif
import os, subprocess, sys, time

FRAMES = 12
FRAME_DELAY = 0.75
WIDTH, HEIGHT = 650, 300
PIE_POS = (WIDTH-50,10, WIDTH-10,50)
FONT = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf', 12)

def make_frame(txt, count, font=FONT):
  image = Image.new("RGBA", (WIDTH, HEIGHT), (255,255,255))
  draw = ImageDraw.Draw(image)
  fontsize = font.getsize('')[1]
  for row, line in enumerate(txt.split('\n')):
    draw.text((5, fontsize * row), line, (0,0,0), font=font)
  draw.pieslice(PIE_POS, 0, 360, (255,255,204))
  draw.pieslice(PIE_POS, 0, int(360.0/FRAMES*(1+count)), (0,128,0))
  return image


frames = []
for count in range(FRAMES):
  txt = subprocess.Popen('top -c -n 1 -b'.split(), stdout=subprocess.PIPE).stdout.read()
  frames.append(make_frame(txt, count))
  time.sleep(FRAME_DELAY)

writeGif("topmovie.gif", frames, duration=FRAME_DELAY, repeat=True, dither=False, nq=0, subRectangles=True, dispose=None) 
#loops=10, dither=0)
