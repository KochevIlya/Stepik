import turtle as t
import random as r

t.tracer(10, 10)
def draw_star(x, y):
  cls = ['red', 'springgreen', 'seagreen', 'orchid', 'blue', 'violet', 'gold', 'orange', 'pink', 'lime', 'turquoise']
  t.up()
  t.setposition(x, y)
  t.setheading(r.randrange(360))
  t.fillcolor(cls[r.randrange(11)])
  t.down()
  t.begin_fill()
  a = r.randrange(30, 50)
  for _ in range(5):
    t.forward(a)
    t.right(144)
  t.end_fill()
  


def left_mouse_click(x, y):
    draw_star(x, y)


t.hideturtle()

t.Screen().onclick(left_mouse_click)
t.Screen().listen()
t.done()