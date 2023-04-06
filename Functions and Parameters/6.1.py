import turtle


def drawSquare():
    turtle.pendown()
    for x in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.penup()


drawSquare()
turtle.goto(50, 50)
drawSquare()
turtle.goto(-10, 45)
drawSquare()
turtle.goto(60, 100)
drawSquare()
turtle.goto(-30, -67)
drawSquare()
