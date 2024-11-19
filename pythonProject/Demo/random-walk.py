import turtle as myTurtle
import random

continue_game=True
tortue=myTurtle.Turtle()
screen=myTurtle.Screen()
myTurtle.colormode(255)

direction=[0,90,180,270]

def coolor():
    a=random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    color=(a, b, c)
    return color

while continue_game:
    width=10
    tortue.pencolor(coolor())
    direct=random.choice(direction)
    tortue.setheading(direct)
    tortue.pensize(width)
    tortue.forward(40)
    width+=0.1
