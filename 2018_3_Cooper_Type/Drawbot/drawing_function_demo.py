from random import random, randint

def rgb_to_decimal(n):
    if n < 0:
        return 0
    elif n > 256:
        return 1
    else:
        return n/256

def draw(x,y,width,height,p):
    stroke(1)
    strokeWidth(1+p)
    flip = randint(0,1)
    if flip == 0:
        line((x,y),(x+width,y+height))
        line((x,y+height/2),(x+width/2,y+height))
        line((x+width/2,y),(x+width,y+height/2))
    else:
        line((x+width,y),(x,y+height))
        line((x+width/2,y),(x,y+height/2))
        line((x+width,y+height/2),(x+width/2,y+height))        

module = 100
spacing = 0
margin = module + spacing
page_width = 2000
page_height = 1000
pages = 100

size(page_width,page_height)

for p in range(pages):
    fill(0)
    rect(0,0,page_width, page_height)
    
    for x in range(0, width(), margin):
        for y in range(0, height(), margin):
            draw(x,y,module,module,p)
            
    if p != pages - 1:
        newPage(page_width,page_height)
        
saveImage("~/Desktop/image.pdf")
saveImage("~/Desktop/image.gif")