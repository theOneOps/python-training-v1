import random
from turtle import Turtle

list_color = ["blue", "red", "purple", "green", "black", "yellow", "orange", "gray"]
speed_increase = 2

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.create_car()

    def create_car(self):
        random_number = random.randint(0, 6)

        if random_number == 1:
            color = list_color[random.randint(0, len(list_color)-1)]
            place = random.randint(-280, 280)
            self.shape('square')
            self.color(color)
            self.shapesize(0.7, 2.2, 1)
            self.penup()
            self.goto(300, place)

    def move(self):
        self.bk(self.speed)

    def increase_car_speed(self):
        self.speed += speed_increase




