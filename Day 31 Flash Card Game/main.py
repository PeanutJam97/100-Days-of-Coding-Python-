from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = 0

try:
    data = pd.read_csv(".\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def word_generator():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.randint(0, len(data_dict))
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=data_dict[current_card]["French"], fill="black")
    flip_timer = window.after(ms=3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=data_dict[current_card]["English"], fill="white")

def remove_word():
    data_dict.remove(data_dict[current_card])
    df = pd.DataFrame(data_dict)
    df.to_csv(".\data\words_to_learn.csv", index=False)
    word_generator()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=word_generator)
wrong_button.grid(column=0, row=1)








mainloop()