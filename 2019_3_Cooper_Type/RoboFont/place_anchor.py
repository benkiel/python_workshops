font = CurrentFont()
glyphs = font.selection
for name in glyphs:
    glyph = font[name]
    offsetX = (glyph.bounds[2]-glyph.bounds[0])/2 + glyph.leftMargin
    offsetX = int(offsetX)
    glyph.appendAnchor("top", (offsetX,glyph.font.info.xHeight + 20))

