font = CurrentFont()

to_make = font.selection
xfactor = 0.84
yfactor = 0.84

for n in to_make:
    name = n + '.sc'
    og_glyph = font[n]
    glyph = font.newGlyph(name)
    glyph.appendGlyph(og_glyph)
    glyph.scale((xfactor,yfactor))
    if len(glyph.components) != 0:
        for c in glyph.components:
            if c.baseGlyph in to_make:
                c.baseGlyph = c.baseGlyph + ".sc"
            else:
                x, y = c.offset
                c.offset = (x*xfactor,y*yfactor)
    glyph.leftMargin = og_glyph.leftMargin
    glyph.rightMargin = og_glyph.rightMargin
    