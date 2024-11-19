from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 / 5
SHORT_BREAK_MIN = 1 / 20
LONG_BREAK_MIN = 1 / 10
rep = 0
timer_start = None
check = '✓'


# ------------------------------SETUP TIMER--------------------------------------#


def start_pom():
    global rep
    rep += 1
    work_time = WORK_MIN * 60
    short_break = int(SHORT_BREAK_MIN * 60)
    long_break = LONG_BREAK_MIN * 60

    if rep % 5 == 0:
        clock(long_break)
        timer_label.config(text='LONG BREAK', font=('Serif', 25, 'bold'), bg=YELLOW)
        window.config(padx=100, pady=50, bg=YELLOW)
        canvas.config(bg=YELLOW)
        check_btn.config(bg=YELLOW)

    elif rep % 2 == 0:
        clock(short_break)
        timer_label.config(text='BREAK', font=('Serif', 25, 'bold'), bg=PINK)
        window.config(padx=100, pady=50, bg=PINK)
        canvas.config(bg=PINK)
        check_btn.config(bg=PINK)
    else:
        clock(work_time)
        timer_label.config(text='WORK', font=('Serif', 25, 'bold'), bg=GREEN)
        window.config(padx=100, pady=50, bg=GREEN)
        canvas.config(bg=GREEN)
        check_btn.config(bg=GREEN)


# ------------------------------SETUP TIMER MECHANISM----------------------------#

def clock(time):
    global timer_start, rep, check
    root_min = math.floor(time / 60)
    root_sec = int(time % 60)

    if root_sec < 10:
        root_sec = f"0{root_sec}"

    if root_min >= 0:
        canvas.itemconfig(timer_rst, text=f"{root_min}:{root_sec}")
    timer_start = window.after(1000, clock, time - 1)

    if time == 0:
        start_pom()
        check_btn.config(text=check)
        if rep % 2 != 0 and rep % 5 != 0:
            check += '✓'

    if rep > 5:
        window.after_cancel(timer_start)
        rep = 0
        top = Toplevel(window)
        top.title("End of pomodoro try")
        Label(top, text="You have reached this application timer limits..., you can reset and then start again :) ",
              font='Serif 20 normal').grid(column=1, row=0)


def reset():
    global timer_start, rep
    window.after_cancel(timer_start)
    rep = 0
    canvas.itemconfig(timer_rst, text='00:00')
    timer_label.config(text='TIMER', font=('Serif', 25, 'bold'), bg=YELLOW)
    window.config(padx=100, pady=50, bg=YELLOW)
    canvas.config(bg=YELLOW)
    check_btn.config(text='', bg=YELLOW)


# -------------------------------------------------------------------#


window = Tk()
window.title('Pomodoro project')
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text='Timer')
timer_label.config(font=('Serif', 25, 'bold'), bg=YELLOW)
timer_label.grid(column=1, row=0)
the_image = PhotoImage(file='tomato.png')
canvas = Canvas(width=225, height=225, highlightthickness=0)
canvas.create_image(112, 112, image=the_image)
canvas.config(bg=YELLOW)
timer_rst = canvas.create_text(112, 130, text='00:00', fill='white', font=('serif', 30, 'bold'))
canvas.grid(column=1, row=1)
# btns
start_btn = Button(text='Start', command=start_pom, highlightthickness=0)
start_btn.grid(column=0, row=2)
reset_btn = Button(text='Reset', command=reset, highlightthickness=0)
reset_btn.grid(column=2, row=2)

check_btn = Label(text='', highlightthickness=0)
check_btn.config(bg=YELLOW)
check_btn.grid(column=1, row=3)
window.mainloop()
