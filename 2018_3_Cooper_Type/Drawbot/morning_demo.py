from random import random

def rgb_to_decimal(n):
    if n < 0:
        return 0
    elif n > 256:
        return 1
    else:
        return n/256

def draw(x,y,width,height):
    
    

module = 50
spacing = 10
margin = module + spacing
page_width = 2000
page_height = 1000


size(page_width,page_height)

for p in range(10):
    for x in range(0, width(), margin):
        for y in range(0, height(), margin):
            r = random()
            while r < 0.5:
                r = random()
            fill(r,random(),0.5, random())
            oval(x,y,module,module)
            
    if p != 9:
        newPage(page_width,page_height)
        
saveImage("~/Desktop/image.pdf")