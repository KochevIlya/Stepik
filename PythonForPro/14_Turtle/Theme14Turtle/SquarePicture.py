import turtle

def Square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)

side = 300
turtle.forward(300)
turtle.left(180)
for i in range(30):
    Square(side)
    side -= 10