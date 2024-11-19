from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Crimson")
        self.penup()
        self.ht()
        self.goto(0, 240)
        self.level = 0
        self.write(f"Level : {self.level}", False, align="center", font=('Serif', 15, 'normal'))


    def incrementLevel(self):
        self.level += 1


    def refresh(self):
        self.clear()
        self.write(f"Level : {self.level}", False, align="center", font=('Serif', 15, 'normal'))


    def endRace(self):
        tom = Turtle()
        tom.ht()
        tom.penup()
        tom.color("Blue")
        tom.write(f"Race finished !!! your final level is {self.level}", False, align="center", font=('Serif', 20, 'normal'))
