import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def randomColors():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    colors = (r, g, b)
    return colors

tim.penup()
tim.bk(100)
tim.right(90)
tim.fd(50)
tim.left(90)
tim.pendown()

for i in range(0, 10):
    for j in range(0, 10):
        tim.dot(8, randomColors())
        tim.penup()
        tim.forward(20)

    tim.penup()
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(200)
    tim.right(180)
    tim.pendown()


myscreen = Screen()
myscreen.exitonclick()


