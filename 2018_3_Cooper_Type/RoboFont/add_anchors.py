from robofab.interface.all.dialogs import AskString, Message
font = CurrentFont()

text = AskString("A height")
try:
    height = int(text)
except:
    Message("Hey! A number please!")

for name in font.selection:
    glyph = font[name]
    center = glyph.width/2
    glyph.appendAnchor('top', (center,height))
    
