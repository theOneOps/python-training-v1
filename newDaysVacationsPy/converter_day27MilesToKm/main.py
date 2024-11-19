from tkinter import *

window = Tk()
window.title("Mile to km converter")
window.config(padx=30, pady=10)

inputNumber = Entry(width=10)
inputNumber.grid(row=0, column=1)

inputUnite = Label(text="Miles")
inputUnite.grid(row=0, column=2)

equal = Label(text="is equal")
equal.grid(row=1, column=0)

answer = Label(text="")
answer.grid(row=1, column=1)

answerUnite = Label(text="Km")
answerUnite.grid(row=1, column=2)


def calculate():
    entries = round(int(inputNumber.get()) * 1.609)
    answer.config(text=entries)


btnCalculate = Button(text="Calculate", command=calculate)
btnCalculate.grid(row=2, column=1)

window.mainloop()
