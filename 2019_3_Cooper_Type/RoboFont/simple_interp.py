font = CurrentFont()

ss = """
feature ss%s{
    sub %s by %s;    
} ss%s;
"""

one = font['a']
two = font['a.2']

print(one.isCompatible(two))

features = ""
for f in range(10):
    f = f+1
    name = "test."+str(f)
    result = font.newGlyph(name)
    r = .1*f
    print(r)
    result.interpolate(f/5,one,two)
    
    if f < 10:
        f = "0"+str(f)
    features += ss % (f, 'a', name, f)

font.features.text = features