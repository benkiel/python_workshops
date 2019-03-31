from fontParts.ui import Message, AskString, SelectFont

factor = AskString("Interpolation factor")
try:
    factor = float(factor)
    f1 = SelectFont("Pick font one")
    f2 = SelectFont("Pick font two")
    result = RFont()
    for glyph in f1:
        if glyph.name in f2.keys():
            name = glyph.name
            r = result.newGlyph(name)
            r.interpolate(factor,glyph,f2[name])
    # Set new font's naming
    if f1.info.familyName != None:
        result.info.familyName = f1.info.familyName 
    elif f2.info.familyName != None:
        result.info.familyName = f2.info.familyName
    else:
        result.info.familyName = AskString("Family name please")
    result.info.styleName = str(factor)
    result.testInstall()
except:
    Message("Hey! A number please!")
        
    
