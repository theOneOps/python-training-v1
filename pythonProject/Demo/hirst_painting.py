
import colorgram
import turtle as t
import random
l = colorgram.extract('image_dot.jpg',20)
t.colormode(255)
liste=[]
for i in range(len(l)):
    color=l[i]
    rgb=color.rgb
    a = rgb[0]
    b = rgb[1]
    c = rgb[2]
    coolor = (a, b, c)
    liste.append(coolor)


tim = t.Turtle()
screen = t.Screen()
screen.bgcolor("grey")
x = 180
tim.speed(0)
tim.penup()
for i in range(18):
    tim.setheading(x)
    for j in range(10):
        colors = random.choice(liste)
        tim.dot(5, colors)
        tim.bk(50)
        x-=10
    tim.setpos(0,0)

screen.exitonclick()