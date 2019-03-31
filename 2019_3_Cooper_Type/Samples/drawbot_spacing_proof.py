size(1000,2000)

font = CurrentFont()
fn = font.testInstall()

glyphs = font.keys()
glyphs.sort()

t = FormattedString()
t.font(fn)
t.fontSize(24)
t.lineHeight(40)


for name in glyphs:
    if name[0].isupper():
        t.appendGlyph("H","O","H", name, "H", "O", name, "O", "H", "O")
        t += "\n"
    if name[0].islower():
        t.appendGlyph("n", "o", "n", name, "n", "o", name, "o", "n", "o")
        t += "\n"

overflow = textBox(t, (50,50,width()/2,height()-100))
overflow = textBox(overflow, (50+width()/2,50,width()/2,height()-100))

amount = len(overflow)        

while amount != 0:
    newPage()
    overflow = textBox(overflow, (50,50,width()/2,height()-100))
    overflow = textBox(overflow, (50+width()/2,50,width()/2,height()-100))
    amount = len(overflow)

print(len(overflow))