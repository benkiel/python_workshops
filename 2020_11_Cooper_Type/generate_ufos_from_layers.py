font = CurrentFont()

for l in font.layers:
    nf = RFont()
    nf.insertLayer(l, "foreground")