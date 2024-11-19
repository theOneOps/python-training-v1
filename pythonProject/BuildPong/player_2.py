from turtle import Turtle


class Player_2(Turtle):
    def __init__(self):
        super().__init__()
        tom = Turtle("square")
        tom.color("white")
        tom.shapesize(2, 0.5, 1)
        self.y_pos = 0
        self.x_pos = 250
        tuple_pos = (self.x_pos, self.y_pos)
        tom.penup()
        tom.goto(tuple_pos)

    def directionDh(self):
        new_pos = self.ycor()+20
        tuple_pos = (self.x_pos, new_pos)
        self.goto(tuple_pos)

    def directionDb(self):
        new_pos = self.ycor()-20
        tuple_pos = (self.x_pos, new_pos)
        self.goto(tuple_pos)
