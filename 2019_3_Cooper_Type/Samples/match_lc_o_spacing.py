font = CurrentFont()

left_glyphs = ["c", "d", "q", "e"]
right_glyphs = ["b", "p"]

for glyph in left_glyphs:
    font[glyph].leftMargin = font["o"].leftMargin
    
for glyph in right_glyphs:
    font[glyph].rightMargin = font["o"].rightMargin


