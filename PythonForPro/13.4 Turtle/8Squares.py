import turtle
def Square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)


def square(side, angle):
    turtle.setheading(angle)
    Square(side)


temp = 0
for i in range(8):
    square(100, temp)
    temp += 45
turtle.done()