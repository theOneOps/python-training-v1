import time
import turtle
from turtle import Screen
from player import Player
from cars import Cars
from score import Score


theCars = Cars()
theScore = Score()
myscreen = Screen()
myscreen.setup(width=600, height=600)
myscreen.bgcolor("Black")
myscreen.title("The TurtleCrossingGame")
continueGame = True
turtle.tracer(0)
thePlayer = Player()

myscreen.onkey(thePlayer.moveOn, 'Up')
myscreen.listen()


while continueGame:
    time.sleep(0.1)
    turtle.update()

    theCars.moveOn()
    theCars.addCars()
    #print(theCars.length)

    for i in theCars.l:
        if thePlayer.distance(i) < 20:
            continueGame = False
            theScore.endRace()

    if thePlayer.ycor() > 240:
        theScore.incrementLevel()
        theScore.refresh()
        thePlayer.refreshAgain()
        theCars.levelUp()


myscreen.exitonclick()