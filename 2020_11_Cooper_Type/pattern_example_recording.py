from random import random

size(1000, 1000)
step = 20
margin = 4
xRange = range(0, width(), step)
yRange = range(0, height(), step)
xRange2 = range(0, width(), step*4)
yRange2 = range(0, height(), step*4)

# Drawing
def module(x, y, w, h):
    fill(0)
    rect(x, y, w, h)

def module2(x, y, w, h):
    fill(1,0,1)
    rect(x, y, w, h)

notDrawn = []

for x in xRange:
    for y in yRange:
        if random() > 0.5:
            module(x, y, step, step)
        else:
            notDrawn.append([x,y])
print(notDrawn)
for x, y in notDrawn:
    module2(x,y,step,step)







        