from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('blue')
        self.left(90)
        self.penup()
        self.x_pos = 0
        self.y_pos = -300
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        new_x_pos = self.xcor()
        new_y_pos = self.ycor()+20
        self.penup()
        self.goto(new_x_pos, new_y_pos)