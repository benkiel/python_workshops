font = CurrentFont()

# extension to look for:
find = ".pnum"
# extension to add to the swapped glyph
ext = ".tnum"

change = []

for glyph in font:
    if glyph.name.endswith(find):
        change.append(glyph.name)
        
for name in change:
    new = name[:-len(find)]
    
    oldUni = font[name].unicodes
    
    temp = new + ".temp"
    if new in font.keys():
        newUni = font[new].unicodes
        font[new].name = temp
    
    if newUni:
        font[name].unicodes = newUni
    font[name].name = new
    
    if temp in font.keys():
        n = new + ext
        font[temp].unicodes = oldUni
        font[temp].name = n
           