import turtle

def rectangle(width, height):
    turtle.showturtle()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.done()
    

width = float(input())
height = float(input())
rectangle(width, height)
