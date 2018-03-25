font = CurrentFont()

accented = {
    "Aacute": ["A", [("acute", "top")]],
    "aacute": ["a", [("acute", "top")]],
    "Agrave": ["A", [("grave", "top")]],
    "agrave": ["a", [("grave", "top")]],
}

for name, info in accented.items():
    if name in font.keys():
        font.removeGlyph(name)
    baseName = info[0]
    accentNames = info[1]
    font.compileGlyph(name, baseName, accentNames)