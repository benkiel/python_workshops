font = CurrentFont()

min = 0
max = 0

for glyph in font:
    if glyph.box != None:
        if glyph.box[1] < min:
            min = glyph.box[1]
        if glyph.box[3] > max:
            max = glyph.box[3]

font.info.openTypeHheaAscender = max
font.info.openTypeHheaDescender = min
font.info.openTypeHheaLineGap = 0
font.info.openTypeOS2WinAscent = max
font.info.openTypeOS2WinDescent = abs(min)

font.info.openTypeOS2TypoAscender = font.info.capHeight
font.info.openTypeOS2TypoDescender = font.info.descender
font.info.openTypeOS2TypoLineGap = max + abs(min) - font.info.unitsPerEm


    