from fontParts.ui import Message, AskString, SelectFont

if len(fonts) != 2:
    Message("Open two fonts, and only two fonts!")
else:
    factor = AskString("Interpolation factor")
    try:
        factor = float(factor)
        f1 = fonts[0]
        f2 = fonts[1]
        result = RFont()
        for glyph in f1:
            if glyph.name in f2.keys():
                name = glyph.name
                r = result.newGlyph(name)
                r.interpolate(factor,glyph,f2[name])
        result.info.familyName = f1.info.familyName
        result.info.styleName = str(factor)
        result.testInstall()
    except:
        Message("Hey! A number please!")
        
    
    # f1 = fonts[0]
    # f2 = fonts[1]
    # result = RFont()
    # for glyph in f1:
    #     if glyph.name in f2.keys():
    #         name = glyph.name
    #         r = result.newGlyph(name)
    #         r.interpolate((0.5,.75),glyph,f2[name])
    # result.info.familyName = f1.info.familyName
    # result.info.styleName = "0.5 0.75"
    # result.testInstall()