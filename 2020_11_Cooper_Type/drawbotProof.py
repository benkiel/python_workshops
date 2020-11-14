size("A4Landscape")
f = CurrentFont()

stroke(0)
line((0, 10), (width(), 10))

text = FormattedString()
text.fontSize(20)
text.font(f.info.postscriptFontName)

names = list(f.keys())
names.sort()

for n in names:
    if n != ".notdef":
        glyph = f[n]
        if glyph.name[0].isupper():
            text.appendGlyph("H", "H", glyph.name, "O", "O", glyph.name, "O")
        else:
            text.appendGlyph("n", "n", glyph.name, "o", "o", glyph.name, "o")   
        text.append("\n")

counter = 0
column = 150
x = (20+(column*counter))

overflow = textBox(text, (x, 30, column, height()-60))

while len(overflow) > 0:
    counter += 1
    x = (20+(column*counter))
    print(x)
    if (x + column) > width():
        newPage("A4Landscape")
        x = 20
        counter = 0
    overflow = textBox(overflow, (x, 30, column, height()-60))
