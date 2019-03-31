font = CurrentFont()

for name in font.selection:
    # get source glyph
    source = font[name]
    
    # get smallcap name
    gn = source.name + ".sc"
    
    # make sc glyph object
    glyph = font.newGlyph(gn)
    
    # add source to sc glyph
    glyph.appendGlyph(source)
    
    # scale
    glyph.prepareUndo()
    glyph.scaleBy((.8,.7))
    glyph.performUndo()
    glyph.rightMargin = source.rightMargin
