from turtle import Turtle
import random
colors = ["orange", "yellow", 'red', 'green', 'blue', 'purple', 'lightblue', 'lightgreen', 'white', 'grey', 'midnightblue']

class Cars():
    def __init__(self):
        self.l = []
        self.length = 0
        self.speedDeb = 3
        self.speedFin = 6

    def createCars(self, n):
        for i in range(n):
            tim = Turtle()
            tim.penup()
            tim.color(random.choice(colors))
            tim.shapesize(0.5, 2)
            tim.shape("square")
            posX, posY = random.randint(230, 250), random.randint(-220, 220)
            tim.goto(posX, posY)
            self.l.append(tim)
            self.length += 1

    def addCars(self):
        i, j = random.randint(0, 10), random.randint(0, 8)

        if i == 5:
            self.createCars(j)
        else:
            return


    def moveOn(self):
        for i in self.l:
            move = random.randint(self.speedDeb, self.speedFin)
            i.bk(move)


    def levelUp(self):
        self.speedDeb += 1
        self.speedFin += 1