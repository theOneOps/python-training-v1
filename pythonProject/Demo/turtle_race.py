from turtle import Turtle, Screen
import random

myscreen = Screen()
myscreen.setup(width=500, height=400)
user_choice = myscreen.textinput(title="Make your bet", prompt="Enter your turtle's color: ")
color_list = ["purple", "green", "red", "blue", "orange", "yellow"]
tim = Turtle("turtle")
x = -230
y = 100
l = []
continue_game = True
first_arrives = []

for i in color_list:
    tim = Turtle("turtle")
    tim.color(i)
    tim.penup()
    tim.goto(x, y)
    l.append(tim)
    y -= 50


def execute():
    for j in l:
        rand_number = random.randint(1, 3)
        j.forward(rand_number)


def finish():
    a = 0
    for j in l:
        finish_task = j.xcor()
        finish_color = color_list[a]
        a += 1
        if finish_task > 220:
            first_arrives.append(finish_color)
            j.clear()


while continue_game:
    execute()
    finish()
    for j in l:
        finish_task = j.xcor()
        if finish_task > 220.:
            continue_game = False

myscreen.exitonclick()
first = first_arrives[0]
if first == user_choice:
    print(f"you win,Congratulations the winner is {first} turtle")
else:
    print(f"you lose you choose {user_choice}'s turtle, but the winner was {first}")
myscreen.exitonclick()

