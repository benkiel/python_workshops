font = CurrentFont()
w = 600

for glyph in font:
    if glyph.bounds != None:
        if glyph.width < w:
            s = (w - glyph.width)/2
            glyph.leftMargin += s
            glyph.rightMargin += s
        elif glyph.width > w:
            sf = w/glyph.width
            glyph.scaleBy((sf,1))
            glyph.width = w
    else:
        glyph.width = w
        