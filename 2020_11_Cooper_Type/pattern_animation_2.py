from random import random

step = 40
margin = 4

fps = 15
seconds = 1

duration = 1/fps
totalFrames = fps*seconds

w = 1920
h = 1080

xRange = range(0, w, step)
yRange = range(0, h, step)

# Make a color limiter
def colorLimit(limit):
    r = random()
    while(r > limit):
        r = random()
    return r

# Drawing
def module(x, y, w, h):
    fill(.5,colorLimit(0.5),1)
    oval(x, y, w/2, h/2)
    fill(1,colorLimit(0.5),1)
    oval(x+w/2, y+h/2,w/2, h/2)

# Layout
for p in range(totalFrames):
    newPage(w, h)
    frameDuration(duration)
    fill(0)
    rect(0,0,width(),height())
    for x in xRange:
        for y in yRange:
            if random() > 0.5:
                module(x, y, step+margin, step+margin)
saveImage("~/Desktop/pattern_animate.gif")
saveImage("~/Desktop/pattern_animage.mp4")
        