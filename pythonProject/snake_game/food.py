import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('blue')
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        location = (x, y)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.goto(location)

    def change_location(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        location = (x, y)
        self.goto(location)