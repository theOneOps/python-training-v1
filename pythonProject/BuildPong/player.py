from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(3.5, 0.5, 1)
