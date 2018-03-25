font = CurrentFont()
min = 0
max = 0
minGlyph = ""
maxGlyph = ""
for glyph in font:
    if glyph.box != None:
        if glyph.box[1] < min:
            min = glyph.box[1]
            minGlyph = glyph.name
        if glyph.box[3] > max:
            max = glyph.box[3]
            maxGlyph = glyph.name
print min, minGlyph
print max, maxGlyph