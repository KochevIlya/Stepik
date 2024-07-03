import turtle

def oneTurtle(length):
    turtle.penup()
    turtle.forward(length)
    turtle.stamp()
    turtle.back(length)
    turtle.pendown()

def TurtleStar(n):
    turtle.shape("turtle")
    turtle.stamp()
    for i in range(n):
        oneTurtle(100)
        turtle.right(360 / n)
    turtle.done()
    
n = int(input())

TurtleStar(n)