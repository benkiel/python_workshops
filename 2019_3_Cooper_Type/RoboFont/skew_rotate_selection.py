font = CurrentFont()

for glyph in font.selection:
    glyph = font[name]
    glyph.prepareUndo()
    glyph.rotate(-5)
    glyph.skew(5)
    glyph.performUndo()
