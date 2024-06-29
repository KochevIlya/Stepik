import turtle


def star(length):
    angle = 144
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)
    turtle.right(angle)


turtle.setheading(72)
star(300)
turtle.done()
