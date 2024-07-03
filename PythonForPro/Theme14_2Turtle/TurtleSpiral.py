import turtle


distance = 0
turtle.shape("turtle")
turtle.bgcolor("#90EE90")
turtle.penup()
for i in range(50):
    turtle.forward(distance)
    turtle.stamp()
    turtle.right(15)
    distance += 1
turtle.done()
