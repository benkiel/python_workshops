from random import random

def rgb_to_decimal(n):
    if n < 0:
        return 0
    elif n > 256:
        return 1
    else:
        return n/256


module = 50
spacing = 0
margin = module + spacing


for p in range(10):
    for x in range(0, width(), margin):
        for y in range(0, height(), margin):
            r = random()
            while r < 0.5:
                r = random()

            fill(r,1,0.5)
            oval(x,y,module,module)
    if p != 9:
        newPage()
saveImage("~/Desktop/image.pdf")