import turtle

def line(length):
    turtle.forward(length)
    turtle.stamp()
    turtle.back(length)



def web(number):
    turtle.setheading(90)
    turtle.pensize(10)
    turtle.dot()
    turtle.pensize(2)
    for i in range(int(number)):
        line(100)
        turtle.right(360 / number)
    turtle.done()



n = int(input())
web(n)
