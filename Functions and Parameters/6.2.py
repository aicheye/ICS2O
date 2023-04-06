# Puzzle 1: Use refactoring to make the code shorter
# import turtle and hide the turtle arrow
import turtle
turtle.hideturtle()


# Function for a correct answer
def correct():
    # Tell them they were right and draw a smiley face
    print("Correct!")

    # reset turtle
    reset()

    # Draw smiley face
    turtle.circle(50)

    # Draw the eyes
    drawEyes()

    # Draw the smile
    turtle.penup()
    turtle.goto(-25, 35)
    turtle.pendown()
    turtle.setheading(270)
    turtle.circle(25, 180)


# Function for an incorrect answer
def incorrect():
    # Tell them they were wrong and draw a sad face
    print("Incorrect!")

    # reset turtle
    reset()

    # Draw smiley face
    turtle.circle(50)

    # Draw the eyes
    drawEyes()

    # Draw the frown
    turtle.penup()
    turtle.goto(25, 15)
    turtle.pendown()
    turtle.setheading(90)
    turtle.circle(25, 180)


# Function to reset the turtle
def reset():
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.setheading(0)


def drawEyes():
    turtle.penup()
    turtle.goto(-20, 60)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(20, 60)
    turtle.pendown()
    turtle.circle(5)


# Welcome user to the game and ask first question
answer = input("Welcome to the game! First question: what do you call a digit of binary ")

# If the answer is correct
if answer == "bit" or answer == "a bit":
    correct()
else:
    incorrect()

# Ask second question
answer = input("Second question: what do you call 8 digits of binary? ")

# If the answer is correct
if answer == "byte" or answer == "a byte":
    correct()

else:
    incorrect()

# Ask final question
answer = input("Last question:what do you call 4 binary digits? ")

# If the answer is correct
if answer == "nibble" or answer == "a nibble":
    correct()

else:
    incorrect()
