import random
import turtle
from turtle import Turtle, Screen

color_list = ["Red", 'Purple', 'Green', 'Blue', 'Yellow', 'Orange', 'Lightgreen']

tuplePos = [(-180, 0), (-180, 90), (-180, 60), (-180, -60), (-180, -90), (-180, -30), (-180, 30)]

theTurtle = []

theQuestion = turtle.textinput('the first turtle', 'What color is the first turtle to finish ?')
continueRace = True
for i in range(len(color_list)):
    tim = Turtle()
    tim.penup()
    tim.color(color_list[i])
    tim.goto(tuplePos[i])
    tim.shape('turtle')
    theTurtle.append(tim)

def drive(j):
    j.fd(random.randint(0, 10))


while continueRace:
    for i in theTurtle:
        if i.xcor() > 230:
            continueRace = False
            if i.pencolor().lower() == theQuestion.lower():
                print(f"congratulations, you've guessed well, the first turtle to finish is {i.pencolor()}")
            else:
                print(f"sorry, you're wrong, the first turtle to finish is {i.pencolor()}")
        else:

            drive(i)

myscreen = Screen()
myscreen.exitonclick()