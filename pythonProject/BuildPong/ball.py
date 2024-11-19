from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.new_pos_x = 0.5
        self.new_pos_y = 0.5
        self.speed("fastest")
        self.tuple = (0, 0)

    def bouncing_game(self):
        self.penup()
        self.goto(self.tuple)
        new_posx = self.xcor() + self.new_pos_x
        new_posy = self.ycor() + self.new_pos_y
        self.tuple = (new_posx, new_posy)
        self.goto(self.tuple)

    def bouncing_game_2(self):
        self.new_pos_y *= -1

    def bouncing_gameD(self):
        self.new_pos_x *= -1

    def refresh(self):
        self.tuple = (0, 0)
        self.bouncing_gameD()