import turtle
import math

def oneTriangle(degree, length):
    radius = length / (math.sqrt(3))
    turtle.setheading(90)
    turtle.right(degree)
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.right(150)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown() 


oneTriangle(0, 200)
oneTriangle(60, 200)
turtle.done()
