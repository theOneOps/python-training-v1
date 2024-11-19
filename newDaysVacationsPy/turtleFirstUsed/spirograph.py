import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
t.speed(0)
turtle.colormode(255)


def randomColors():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    colors = (r, g, b)
    return colors


for i in range(10, 365, 5):
    t.circle(50)
    t.left(i)
    t.color(randomColors())

myscreen = Screen()
myscreen.exitonclick()
