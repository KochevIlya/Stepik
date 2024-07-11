import turtle as t

def draw_fill_rectangle(height, width, color):
    x, y = t.pos()
    t.pu()
    t.setpos(x - width / 2, y - height / 2)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)
    t.end_fill()
    t.pu()
    t.setpos(x, y)
    t.pd()

def draw_fil_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


draw_fill_rectangle(250, 100, "black")
x, y = t.pos()
t.setpos(x, y + 50)
draw_fil_circle(30, "red")
t.setpos(x, y - 30)
draw_fil_circle(30, "yellow")
t.setpos(x, y - 110)
draw_fil_circle(30, "green")
t.done()
