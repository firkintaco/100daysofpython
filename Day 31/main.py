BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
current_card = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
dict = pandas.DataFrame.to_dict(data,orient="records")

#--------------------------- Random word ---------------------------#
def new_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(dict)
    print(current_card)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_word, text=current_card['French'], fill="black")
    card.itemconfig(card_bg, image=card_img)
    print(current_card['French'])
    flip_timer = screen.after(3000, func=flip_card)

def flip_card():

    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_word, text=current_card["English"], fill="white")
    card.itemconfig(card_bg, image=card_back_img)

def is_known():
    dict.remove(current_card)
    data = pandas.DataFrame(dict)
    data.to_csv("./data/words_to_learn.csv", index=False)

    new_card()
#--------------------------- UI ---------------------------#

screen = Tk()
screen.title("Flash Card")
screen.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000, func=flip_card)

wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")
card_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = card.create_image(400,261, image=card_img)
card_title = card.create_text(400,150, text="French",font=("Arial",40, "italic"))
card_word = card.create_text(400,263,text="trouve", font=("Arial", 60, "bold"))
card.grid(column=0, row=0,columnspan=2)

# Right button
right = Button(image=right_img, borderwidth=0, highlightthickness=0, command=is_known)
right.grid(row=1,column=1)

# Wrong button
wrong = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=new_card)
wrong.grid(row=1, column=0)

new_card()

screen.mainloop()