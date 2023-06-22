from tkinter import *
from tkinter import messagebox
import random
from pyperclip import copy
DEFAULT_EMAIL = "testi@ukko.fi"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    copy(password)
    messagebox.showinfo(title="Copied", message="Copied to clipboard!")
    password_box.delete(0,END)
    password_box.insert(END, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_box.get()
    email = email_box.get()
    password = password_box.get()
    formatted_pw = f"{website} | {email} | {password}\n"


    if len(website) < 3 or len(password) <3:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        confirm = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if confirm:
            with open("./passwords.txt", "a") as pw_file:
                pw_file.write(formatted_pw)
                website_box.delete(0,END)
                password_box.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

logo = Canvas(width=200, height=200)
LOGO_IMG = PhotoImage(file="./logo.png")
logo.create_image(100,100,image=LOGO_IMG)
logo.grid(column=1, row=0)

# TODO 1: Website label and textbox
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_box = Entry(width=51)
website_box.grid(column=1, row=1, columnspan=2)
website_box.focus()

#TODO 2: Email/username label and textbox
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_box = Entry(width=51)
email_box.insert(END, DEFAULT_EMAIL) # Insert DEFAULT EMAIL to box
email_box.grid(column=1, row=2, columnspan=2)

#TODO 3: Password label, textbox
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_box = Entry(width=33)
password_box.grid(column=1, row=3)

#TODO 4: Generate password button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, padx=0, pady=0)

# TODO 5: Add button
add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()