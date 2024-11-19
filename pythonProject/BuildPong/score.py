from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.move = False
        self.color("white")
        self.align = "center"
        self.font = ("serif", 15, 'normal')
        self.penup()
        self.goto(0, 230)
        self.x_score = 0
        self.y_score = 0
        self.arg = f"X: {self.x_score} - Y: {self.y_score}"
        self.ht()
        self.write(self.arg, self.move, self.align, self.font)


    def incrementX(self):
        self.x_score += 1
        self.clear()
        self.arg = f"X: {self.x_score} - Y: {self.y_score}"
        self.write(self.arg, self.move, self.align, self.font)

    def incrementY(self):
        self.y_score += 1
        self.clear()
        self.arg = f"X: {self.x_score} - Y: {self.y_score}"
        self.write(self.arg, self.move, self.align, self.font)



