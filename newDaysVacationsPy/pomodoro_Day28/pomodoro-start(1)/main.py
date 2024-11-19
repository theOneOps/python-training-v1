from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 15
reps = 0
theTimer = None
counter = ""

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro app")
window.config(padx=50, pady=30, bg=YELLOW)

titre = Label(text="Timer", font=(FONT_NAME, 30, "bold"))
titre.config(bg=YELLOW, fg=GREEN)
titre.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
theImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=theImage)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 20, "bold"))
canvas.grid(column=1, row=1)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countDown(a):
    global reps, theTimer, counter
    seconds = math.floor(a % 60)
    minutes = math.floor(a / 60)

    if seconds < 10:
        canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if reps == 9:
        reps = 0
        counter += ' ✔'
        EntrieValided.config(text=counter, fg=GREEN)
        return

    if a > 0:
        theTimer = window.after(1000, countDown, a - 1)
    else:
        initializePomodoro()


# ---------------------------- TIMER MECHANISM ------------------------------- #

def initializePomodoro():
    global reps, counter
    reps += 1

    if reps % 8 == 0:
        countDown(LONG_BREAK_MIN * 60)
        titre.config(text="LONG BREAK", fg=PINK)
    elif reps % 2 == 0:
        countDown(SHORT_BREAK_MIN * 60)
        titre.config(text="SHORT BREAK", fg=RED)
    else:
        countDown(WORK_MIN * 60)
        titre.config(text="WORK", fg=GREEN)
    print(reps)


# ---------------------------- TIMER RESET ------------------------------- #

def resetPomodoro():
    global theTimer, reps
    window.after_cancel(theTimer)
    titre.config(text="Timer reset")
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    counterInd = ""
    EntrieValided.config(text=counterInd)


startBtn = Button(text="Start", command=initializePomodoro)
startBtn.config(width=8, font=(FONT_NAME, 15))
startBtn.grid(column=0, row=2)

resetBtn = Button(text="Reset", command=resetPomodoro)
resetBtn.config(width=8, font=(FONT_NAME, 15))
resetBtn.grid(column=2, row=2)

EntrieValided = Label(text="")
EntrieValided.grid(column=1, row=4)

window.mainloop()
