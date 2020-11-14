font = CurrentFont()

for l in font.layers:
    p = font.path[:-4]
    p = p + "_" + l.name + ".otf"
    
    font.generate("otf", path=p, layerName=l.name)
