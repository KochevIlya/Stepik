import turtle

def TwoLines(side):
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)

turtle.setheading(270)
side = 200
while side > 0:
    TwoLines(side)
    side -= 10
