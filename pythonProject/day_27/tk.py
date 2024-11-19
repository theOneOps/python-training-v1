from tkinter import *

window = Tk()
window.minsize(width=300, height=200)
window.title('Mile to Km Converter')
window.config(padx=100, pady=100)

put = Entry(width=10)
put.grid(column=1, row=0)

Miles = Label(text="Miles", font=("verdana", 10, 'bold'))
Miles.config(padx=10, pady=10)
Miles.grid(column=2, row=0)

is_equal = Label(text='is equal', font=("verdana", 10, 'normal'))
is_equal.config(padx=10, pady=10)
is_equal.grid(column=0, row=1)

result = Label('',font=("verdana", 15, 'bold'))
result.config(padx=10, pady=10)
result.grid(column=1, row=1)


Km = Label(text='Km', font=("verdana", 10, 'bold'))
Km.config(padx=10, pady=10)
Km.grid(column=2, row=1)


def calculate():
    factor = 1.609344
    f = round(factor, 1)
    r = (float(put.get()) * f)
    result.config(text=r)


calcul_btn = Button(text='Calculate', command=calculate)
calcul_btn.config(padx=5, pady=5)
calcul_btn.grid(column=1, row=2)
window.mainloop()
