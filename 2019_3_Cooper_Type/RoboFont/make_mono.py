font = CurrentFont()

w = 100

for glyph in font:
    glyph.prepareUndo()
    if glyph.width != w and glyph.bounds == None:
        glyph.width = w
    elif glyph.width < w:
        v = w - glyph.width
        glyph.leftMargin += v/2
        glyph.rightMargin += v/2
    elif glyph.width > w:
        f = w/glyph.width
        glyph.scaleBy((f,1))
        v = w-glyph.bounds[2]
        glyph.rightMargin = v     
    glyph.performUndo()
    
for glyph in font:
    if glyph.width != w:
        glyph.width = w