from robofab.interface.all.dialogs import AskString, Message
font = CurrentFont()

minGlyph = AskString("Min Glyph")
maxGlyph = AskString("Max Glyph")
steps = AskString("How many?")
try:
    steps = int(steps)
except:
    Message("Number please!")

for n in range(1, steps, 1):
    name = "test." + str(n)
    n = n/10
    glyph = font.newGlyph(name)
    glyph.interpolate(n, font[minGlyph], font[maxGlyph])
    glyph.mark = (1,0,0,1)