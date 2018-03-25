try:
    from robofab.interface.all.dialogs import AskString, Message
except:
    from fontParts.ui import AskString, Message
    
font = CurrentFont()

width_text = AskString("What width?")
try:
    width = int(width_text)
except:
    Message("A number, come on!")

for glyph in font:
    if glyph.isEmpty():
        glyph.width = width
    elif glyph.width < width:
        dif = width - glyph.width
        glyph.leftMargin += dif/2
        glyph.rightMargin += dif/2
    elif glyph.width > width:
        f = width/glyph.width
        glyph.scale((f,1))
        gw = glyph.box[2]-glyph.box[0]
        dif = width - gw
        glyph.leftMargin = dif/2
        glyph.rightMargin = dif/2
    else:
        pass    




