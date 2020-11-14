fonts = AllFonts()
for font in fonts:
    min = 0
    max = 0

    for glyph in font:
        if glyph.bounds != None:
            if glyph.bounds[1] < min:
                min = glyph.bounds[1]
            if glyph.bounds[3] > max:
                max = glyph.bounds[3]
            
    print(min,max)

    capSpace = max - font['H'][3]

    if capSpace > min:
        min = -capSpace
    else:
        max = font['H'][3] + abs(min)

    font.info.openTypeOS2TypoAscender = max
    font.info.openTypeOS2TypoDescender = min
    font.info.openTypeOS2TypoLineGap = 0
    font.info.openTypeOS2WinAscent = max
    font.info.openTypeOS2WinDescent = abs(min)
    font.info.openTypeHheaAscender = max
    font.info.openTypeHheaDescender = min
    font.info.openTypeHheaLineGap = 0
