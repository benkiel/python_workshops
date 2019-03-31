glyph = CurrentGlyph()

top = glyph.bounds[3]
for c in glyph:
    for p in c.points:
        if p.y > top-10 and p.y < top+10:
            p.y += 100
glyph.update()