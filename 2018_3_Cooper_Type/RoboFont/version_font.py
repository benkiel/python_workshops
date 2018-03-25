fonts = AllFonts()
for font in fonts:
    n = font.info.familyName
    e = n[-1:]
    e = int(e) + 1
    font.info.familyName = n[:-1] + str(e)
