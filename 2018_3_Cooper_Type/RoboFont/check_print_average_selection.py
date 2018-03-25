# Prints average width of selected glyphs
font = CurrentFont()
s = 0
c = 0
include = font.selection
for glyph in font:
    if not glyph.isEmpty() and glyph.name in include:
        s = s + glyph.width
        c = c + 1
print s/c