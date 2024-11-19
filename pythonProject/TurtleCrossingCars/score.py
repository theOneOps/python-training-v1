from turtle import Turtle

tuple = (-220, 260)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.ht()
        self.move = False
        self.color("green")
        self.arg = f"Level :{self.level}"
        self.font = ("Serif", 20, 'normal')
        self.align = "center"
        self.penup()
        self.goto(tuple)
        self.write(self.arg, self.move, self.align, self.font)

    def increment_score(self):
        self.level += 1

    def refresh(self):
        self.clear()
        self.arg = f"Level :{self.level}"
        self.write(self.arg, self.move, self.align, self.font)
