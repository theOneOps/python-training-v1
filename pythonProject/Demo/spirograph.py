import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()


def coolor():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    color = (a, b, c)
    return color


for i in range(200):
    tim.speed(0)
    tim.color(coolor())
    tim.lt(i)
    tim.circle(100)

screen.exitonclick()