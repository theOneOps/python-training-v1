from turtle import Turtle,Screen

ninja=Turtle();
ninja.color("green","blue")
ninja.shape("turtle")
ninja.shapesize(1,1,5)
ninja.resizemode("user")
myscreen=Screen()

def forward():
    ninja.fd(90);
def backward():
    ninja.backward(90);
def left():
    new_heading=ninja.heading()+10
    ninja.setheading(new_heading)
def right():
    new_heading = ninja.heading() - 10
    ninja.setheading(new_heading)

def clear():
    ninja.clear()
    ninja.penup()
    ninja.home()
    ninja.pendown()

myscreen.listen();
myscreen.onkey(forward,"Up")
myscreen.onkey(right,"Right")
myscreen.onkey(left,"Left")
myscreen.onkey(backward,"Down")
myscreen.onkey(clear,"c")
myscreen.exitonclick()
print(myscreen.getshapes())
