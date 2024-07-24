import turtle


def SixAngle():
    for i in range(6):
        turtle.forward(50)
        turtle.left(60)
    turtle.right(120)


for i in range(6):
    SixAngle()
    turtle.forward(50)
    turtle.left(60)
turtle.done()
