font = CurrentFont()

for glyph in font:
    glyph.prepareUndo(undoTitle="Skew")
    glyph.skew(15)
    glyph.performUndo()




