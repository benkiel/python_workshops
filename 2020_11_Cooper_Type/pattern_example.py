from random import random

size(1920, 1080)
step = 40
margin = 4
xRange = range(0, width(), step)
yRange = range(0, height(), step)

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
fill(0)
rect(0,0,width(),height())
for x in xRange:
    for y in yRange:
        if random() > 0.5:
            module(x, y, step+margin, step+margin)
saveImage("~/Desktop/pattern.png")
        