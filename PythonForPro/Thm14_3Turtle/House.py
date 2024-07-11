import turtle
import math 

def draw_fill_rectangle(height, width, color):
    x, y = turtle.pos()
    turtle.pu()
    turtle.setpos(x - width / 2, y - height / 2)
    turtle.pd()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(width)
        turtle.lt(90)
        turtle.fd(height)
        turtle.lt(90)
    turtle.end_fill()
    turtle.pu()
    turtle.setpos(x, y)
    turtle.dot()
    turtle.pd()

def draw_fill_triangle(height, color):
    x, y = turtle.pos()
    turtle.pu()
    turtle.setpos(x, y + 3 * height / 2)
    turtle.pd()
    temp = height / math.sin(50 * math.pi / 180)
    a = temp
    temp = a / math.sin(50 * math.pi / 180)
    b = temp * math.sin(80 * math.pi / 180)
    turtle.setheading(-130)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.lt(130)
    turtle.fd(b)
    turtle.lt(130)
    turtle.fd(a)
    turtle.end_fill()



draw_fill_rectangle(100, 100, "blue")
draw_fill_triangle(100, "brown")
turtle.done()


