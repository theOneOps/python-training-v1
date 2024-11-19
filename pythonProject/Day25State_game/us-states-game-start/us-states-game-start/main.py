import turtle
import pandas

screen = turtle.Screen()
player = turtle.Turtle()
player.ht()
data = pandas.read_csv("50_states.csv")
list_states = data.state
state_content = list_states.to_list()
print(state_content)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
player.color("blue")
continue_game = True
new_stat = []
with open("states.txt") as file:
    stat = file.readlines()
    stat = list(set(stat))
    for i in stat:
        new_stat.append(i.strip("\n"))


score = len(new_stat)
print(score)

if score > 0:
    for i in new_stat:
        position_X = int(data[data.state == i].x)
        position_Y = int(data[data.state == i].y)
        t = (position_X, position_Y)
        player.penup()
        player.goto(t)
        player.write(i, False, "center", ("serif", 8, "normal"))
        player.goto(0, 0)

while continue_game:
    answer = screen.textinput(title=f"State_correct {score}/50", prompt="what's another state name ?").title()
    if answer not in new_stat:
        for i in state_content:
            if i == answer:
                position_X = int(data[data.state == answer].x)
                position_Y = int(data[data.state == answer].y)
                t = (position_X, position_Y)
                player.penup()
                player.goto(t)
                player.write(answer, False, "center", ("serif", 10, "normal"))
                player.goto(0, 0)
                if score == 0:
                    with open("states.txt", mode="w") as file:
                        content = file.write(answer+"\n")
                else:
                    with open("states.txt", mode='a') as file:
                        content = file.write(answer+"\n")
                score += 1
                new_stat.append(answer)

            if score == 50:
                continue_game = False
                player.color('green')
                player.goto(320, 270)
                player.write("you have found all US states names, Congratulations", False, "center", ("sans-serif", 25, "normal"))

screen.exitonclick()