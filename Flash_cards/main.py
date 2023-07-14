from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
options = ["Arabic",
           "Hebrew",
           "English",
           "Russian",
           "French"
           ]

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/ar_en_he_fr_ru_words.csv")
    # original_data = pandas.read_csv("data/french_words.csv")
    # print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # canvas.itemconfig(card_title, text="French", fill="black")
    # canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text=clicked_from.get(), fill="black")
    canvas.itemconfig(card_word, text=current_card[clicked_from.get()], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # canvas.itemconfig(card_title, text="English", fill="white")
    # canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_title, text=clicked_to.get(), fill="white")
    canvas.itemconfig(card_word, text=current_card[clicked_to.get()], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -----------UI---------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
# canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=1, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=2, column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, highlightthickness=0, command=is_known)
known_btn.grid(row=2, column=1)

lbl_choose_from = Label(window, text="From:", width="20", font=("Ariel", 10), bg=BACKGROUND_COLOR, highlightthickness=0)
lbl_choose_to = Label(window, text="To:", width="20", font=("Ariel", 10), bg=BACKGROUND_COLOR, highlightthickness=0)
lbl_choose_from.place(x=50, y=5)
lbl_choose_to.place(x=455, y=5)

clicked_from = StringVar(window)
clicked_from.set(options[2])
clicked_to = StringVar(window)
clicked_to.set(options[4])

drop_from = OptionMenu(window, clicked_from, *options)
drop_from.config(bg=BACKGROUND_COLOR, highlightthickness=0)
drop_from.grid(column=0, row=0)
drop_to = OptionMenu(window, clicked_to, *options)
drop_to.config(bg=BACKGROUND_COLOR, highlightthickness=0)
drop_to.grid(column=1, row=0)

next_card()

window.mainloop()
