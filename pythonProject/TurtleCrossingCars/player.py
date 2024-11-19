from turtle import Turtle

tuple_pos = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.left(90)
        self.penup()
        self.goto(tuple_pos)

    def move(self):
        self.fd(20)

    def return_position(self):
        self.goto(tuple_pos)


