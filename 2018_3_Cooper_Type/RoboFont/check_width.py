font = CurrentFont()

for glyph in font:
    if glyph.width != 500:
        print glyph.name 