font = CurrentFont()

for name in font.selection:
    # get source glyph
    source = font[name]
    
    # get smallcap name
    gn = source.name + ".num"
    
    # make sc glyph object
    glyph = font.newGlyph(gn)
    
    # add source to sc glyph
    glyph.appendGlyph(source)
    
    # scale
    glyph.prepareUndo()
    glyph.scaleBy((.8,.7))
    move = source.bounds[3] - glyph.bounds[3]
    glyph.moveBy((0,move))
    glyph.performUndo()
    glyph.rightMargin = source.rightMargin
