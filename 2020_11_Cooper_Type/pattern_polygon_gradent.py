from random import random

size(1000, 1000)
step = 20
margin = 4
xRange = range(0, width(), step)
yRange = range(0, height(), step)

linearGradient(
    (100, 100),                         # startPoint
    (800, 800),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .2, 1]                          # locations
    )

def drawLine(startX,startY,endX,endY,sw):
    polygon((startX,startY), (startX+sw,startY), (endX+sw,endY), (endX,endY))

drawLine(0,0,1000,1000,10)
    





