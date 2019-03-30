size(1000,2000)

font = CurrentFont()
fn = font.testInstall()
uc = "HOH%sHO%sOHO"
lc = "non%sno%sono"

glyphs = font.keys()
glyphs.sort()

t = FormattedString()
t.font(fn)
t.fontSize(24)
t.lineHeight(40)

for name in glyphs:
    if name.isupper():
        t.appendGlyph("H", "O", "H", name, "H", "O", name, "O", "H", "O")
        t += "\n"
    if name.islower():
        t.appendGlyph("n", "o", "n", name, "n", "o", name, "o", "n", "o")
        t += "\n"

overflow = textBox(t, (50,50,width()-100,height()-100))
amount = len(overflow)        

while amount != 0:
    newPage()
    overflow = textBox(overflow, (50,50,width()-100,height()-100))
    amount = len(overflow)

print len(overflow)