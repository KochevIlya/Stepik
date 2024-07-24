from turtle import *
from math import *
from random import *
speed(0)
tracer(0)
hideturtle()
penup()
colormode(255)
def fig(n, s):
    a = (s * 4 * tan(pi / n) / n) ** 0.5
    r = a / (2 * sin(pi / n))
    fillcolor(randrange(255), randrange(255), randrange(255))
    begin_fill()
    pendown()
    circle(r, 360, n)
    penup()
    end_fill()
    return 1
    
x0 = -100
y0 = -100
h = 50
for i in range(5):
    y = i * h + y0 
    for j in range(5):
        x = j * h + x0
        setpos(x, y)
        fig(randrange(3, 8), 800)
update()
done()