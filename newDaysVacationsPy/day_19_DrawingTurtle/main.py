import turtle
from turtle import Turtle, Screen

tim = Turtle()


def turnRight():
    tim.right(10)


def turnLeft():
    tim.left(10)


def goOn():
    tim.forward(10)


def goBack():
    tim.bk(10)


turtle.onkey(turnRight, 'Right')
turtle.onkey(turnLeft, 'Left')
turtle.onkey(goOn, 'Up')
turtle.onkey(goBack, 'Down')
turtle.listen()

myscreen = Screen()
myscreen.exitonclick()
