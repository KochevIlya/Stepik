import turtle as t, random as r
t.Screen().setup(400, 400)
t.speed(0)
t.ht()

def star5(side):
  cls = ['red', 'springgreen', 'seagreen', 'orchid', 'blue', 'violet', 'gold', 'orange', 'pink', 'lime', 'turquoise']
  t.up()
  t.setposition(r.randint(-200, 200), r.randint(-200, 200))
  t.setheading(r.randrange(360))
  t.fillcolor(cls[r.randrange(11)])
  t.begin_fill()
  for _ in range(5):
    t.forward(side)
    t.right(144)
  t.end_fill()

for i in range(100):
  star5(r.randint(15, 28))
t.tracer(100, 0)