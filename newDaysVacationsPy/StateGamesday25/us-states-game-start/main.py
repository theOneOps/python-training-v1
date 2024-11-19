import pandas
from turtle import Turtle, Screen

width = 725
height = 491

myScreen = Screen()
myScreen.setup(width=width, height=height)
myScreen.bgcolor("black")
myScreen.bgpic("blank_states_img.gif")
continueGame = True
data = pandas.read_csv("50_states.csv")
theStates = data["state"].tolist()
tim = Turtle()
tim.penup()
tim.color("blue")
tim.ht()
stateNames = []
with open("../countriesFound.txt") as f:
    content = list(set(f.readlines()))
    for i in content:
        stateNames.append(i.replace('\n', ''))

for i in stateNames:
    tim.goto(int(data[data.state == i].x), int(data[data.state == i].y))
    tim.pendown()
    tim.write(i, False, align="center")
    tim.penup()

countriesFound = len(stateNames)
l = []
theDict = {}
StatesNotFound = []
answer = ''
while continueGame:
    answer = myScreen.textinput(f"{countriesFound}/50", "What's another state Name ?").title()
    if answer == "Exit":
        StatesNotFound = [j for j in theStates if j not in stateNames]
        theDict["Notfound"] = StatesNotFound
        newData = pandas.DataFrame(theDict)
        newData.to_csv("statesNotFound.csv")
        tim.goto(0, 220)
        tim.color("Red")
        tim.write(
            f"You have missed {50 - countriesFound} countries, you can go to the StatesNotFound.csv, to find all your "
            f"missing countries ",
            False, align="center", font=("serif", 10, "normal"))
        break

    if answer in theStates and answer not in stateNames:
        tim.goto(int(data[data.state == answer].x), int(data[data.state == answer].y))
        tim.color("green")
        tim.pendown()
        tim.write(answer, False, align="center")
        tim.penup()
        countriesFound += 1
        l.append(answer)

    theFinalList = list(set(l))
    print(theFinalList)
    with open("../countriesFound.txt", mode='a') as file:
        for i in theFinalList:
            file.write(f"{i}\n")

    if countriesFound == 50:
        continueGame = False
        tim.goto(0, 220)
        tim.color("Purple")
        tim.write("Congratulations", False, align="center", font=("serif", 20, "normal"))
myScreen.exitonclick()
