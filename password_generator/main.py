from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

import pyperclip

WHITE = "#FFFFFF"
FONT_NAME = "Courier"
DATA = "data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(DATA, "r") as dat_file:
                # reading old data
                data = json.load(dat_file)
        except FileNotFoundError:
            with open(DATA, "w") as dat_file:
                json.dump(new_data, dat_file, indent=4)
                # data = json.load(dat_file)
        else:
            # Update the data
            data.update(new_data)

            with open(DATA, "w") as data_file:
                # saving updates data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "email@email.com")


# ----------------------------Search website--------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(DATA, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website: ", bg=WHITE, font=(FONT_NAME, 15, "bold"))
email_lbl = Label(text="Email/Username: ", bg=WHITE, font=(FONT_NAME, 15, "bold"))
password_lbl = Label(text="Password: ", bg=WHITE, font=(FONT_NAME, 15, "bold"))
website_lbl.grid(column=0, row=1)
email_lbl.grid(column=0, row=2)
password_lbl.grid(column=0, row=3)

generate_bt = Button(text="Generate Password", command=generate_pass, width=14, bg=WHITE, highlightthickness=0)
add_bt = Button(text="Add", command=save_pass, width=43, bg=WHITE, highlightthickness=0)
generate_bt.grid(column=2, row=3)
add_bt.grid(column=1, row=4, columnspan=2)
search_bt = Button(text="Search", command=find_password, width=14, bg=WHITE, highlightthickness=0)
search_bt.grid(column=2, row=1)

# Entry
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "email@email.com")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

window.mainloop()
