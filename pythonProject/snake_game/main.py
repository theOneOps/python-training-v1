from turtle import Screen
from snake_create import Snake
from food import Food
from scoreBoard import Score
import time

snake = Snake()
hood = Food()
myscore = Score()
myscreen = Screen()
myscreen.setup(width=600, height=600)
myscreen.bgcolor("black")
myscreen.title("My snake game")
myscreen.tracer(0)
continue_game = True

while continue_game:
    myscreen.update()
    time.sleep(0.09)
    snake.move()

    if snake.l[0].distance(hood) < 15:
        hood.change_location()
        snake.Refresh()
        myscore.incrementScore()

    if snake.l[0].xcor() < -260 or snake.l[0].xcor() > 260 or snake.l[0].ycor() < -260 or snake.l[0].ycor() > 260:
        myscore.refresh_high_Score()
        snake.reset()


    for i in snake.l[1:]:
        if snake.l[0].distance(i) < 10:
            myscore.refresh_high_Score()
            snake.reset()



    myscreen.listen()
    myscreen.onkey(snake.front, "Up")
    myscreen.onkey(snake.back, "Down")
    myscreen.onkey(snake.right, "Right")
    myscreen.onkey(snake.left, "Left")

myscreen.exitonclick()
