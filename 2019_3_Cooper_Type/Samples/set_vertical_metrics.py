fonts = AllFonts()

min = 0
max = 0
maxGlyph = ''
minGlyph = ''
for font in fonts:
    for glyph in font:
        if glyph.box is not None:
            if glyph.box[1] < min:
                min = glyph.box[1]
                minGlyph = glyph.name + ' ' + font.info.familyName + font.info.styleName
            if glyph.box[3]  > max:
                max = glyph.box[3]
                maxGlyph = glyph.name + ' ' + font.info.familyName + font.info.styleName

for font in fonts:
    font.info.openTypeHheaAscender = max
    font.info.openTypeHheaDescender = min
    font.info.openTypeHheaLineGap = 0
    font.info.openTypeOS2TypoAscender = font.info.ascender
    font.info.openTypeOS2TypoDescender = font.info.descender
    font.info.openTypeOS2TypoLineGap = (max + abs(min)) - font.info.unitsPerEm
    font.info.openTypeOS2WinAscent = max
    font.info.openTypeOS2WinDescent = abs(min)
    print (max + abs(min)) - font.info.unitsPerEm