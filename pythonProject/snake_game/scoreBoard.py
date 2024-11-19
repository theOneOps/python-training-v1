from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score.txt') as file:
            self.high_score = int(file.read())
        self.shape("classic")
        self.color('white')
        self.move = False
        self.arg = f"Score: {self.score} High score : {self.high_score}"
        self.penup()
        self.setpos(0, 250)
        self.align = "center"
        self.font = ("Arial", 15, 'normal')
        self.ht()
        self.write(self.arg, self.move, self.align, self.font)

    def incrementScore(self):
        self.score += 1
        self.clear()
        self.arg = f"Score: {self.score} High score : {self.high_score}"
        self.write(self.arg, self.move, self.align, self.font)

    def refresh_high_Score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', mode='w') as file:
                file.write(str(self.high_score))
            self.score = 0
            self.clear()
            self.arg = f"Score: {self.score} High score : {self.high_score}"
            self.write(self.arg, self.move, self.align, self.font)

        elif self.score <= self.high_score:
            with open('score.txt', mode='w') as file:
                file.write(str(self.high_score))
            self.score = 0
            self.clear()
            self.arg = f"Score: {self.score} High score : {self.high_score}"
            self.write(self.arg, self.move, self.align, self.font)

    def game_over(self):
        tim = Turtle()
        tim.color('white')
        tim.write("game over", self.move, "center", font=("Arial", 15, 'normal'))