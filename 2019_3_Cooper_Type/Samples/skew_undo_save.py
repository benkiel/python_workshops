font = CurrentFont()


for glyph in font:
    glyph.prepareUndo(undoTitle="Skew")
    glyph.skew(10)

for glyph in font:
    glyph.rotate(10)
    glyph.performUndo()

print font.path
p = font.path[:-4] + "_skew.ufo"
font.save(p)



