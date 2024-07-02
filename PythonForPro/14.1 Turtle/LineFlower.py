import turtle


def Line(length):
    turtle.forward(length)
    turtle.back(length)


turtle.setheading(90)
for i in range(10):
    Line(100)
    turtle.right(36)
