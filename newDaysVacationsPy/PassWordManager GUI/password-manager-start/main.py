import random
from tkinter import *
from tkinter import messagebox
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PassWord Mananger")
window.minsize(width=200, height=210)
window.config(padx=20, pady=20)

theCanvas = Canvas(width=180, height=200, highlightthickness=0)
theImage = PhotoImage(file="logo.png")
theCanvas.create_image(90, 100, image=theImage)
theCanvas.grid(column=1, row=0)

theWebsiteLabel = Label(text="Website:", font=("Arial", 10, "normal"))
theWebsiteLabel.grid(column=0, row=1)

theEmailLabel = Label(text="Email/Username:", font=("Arial", 10, "normal"))
theEmailLabel.grid(column=0, row=2)

thePasswordLabel = Label(text="Password:", font=("Arial", 10, "normal"))
thePasswordLabel.grid(row=3, column=0)

theWebsiteEntry = Entry(width=25)
theWebsiteEntry.grid(column=1, row=1, columnspan=1)

theEmailEntry = Entry(width=35)
theEmailEntry.grid(column=1, row=2, columnspan=2)

thePasswordEntry = Entry(width=21)
thePasswordEntry.grid(column=1, row=3)


def GeneratePassWord():
    thePasswordEntry.delete(0, END)
    l = []
    others = ["/", "@", "_", "|", "%"]
    lettersUpper = random.randint(1, 4)
    lettersLower = random.randint(1, 5)
    number = random.randint(1, 4)
    other = random.randint(1, 4)

    for i in range(number):
        l.append(str(random.randint(0, 9)))

    for i in range(lettersLower):
        l.append(chr(random.randint(65, 90)))

    for i in range(lettersUpper):
        l.append(chr(random.randint(65, 90)).upper())

    for i in range(other):
        l.append(random.choice(others))

    random.shuffle(l)

    thePasswordEntry.insert(0, "".join(l))
    pyperclip.copy(thePasswordEntry.get())


theGenerateBtn = Button(text="Generate Password", command=GeneratePassWord)
theGenerateBtn.grid(column=2, row=3, columnspan=2)


def savePassWord():
    dictionaryPass = {}
    website = theWebsiteEntry.get().strip().title()
    email = theEmailEntry.get().strip()
    password = thePasswordEntry.get().strip()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askokcancel(title="error", message="You need to fill all empty entries before adding...")
    else:
        """with open("password.txt", mode='a') as file:
            file.write(f"{theWebsiteEntry.get()}|{theEmailEntry.get()}|{thePasswordEntry.get()}\n")
            messagebox.askokcancel(title="Process successful",
                                   message=f"the website: {website}|the email: {email}|the passWord: {password} \n")
        """
        dictionaryPass = {
            f"{website}": {
                "email": f"{email}",
                "password": f"{password}"
            }
        }
        try:
            data_file = open("password.json", "r")
            content = json.load(data_file)
        except FileNotFoundError:
            file = open("password.json", "w")

            json.dump(dictionaryPass, file, indent=4)
        else:
            content.update(dictionaryPass)
            print(content)
            data = open("password.json", "w")
            json.dump(content, data, indent=4)
        finally:
            theWebsiteEntry.delete(0, END)
            theEmailEntry.delete(0, END)
            thePasswordEntry.delete(0, END)

def search():
    website = theWebsiteEntry.get().strip().title()
    if len(website) == 0:
        messagebox.showinfo(title="Warning !!!", message="you need to fill the website entry first before click on the search button...")
    else:
        try:
            data_file = open("password.json")
            content = json.load(data_file)
        except KeyError:
            messagebox.showinfo(title="Process Failed", message=f"There is no register account for the website named {website} in our data")
        except FileNotFoundError:
            messagebox.showinfo(title="Process Failed", message="There is no data in where to find your account")
        else:
            thedict = content[website]
            messagebox.askokcancel(title=f"{website}",
                                   message=f"the website: {website}|the email: {thedict['email']}|the passWord: {thedict['password']} \n")

theSearchBtn = Button(text="Search", width=10, command=search)
theSearchBtn.grid(column=2, row=1, columnspan=2)

theAddButton = Button(text="Add", width=30, command=savePassWord)
theAddButton.grid(column=1, row=4, columnspan=2)

window.mainloop()
