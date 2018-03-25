letter = 65
for p in range(26):
    fontSize(300)
    t = chr(letter+p)
    text(t,(width()/2,height()/2))
    newPage()

for p in range(10):
    rect(100*p,100,200,100)
    newPage()