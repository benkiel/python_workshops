font = CurrentFont()

caps = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
lc = ('a', 'c', 'e', 'g', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z')
asc = ('b', 'd', 'f', 'h', 'l')
des = ('g', 'j', 'y', 'p', 'q')
base = ('C', 'G', 'J', 'O', 'S', 'U', 'a', 'b', 'c', 'd', 'e', 'o', 's', 'u')

def findAbove(glyphs):
    min = 0
    max = 0
    for name in glyphs:
        g = font[name]
        if g.bounds[1] < min:
            min = g.bounds[1]
        if g.bounds[3] > max:
            max = g.bounds[3]
    return min, max


cap_min, cap_max = findAbove(caps)
x_min, x_max = findAbove(lc)
asc_min, asc_max = findAbove(asc)

b = 0
for name in base:
    g = font[name]
    if g.bounds[1] < b:
        b = g.bounds[1]

des_min = 0
for name in des:
    g = font[name]
    if g.bounds[1] < des_min:
        des_min = g.bounds[1]

font.info.postscriptBlueValues = [b, 0, font['x'].bounds[3], x_max, font['H'].bounds[3], cap_max, font['b'].bounds[3], asc_max]
font.info.postscriptOtherBlues = [des_min, font['p'].bounds[1]]