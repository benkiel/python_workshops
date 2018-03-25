font = CurrentFont()

for name in font.selection:
    glyph = font[name]
    
    newName = name + '.sup'
    font.insertGlyph(glyph, name=newName)
    
    supGlyph = font[newName]
    
    supGlyph.scale((.5,.5))
    supGlyph.move((0,font.info.capHeight/2))
    supGlyph.leftMargin = glyph.leftMargin
    supGlyph.rightMargin = glyph.rightMargin
    
    
