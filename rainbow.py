import turtle
from turtle import *

title("Rainbow Spiral")
speed(0)
bgcolor("black")

r, g, b = 255, 0, 0
colormode(255)

for i in range(255 * 2):
    if i < 255 // 3:
        g = min(g + 3, 255)
    elif i < 255 * 2 // 3:
        r = max(r - 3, 0)
    elif i < 255:
        b = min(b + 3, 255)
    elif i < 255 * 4 // 3:
        g = max(g - 3, 0)
    elif i < 255 * 5 // 3:
        r = min(r + 3, 255)
    else:
        b = max(b - 3, 0)

    pencolor(r, g, b)
    fd(50 + i)
    rt(91)

done()
    