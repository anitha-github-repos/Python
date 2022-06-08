from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


#--------------------------------Create new flash card---------------#
def csv_read():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(front, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(front, image=card_back_img)

def is_known():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    csv_read()

#---------------------------UI SetUP-----------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
#window.configure(bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")


front = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 20, "italic"))
word = canvas.create_text(400, 240, text="word", font=("Ariel", 30, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_png = PhotoImage(file="images/right.png")
wrong_png = PhotoImage(file="images/wrong.png")

unknown_button = Button(imag=right_png, highlightthickness=0, command=csv_read)
unknown_button.grid(column=0, row=1)

right_button = Button(image=wrong_png, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)






window.mainloop()