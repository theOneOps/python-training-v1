from tkinter import *
import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random

def generate_password():
    length_pass = len(password_entry.get())
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(5, 8)
    nr_symbols = random.randint(5, 8)
    nr_numbers = random.randint(5, 8)

    l = [random.choice(letters) for ind in range(nr_letters)]
    n = [random.choice(numbers) for i in range(nr_numbers)]
    s = [random.choice(symbols) for j in range(nr_symbols)]
    final_list = l+s+n
    random.shuffle(final_list)

    mdp = "".join(final_list)
    print(f'the password is {mdp}')
    if length_pass == 0:
        password_entry.insert(0, mdp)
        pyperclip.copy(mdp)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    pass_word = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":pass_word
        }
    }
    if pass_word == "" or email == "" or pass_word == "":
        messagebox.showinfo(title="oops", message="every entry such as email, or website or password should be filled before adding")
    else:
        messagebox.showinfo(title="ok", message=f"the website is {website} the email you enter is {email} and your password is {pass_word}")
        #with open('recover_pass.json', 'r') as file:
            #content = file.read()
            #if content == "":
                #with open('recover_pass.txt', 'w') as files:
                    #files.write(f"website:{website}|email:{email}|password:{pass_word}\n")
            #else:
                #with open('recover_pass.txt', 'a') as new_file:
                    #new_file.write(f"website:{website}|email:{email}|password:{pass_word}\n")
        try:
            with open("recover_pass.json", "r") as file:
                data = json.load(file)
                if website in data:
                    data[website]["email"] = email
                    data[website]["password"] = pass_word
                else:
                    data.update(new_data)
            with open("recover_pass.json", "w") as n_file:
                json.dump(data, n_file, indent=4)
        except FileNotFoundError:
            with open("recover_pass.json", "w") as new_file:
                json.dump(new_data, new_file, indent=4)

        password_entry.delete(0, END)
        email_entry.delete(0, END)
        website_entry.delete(0, END)


# ---------------------------- Search password managememnt ------------------------------- #

def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="error", message="you have to fill the website's entry before sending your request with the search 's button")
    else:
        try:
            with open('recover_pass.json', 'r') as file:
                data = json.load(file)
        except:
            messagebox.showinfo(title="request failed", message="there is no save account in our database ,try to save some before searching for account")
        else:
            with open('recover_pass.json', 'r') as file:
                data = json.load(file)
            if website in data:
                print(data[website])
                messagebox.showinfo(title="request successful", message=f"website:{website} \n email:{data[website]['email']} \n password: {data[website]['password']}")
            else:
                messagebox.showinfo(title="request failed", message=f"we don't have in our database your account for the website: '{website}'")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title('Password manager')

#Labels

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='email/username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)



canvas = Canvas(width=200, height=200)
the_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=the_image)
canvas.grid(column=1, row=0)

#Entry

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

#btns

btn_search = Button(text='search', width=10, command=search)
btn_search.grid(column=2, row=1)

generate_pass = Button(text='Generate', width=10, command=generate_password)
generate_pass.grid(column=2, row=3)

btn_add = Button(text='ADD', width=29, command=add)
btn_add.grid(column=1, row=4)

window.mainloop()