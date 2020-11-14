font = CurrentFont()

for glyph in font:
    if (len(glyph.components)) != 0:
        parts = []
        for c in glyph.components:
            parts.append(c.baseGlyph)
        print(f"{glyph.name} = {' + '.join(parts)}")
        