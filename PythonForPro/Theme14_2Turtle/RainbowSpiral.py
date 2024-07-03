import turtle

colors = ("red", "blue", "yellow", "green", "purple", "orange")

distance = 0
counter = 0
for i in range(45):
    turtle.pencolor(colors[counter % len(colors)])
    counter += 1
    turtle.pensize(counter / 2)
    turtle.forward(distance)
    turtle.left(45)
    distance += 3
turtle.done()
