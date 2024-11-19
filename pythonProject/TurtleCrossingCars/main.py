import time
from turtle import Screen, Turtle
from player import Player
from cars import Car
from score import Score

list_cars = []
myscreen = Screen()
myscreen.setup(width=600, height=600)
myscreen.tracer(0)
myscreen.title("The turtle crossing game")

the_player = Player()

myscore = Score()

continue_game = True

while continue_game:
    myscreen.update()
    time.sleep(0.1)
    myscreen.listen()
    myscreen.onkey(the_player.move, "Up")

    car = Car()
    list_cars.append(car)

    for i in list_cars:
        i.move()

    for i in list_cars:
        if i.distance(the_player) < 15:
            continue_game = False
            game = Turtle()
            game.color("red")
            game.write(arg="Game over", align="center", font=('Serif', 20, 'normal'))

    if the_player.ycor() > 280:
        myscore.increment_score()
        myscore.refresh()
        the_player.return_position()
        for i in list_cars:
            i.increase_car_speed()


myscreen.exitonclick()