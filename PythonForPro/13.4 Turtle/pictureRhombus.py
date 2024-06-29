import turtle

def rhombus(angle1, angle2):
    turtle.forward(100)
    turtle.left(angle1)
    turtle.forward(100)
    turtle.left(angle2)
    turtle.forward(100)
    turtle.left(angle1)
    turtle.forward(100)
    turtle.left(angle2)
for i in range(10):
    rhombus(60, 120)
    turtle.right(36)
