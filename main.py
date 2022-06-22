from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_text.get().title(): {
            "email": email_text.get(),
            "password": password_text.get(),
        }
    }

    if len(website_text.get()) == 0 or len(email_text.get()) == 0 or len(password_text.get()) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        website_text.delete(0, END)
        password_text.delete(0, END)


# ---------------------------- Search Website ------------------------------- #

def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website_text.get().title() in data:
            messagebox.showinfo(title=f"{website_text.get()}",
                                message=f"Email: {data[website_text.get().title()]['email']} \n\nPassword: {data[website_text.get().title()]['password']}")
        else:
            messagebox.showinfo(title=f"{website_text.get()}", message="No details for the website exist")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

website = Label(text="Website:", font=('Times New Roman', 14, 'normal'))
website.grid(column=0, row=1)

email = Label(text="Email/Username:", font=('Times New Roman', 14, 'normal'))
email.grid(column=0, row=2)

password = Label(text="Password:", font=('Times New Roman', 14, 'normal'))
password.grid(column=0, row=3)

website_text = Entry(width=33)
website_text.grid(column=1, row=1, columnspan=2, sticky="w")
website_text.focus()

email_text = Entry(width=49)
email_text.grid(column=1, row=2, columnspan=2, sticky="w")
email_text.insert(0, "dannys77222@gmail.com")

password_text = Entry(width=33)
password_text.grid(column=1, row=3, sticky="w")

generate_password = Button(text="Generate", width=12, command=generate_pass)
generate_password.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=41, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

window.mainloop()
