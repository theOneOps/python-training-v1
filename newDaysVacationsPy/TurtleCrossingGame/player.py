from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.color("Green")
        self.goto(0, -250)
        self.shape("turtle")


    def moveOn(self):
        self.fd(20)

    def refreshAgain(self):
        self.goto(0, -250)
