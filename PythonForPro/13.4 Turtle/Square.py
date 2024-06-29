import turtle


def Square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)


def square(side, angle):
    turtle.setheading(angle)
    Square(side)


side = 100
square(side, 165)
square(side, 135)
square(side, 105)
turtle.done()
