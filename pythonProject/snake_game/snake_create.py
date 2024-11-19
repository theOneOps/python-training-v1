from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.l = []
        self.length = 3
        self.pos = 0
        self.CreateSnake()

    def CreateSnake(self):
        for i in range(0, self.length):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.setpos(self.pos, 0)
            self.l.append(tim)
            self.pos -= 20

    def Refresh(self):
        self.length += 1
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        position = (self.l[-1].xcor(), self.l[-1].ycor())
        tim.setpos(position)
        self.l.append(tim)

    def right(self):
        for i in self.l:
            i.setheading(0)

    def left(self):
        for i in self.l:
            i.setheading(180)

    def back(self):
        for i in self.l:
            i.setheading(270)

    def front(self):
        for i in self.l:
            i.setheading(90)

    def move(self):
        for i in range(len(self.l) - 1, 0, -1):
            xcor = self.l[i - 1].xcor()
            ycor = self.l[i - 1].ycor()
            self.l[i].goto(xcor, ycor)
        self.l[0].forward(10)

    def reset(self):
        for i in self.l:
            i.goto(1000, 1000)
        self.clear()
        self.l = []
        self.pos = 0
        self.length = 3
        self.CreateSnake()