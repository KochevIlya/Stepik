import turtle

def rectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.dot()
    turtle.forward(height)
    turtle.left(90)
    turtle.dot()
    turtle.forward(width)
    turtle.left(90)
    turtle.dot()
    turtle.forward(height)
    turtle.dot()
    turtle.done()

rectangle(200, 100)