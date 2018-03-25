font = CurrentFont()

one = font['A']
two = font['A.2']
steps = 4


if one.isCompatible(two):
    for x in range(steps):
        n = "A.interp" + str(x+1)
        g = font.newGlyph(n)
        f = (x+1)/(steps+1)
        print f
        g.interpolate(f, one, two)