scratch = 0
python = 0


def pointScratch():
    global scratch

    scratch += 1
    print("Hmm, sounds more like Scratch to me!")


def pointPython():
    global python

    python += 1
    print("That's what Python would say!")


def askQuestion(question, scratchAns):
    ans = input(question)

    if ans == scratchAns:
        pointScratch()
    else:
        pointPython()


print("Welcome to Which Programming Language are You!")
askQuestion("First question: How would you prefer to spend an afternoon? "
            "\nEnter a for playing with blocks. "
            "\nEnter b for writing using my computer. ", "a")

askQuestion("Second question: How would your friends describe you? "
            "\nEnter a for cerebral and determined. "
            "\nEnter b for fun and vibrant. ", "b")


askQuestion("Third question: What's your favourite brian exercise? "
            "\nEnter a for educational computer game. "
            "\nEnter b for logic puzzles. ", "a")

if scratch > python:
    print("Based on your answers, you are Scratch!")
else:
    print("Based on your answers, you are Python!")