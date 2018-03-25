font = CurrentFont()

caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
extras = ['space', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'hyphen', 'endash', 'emdash', 'quotedbl', 'period', 'comma', 'colon', 'ellipsis', 'exclam', 'periodcentered', 'bullet', '.notdef', 'dollar', 'semicolon', 'quotedblright', 'quoteright', 'quotedblleft', 'quoteleft', 'percent', 'multiply', 'plus', 'copyright', 'acute', 'ampersand', 'asterisk', 'question', 'trademark', 'eacute', 'parenright', 'quotesingle', 'parenleft', 'at', 'bar', 'slash', 'numbersign', 'ccaron', 'caron', 'j.sup', 'n.sup', 'f.sup', 'q.sup', 'u.sup', 'm.sup', 'x.sup', 'z.sup', 'i.sup', 's.sup', 'l.sup', 'r.sup', 'v.sup', 'a.sup', 'Q.sup', 'o.sup', 'k.sup', 'e.sup', 'w.sup', 'h.sup', 'g.sup', 'b.sup', 'y.sup', 'd.sup', 'c.sup', 't.sup', 'p.sup']


feature = "feature calt {\n"

for name in caps:
    new_caps = [n for n in caps if n != name]
    feature += "    @skip_%s = [%s];\n" % (name, " ".join(new_caps + lc + extras))

for name in lc:
    new_lc = [n for n in lc if n != name]
    feature += "    @skip_%s = [%s];\n" % (name, " ".join(new_lc + caps + extras))

feature += "\n"

for x in range(0,10):
    feature += "    lookup swap_%s{\n" % (x)
    
    counter = 0
    for name in caps:
        skip = "@skip_%s " % name
        feature += "        sub %s %s %s' by %s;\n" % (name, skip*x, name, lc[counter])
        counter += 1
    counter = 0
    for name in lc:
        skip = "@skip_%s " % name
        feature += "        sub %s %s %s' by %s;\n" % (name, skip*x, name, caps[counter])
        counter += 1
    feature += "    } swap_%s;\n"% x
    
feature += "} calt;"
font.features.text = feature