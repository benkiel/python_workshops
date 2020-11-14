font = CurrentFont()

sc = []

sc_feature = """
feature c2sc {
    sub @sc_off by @sc_on;
} c2sc;
"""


for glyph in font:
    if '.sc' in glyph.name:
        sc.append(glyph.name)
sc.sort()

sc_off = []
for n in sc:
    sc_off.append(n[:-3])

sc_on = f"@sc_on  = [{' '.join(sc)}];\n"
sc_off = f"@sc_off = [{' '.join(sc_off)}];\n"

font.features.text = sc_on + sc_off + sc_feature
