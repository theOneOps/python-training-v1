import random
from turtle import Turtle

list_color = ['red', 'blue', 'yellow', 'green', 'black', 'purple', 'pink', 'gray']

continue_move = True
continue_create = True


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.lists = []
        self.x_pos_2 = 330
        self.distance = 100
        self.vitesse_x = 4
        self.vitesse_y = 20
        self.create_cars_2()
        self.move()

    def create_cars(self):
        ind = 9
        place = -280
        for i in range(ind):
            coolor = list_color[random.randint(0, 7)]
            tim = Turtle('square')
            tim.shapesize(1, 3, 1)
            tim.color(coolor)
            tim.penup()
            tim.goto(self.x_pos_2, place)
            self.lists.append(tim)
            place += 65

    def move(self):
        while self.lists[-1].xcor() > self.distance:
            for i in self.lists:
                walk_step = random.randint(self.vitesse_x, self.vitesse_y)
                new_x_pos = i.xcor() - walk_step
                new_y_pos = i.ycor()
                i.goto(new_x_pos, new_y_pos)

    def create_cars_2(self):
        for i in range(2):
            self.create_cars()
            self.move()
            self.x_pos_2 -= 25
            self.distance -= 10
            self.vitesse_x += 2
            self.vitesse_y += 2
