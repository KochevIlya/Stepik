import turtle

def oneTurtle(length):
    turtle.penup()
    turtle.forward(length)
    turtle.stamp()
    turtle.back(length)
    turtle.pendown()


turtle.shape("turtle")
bg_color = (173 / 255, 216 / 255, 230 / 255)
turtle.bgcolor(bg_color)
for i in range(12):
    oneTurtle(120)
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.back(100)
    turtle.pendown()
    turtle.right(360 // 12)

