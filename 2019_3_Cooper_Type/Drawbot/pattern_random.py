from random import random
size(500,500)
w = 20
p = 0

def module(x,y,w,h):
    strokeWidth(0)
    r = random()
    while r > 0.6:
        r = random()
    fill(r,r,0,0.5)
    oval(x,y,w,h)
    stroke(1,1,1,0.5)
    strokeWidth(w/10)
    r = random()
    if r > 0.5:
        line((x,y),(x+w,y+h))
    elif r < 0.25:
        line((x+w/2,y),(x+w/2,y+h))
    else:
        line((x,y+h),(x+w, y))

for page in range(10):
    if page != 0:
        newPage()
    for x in range(0,width(),w+p):
        for y in range(0,height(),w+p):
            module(x,y,w,w)

saveImage("/Users/benkiel/Desktop/dots.gif")