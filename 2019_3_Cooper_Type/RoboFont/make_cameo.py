font = CurrentFont()

def drawBox(pen,x,y,w,h):
    pen.moveTo((x,y))
    pen.lineTo((x+w,y))
    pen.lineTo((x+w,y+h))
    pen.lineTo((x,y+h))
    pen.closePath()

max = 0
min = 0
for glyph in font:
    if glyph.bounds != None:
        if glyph.bounds[1] < min:
            min = glyph.bounds[1]
        if glyph.bounds[3] > max:
            max = glyph.bounds[3]
max += 30
min -= 30

for glyph in font:
    xMin = -30
    xMax = glyph.bounds[2]+glyph.rightMargin + 30
    pen = glyph.getPen()
    drawBox(pen, xMin, min, xMax, max+abs(min))    