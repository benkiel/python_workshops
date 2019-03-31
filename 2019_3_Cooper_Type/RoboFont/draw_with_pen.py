font = CurrentFont()

glyph = font.newGlyph("a")
glyph.width = 500

pen = glyph.getPen()
pen.moveTo((100, 100))
pen.lineTo((800, 100))
pen.curveTo((1000, 300), (1000, 600), (800, 800))
pen.lineTo((100, 800))
pen.lineTo((100, 100))
pen.closePath()
glyph.update()