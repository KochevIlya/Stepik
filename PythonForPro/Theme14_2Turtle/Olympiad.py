import turtle as t

def oneCircle(radius, color):
    t.pendown()
    t.pencolor(color)
    t.circle(radius)
    t.penup()

radius = 50
t.penup()
t.pensize(3)
oneCircle(radius, "blue")
t.goto(2 * radius, 0)
oneCircle(radius, "black")
t.goto(4 * radius, 0)
oneCircle(radius, "red")
t.goto(radius, -radius - radius / 5)
oneCircle(radius, "yellow")
t.goto(3 * radius, -radius - radius / 5)
oneCircle(radius, "green")