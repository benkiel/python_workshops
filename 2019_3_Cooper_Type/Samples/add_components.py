font = CurrentFont()

toMake = {'cacute':['c', 'acute'], 'racute':['r', 'acute']}
accents = {'acute': (0,80)}

for name, parts in toMake.items():
    glyph = font.newGlyph(name)
    for c in parts:
        if c not in accents:
            glyph.appendComponent(c)
        else:
            glyph.appendComponent(c, offset=accents[c])
    glyph.leftMargin = font[parts[0]].leftMargin
    glyph.rightMargin = font[parts[0]].rightMargin
