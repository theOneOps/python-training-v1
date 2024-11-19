import time
from turtle import Screen, Turtle
from players import Player
from cars import Cars

myscreen = Screen()
myscreen.setup(width=600, height=600)
player_1 = Player()
continue_game = True

while continue_game:
    myscreen.update()
    time.sleep(0.1)

    myscreen.listen()
    myscreen.onkey(player_1.move, "Up")
    car = Cars()

    for i in car.lists:
        if player_1.distance(i) < 10:
            continue_game = False
            game = Turtle()
            game.color('red')
            game.write("Game Over", False, "center", font=("Arial", 20, "normal"))

    if player_1.ycor() >= 280:
        continue_game = False
        game = Turtle()
        game.color('green')
        game.write("Congratulations, You win", False, "center", font=("Arial", 20, "normal"))



    myscreen.exitonclick()

