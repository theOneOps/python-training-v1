import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def Rcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t = (r, g, b)
    return t

orientation = [0, 90, 180, 270]

def move():
    tim.color(Rcolor())
    tim.setheading(random.choice(orientation))
    tim.forward(10)
    tim.pensize(random.randint(5, 9))


for _ in range(150):
    move()

screen = Screen()
screen.exitonclick()
