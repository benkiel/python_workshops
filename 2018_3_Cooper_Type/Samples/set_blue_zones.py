fonts = AllFonts()

cap = ["C", "G", "J", "U", "O", "S"]
lc = ["a", "o", "n", "c", "e", "s", "u"]
second = ["g", "j", "y"]


for font in fonts:
    cap_max = 0
    cap_min = font["H"].box[3]
    lc_max = 0
    lc_min = font["x"].box[3]
    second_max = font["p"].box[1]
    second_min = 0
    min = 0
    for n in cap:
        if font[n].box[3] > cap_max:
            cap_max = font[n].box[3]
        if font[n].box[1] < min:
            min = font[n].box[1]
    for n in lc:
        if font[n].box[3] > lc_max:
            lc_max = font[n].box[3]
        if font[n].box[1] < min:
            min = font[n].box[1]
    for n in second:
        if font[n].box[1] < second_min:
            second_min = font[n].box[1]
    font.info.postscriptBlueValues = [min, 0, lc_min, lc_max, cap_min, cap_max]
    font.info.postscriptOtherBlues = [second_min, second_max]

    print font.info.postscriptFullName
    print font.info.postscriptBlueValues
    print font.info.postscriptOtherBlues
