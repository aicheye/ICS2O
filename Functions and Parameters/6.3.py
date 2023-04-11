# Import turtle
import turtle
import math


# Function to reset the turtle
def reset(x=0.0, y=0.0):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)


# Draws the hill using a large circle
def drawHill():
    hillPos = (400, -500)
    hillRadius = 400

    reset(hillPos[0], hillPos[1])
    turtle.color("green")
    turtle.seth(90)
    turtle.begin_fill()
    turtle.circle(hillRadius, 180)
    turtle.end_fill()


# Draws the sun
def drawSun():
    # Draws the disc of the sun
    sunPos = (-150, 110)
    radius = 40

    reset(sunPos[0], sunPos[1])
    turtle.seth(0)
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    # Draws sun rays
    rays = 13
    rayOffset = 10
    rayLength = 15

    angle = 0
    while angle < 360:
        reset(sunPos[0], sunPos[1] + radius)
        turtle.seth(angle)
        turtle.penup()
        turtle.forward(radius + rayOffset)
        turtle.pendown()
        turtle.forward(rayLength)
        angle += 360 / rays

    # Draws a smile
    turtle.color("black")
    reset(sunPos[0] - radius * 0.2, sunPos[1] + radius)
    turtle.seth(-90)
    turtle.forward(radius * 0.2)

    reset(sunPos[0] + radius * 0.2, sunPos[1] + radius)
    turtle.seth(-90)
    turtle.forward(radius * 0.2)

    reset(sunPos[0] - radius * 0.4, sunPos[1] + radius * 0.7)
    turtle.seth(-90)
    turtle.circle(radius * 0.4, 180)


# Draws a house in the center of the screen
def drawHouse():
    # Draws the square part of the house
    topLeft = (-60, 0)
    houseSize = 120

    topRight = (topLeft[0] + houseSize, topLeft[1])
    botRight = (topRight[0], topRight[1] - houseSize)
    botLeft = (botRight[0] - houseSize, botRight[1])

    reset(topLeft[0], topLeft[1])
    turtle.color("maroon")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(houseSize)
        turtle.right(90)
    turtle.end_fill()

    # Draws the roof of the house
    roofLength = 160
    roofAngle = 40

    roofPos = (topLeft[0] - (roofLength - houseSize) / 2, topLeft[1])
    slopeLength = (roofLength * math.sin(math.radians(roofAngle))) / math.sin(math.radians(180 - roofAngle * 2))

    reset(roofPos[0], roofPos[1])
    turtle.begin_fill()
    turtle.color("gray")
    turtle.seth(roofAngle)
    turtle.forward(slopeLength)
    turtle.seth(-roofAngle)
    turtle.forward(slopeLength)
    turtle.seth(180)
    turtle.forward(roofLength)
    turtle.end_fill()

    # Draws the door
    doorOffset = 20
    doorHeight = 70
    doorWidth = 40

    doorPos = (botLeft[0] + doorOffset, botLeft[1])

    reset(doorPos[0], doorPos[1])
    turtle.seth(90)
    turtle.pencolor("gray")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(doorHeight)
        turtle.right(90)
        turtle.forward(doorWidth)
        turtle.right(90)
    turtle.end_fill()
    turtle.color("gray")
    reset(doorPos[0] + doorWidth / 2, doorPos[1])
    turtle.seth(90)
    turtle.forward(doorHeight)
    reset(doorPos[0], doorPos[1] + doorHeight / 2)
    turtle.seth(0)
    turtle.forward(doorWidth)

    # Draws the window
    windowWidth = 30

    windowPos = (botRight[0] - doorOffset, botRight[1] + doorHeight)

    reset(windowPos[0], windowPos[1])
    turtle.pencolor("brown")
    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    turtle.seth(180)
    for i in range(4):
        turtle.forward(windowWidth)
        turtle.left(90)
    turtle.end_fill()
    turtle.color("brown")
    reset(windowPos[0] - windowWidth / 2, windowPos[1])
    turtle.seth(-90)
    turtle.forward(windowWidth)
    reset(windowPos[0] - windowWidth, windowPos[1] - windowWidth / 2)
    turtle.seth(0)
    turtle.forward(windowWidth)


# Draws a cloud
def drawCloud(x, y):
    # First, three staggering circles are drawn one after another
    radius = 30

    reset(x, y)
    turtle.color("lightgray")
    turtle.seth(90)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    newX = x + radius * 1 / 2
    newY = y - radius
    reset(newX, newY)
    turtle.begin_fill()
    turtle.circle(radius * 1.2)
    turtle.end_fill()

    newX = newX + radius * 1 / 2 + radius
    reset(newX, newY)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    # Then, rain is drawn under
    rainStep = 20

    turtle.color("blue")
    reset(x - radius, y - radius - rainStep)
    turtle.seth(-90)
    turtle.forward(rainStep)

    reset(x + radius * 1 / 2, y - radius - rainStep * 0.5)
    turtle.seth(-90)
    turtle.forward(rainStep)
    turtle.penup()
    turtle.forward(rainStep)
    turtle.pendown()
    turtle.forward(rainStep)

    reset(x + radius * 2, y - radius - rainStep)
    turtle.seth(-90)
    turtle.forward(rainStep)
    turtle.penup()
    turtle.forward(rainStep)
    turtle.pendown()
    turtle.forward(rainStep)


# resets the field
turtle.clear()
turtle.bgcolor("skyblue")
turtle.reset()

print("Welcome to the Python Landscape Creator!")
turtle.hideturtle()
drawHill()
drawSun()
drawCloud(85, 130)
drawHouse()
turtle.done()
