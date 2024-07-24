import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.penup()

def circle(x, y):
  turtle.goto(x, y)
  turtle.pendown()
  turtle.pencolor('black')
  turtle.fillcolor('black')
  turtle.begin_fill()
  turtle.circle(20)
  turtle.end_fill()
  turtle.penup()

def triangle(x, y, angle, pencolor, fillcolor):
  turtle.goto(x, y)
  turtle.setheading(angle)
  turtle.pendown()
  turtle.pencolor(pencolor)
  turtle.fillcolor(fillcolor)
  turtle.pensize(3)
  turtle.begin_fill()
  for i in range(3):
    turtle.forward(200)
    turtle.left(120)
  turtle.end_fill()
  turtle.penup()
  
triangle(-100, -100, 0, 'black', 'white')
circle(0, -175)
circle(105, 0)
circle(-105, 0)
triangle(0, -155, 60, 'white', 'white')

turtle.done()