fonts = AllFonts()

min = 0
max = 0

for font in fonts:
    for glyph in font:
        if glyph.bounds != None:
            if glyph.bounds[1] < min:
                min = glyph.bounds[1]
            if glyph.bounds[3] > max:
                max = glyph.bounds[3]
print(max, min)       
for font in fonts:
    font.info.openTypeHheaAscender = max
    font.info.openTypeHheaDescender = int(min)
    font.info.openTypeHheaLineGap = 0
    font.info.openTypeOS2TypoAscender = 750
    font.info.openTypeOS2TypoDescender = -250d
    font.info.openTypeOS2TypoLineGap = (max+abs(int(min)))-1000
    font.info.openTypeOS2WinAscent = max
    font.info.openTypeOS2WinDescent= abs(min)