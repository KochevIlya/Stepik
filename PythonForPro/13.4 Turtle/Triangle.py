import turtle

def triangle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.done()
side = float(input())
triangle(side)
