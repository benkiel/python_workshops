font = CurrentFont()

myGlyphs = {"Racute": ("R", [("acute", "top")])}

for name, parts in myGlyphs.items():
    font.compileGlyph(name, parts[0], parts[1])