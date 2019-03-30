font = CurrentFont()
ligs = []
for glyph in font:
    if "_" in glyph.name:
        ligs.append(glyph.name)
for lig in ligs:
    parts = lig.split('_')
    line = "sub "
    for p in parts:
        line = line + p + " "
    line = line + "by " + lig + ";"
    print line