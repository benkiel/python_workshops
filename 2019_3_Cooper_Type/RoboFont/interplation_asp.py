font = CurrentFont()

one = font['a']
two = font['a.3']

result = font.newGlyph("blah")
result.interpolate((.1,.9),one,two)
    