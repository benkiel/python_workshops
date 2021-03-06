from robofab.interface.all.dialogs import AskString, Message
font = CurrentFont()

change = AskString("How much?")
try:
    change = int(change)
except:
    Message("Number Please!")

xheight = font.info.xHeight

for name in font.selection:
    glyph = font[name]
    for c in glyph:
        for p in c.bPoints:
            y = p.anchor[1]
            if y > xheight + 20:
                p.move((0,change))
    glyph.update()
      