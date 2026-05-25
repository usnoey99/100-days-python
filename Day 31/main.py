import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
new_word = ""
flip_timer = None

try:
    word_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pd.read_csv("data/english_words.csv")
    word_data.to_csv("data/words_to_learn.csv", index=False)

eng_word_dict = dict(zip(word_data["English"], word_data["Deutsch"]))


# ---------------------------- CARD MECHANISM ------------------------------- #
def flip_card():
    global new_word
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(language_text, text="Deutsch")
    canvas.itemconfig(word_text, text=eng_word_dict[new_word])

def new_flashcard():
    global new_word, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    if len(eng_word_dict) == 0:
        canvas.itemconfig(word_text, text="Finished!")
        return

    canvas.itemconfig(canvas_img, image=front_img)
    new_word = random.choice(list(eng_word_dict.keys()))
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=new_word)

    flip_timer = window.after(5000, flip_card)



# ---------------------------- RIGHT MECHANISM ------------------------------- #
def answer_right():
    global new_word
    eng_word_dict.pop(new_word)

    pd.DataFrame(
        list(eng_word_dict.items()),
        columns=["English", "Deutsch"]
    ).to_csv("data/words_to_learn.csv", index=False)

    new_flashcard()

# ---------------------------- WRONG MECHANISM ------------------------------- #
def answer_wrong():
    new_flashcard()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=810, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tk.PhotoImage(file="images/card_front.png")
back_img = tk.PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(10,0,image=front_img, anchor="nw")
canvas.grid(row=1,column=1,columnspan=2)

language_text = canvas.create_text(410, 150, font=FONT_LANGUAGE)
word_text = canvas.create_text(410, 300, font=FONT_WORD)

new_flashcard()


right_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=answer_right)
right_button.grid(row=2,column=1)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=answer_wrong)
wrong_button.grid(row=2,column=2)





window.mainloop()