font = CurrentFont()

min = 0
max = 0

for glyph in font:
    if glyph.bounds != None:
        if glyph.bounds[1] < min:
            min = glyph.bounds[1]
        if glyph.bounds[3] > max:
            max = glyph.bounds[3]
            
print(min,max)

font.info.openTypeOS2TypoAscender = font.info.ascender
font.info.openTypeOS2TypoDescender = font.info.descender
font.info.openTypeOS2TypoLineGap = (max + abs(min)) - font.info.unitsPerEm
font.info.openTypeOS2WinAscent = max
font.info.openTypeOS2WinDescent = abs(min)
font.info.openTypeHheaAscender = max
font.info.openTypeHheaDescender = min
font.info.openTypeHheaLineGap = 0

print((max + abs(min)) - font.info.unitsPerEm)