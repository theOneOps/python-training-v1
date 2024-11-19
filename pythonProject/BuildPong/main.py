
from turtle import Turtle, Screen
from player import Player
from score import Score
from ball import Ball

y_pos_1 = 0
y_pos_2 = 0
x_pos_1 = -250
x_pos_2 = 250

joueur_1 = Player()
tuple_1_pos = (x_pos_1, y_pos_1)
joueur_1.penup()
joueur_1.goto(tuple_1_pos)

joueur_2 = Player()
tuple_2_pos = (x_pos_2, y_pos_2)
joueur_2.penup()
joueur_2.goto(tuple_2_pos)

scores = Score()

ballon = Ball()

def directionDb():
    y_pos_2 = joueur_2.ycor()-30
    tuple_2_pos=(x_pos_2, y_pos_2)
    joueur_2.goto(tuple_2_pos)

def directionDh():
    y_pos_2 = joueur_2.ycor() + 30
    tuple_2_pos = (x_pos_2, y_pos_2)
    joueur_2.goto(tuple_2_pos)

def directionGb():
    y_pos_1 = joueur_1.ycor() - 30
    tuple_1_pos = (x_pos_1, y_pos_1)
    joueur_1.goto(tuple_1_pos)

def directionGh():
    y_pos_1 = joueur_1.ycor() + 30
    tuple_1_pos = (x_pos_1, y_pos_1)
    joueur_1.goto(tuple_1_pos)


x_pos = 0.
y_pos = 200.
myscreen = Screen()
myscreen.bgcolor("black")
myscreen.setup(width=600, height=550)
myscreen.title("welcome to the GREAT Build Pong")
myscreen.tracer(0)
continue_game = True

for i in range(20):
    tim = Turtle("square")
    tim.color("white")
    tim.shapesize(0.3, 0.1, 1)
    tim.penup()
    tim.setpos((x_pos, y_pos))
    y_pos -= 20.

myscreen.listen()
myscreen.onkey(directionDb, 'Down')
myscreen.onkey(directionDh, 'Up')
myscreen.onkey(directionGh, 'q')
myscreen.onkey(directionGb, 'w')

while continue_game:
    myscreen.update()
    ballon.bouncing_game()

    if ballon.ycor() > 220 or ballon.ycor() < -220:
        ballon.bouncing_game_2()

    if ballon.distance(joueur_1) < 15 or ballon.distance(joueur_2) < 15:
        ballon.bouncing_gameD()

    if ballon.xcor() > 280:
        ballon.refresh()
        scores.incrementX()


    if ballon.xcor() < -280:
        ballon.refresh()
        scores.incrementY()

    if scores.x_score == 5:
        final_result = Turtle()
        final_result.ht()
        final_result.color("blue")
        final_result.write("Le joueur X a gagné", move=False, align="center",font=("serif", 30, 'normal'))
        continue_game = False

    if scores.y_score == 5:
        final_result = Turtle()
        final_result.ht()
        final_result.color("blue")
        final_result.write("Le joueur Y a gagné", move=False, align="center",font=("serif", 30, 'normal'))
        continue_game = False

myscreen.exitonclick()
