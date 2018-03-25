font = CurrentFont()

v = 10

for glyph in font:
    if not glyph.isEmpty():
        glyph.leftMargin = glyph.leftMargin + v
        glyph.rightMargin = glyph.rightMargin + v
