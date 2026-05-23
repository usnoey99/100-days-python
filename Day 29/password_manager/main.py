import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
import pyperclip

FONT_STANDARD = ("Arial", 11, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    pw_letters = [random.choice(letters) for _ in range(nr_letters)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = pw_letters + pw_numbers + pw_symbols
    random.shuffle(password_list)

    generated_password = "".join(password_list)

    pw_entry.delete(0, tk.END)
    pw_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_data = website_entry.get().lower() # Avoid duplication
    id_data = id_entry.get()
    pw_data = pw_entry.get()


    if len(web_data) == 0 or len(id_data) == 0 or len(pw_data) == 0:
        messagebox.showinfo(title="Info", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=web_data, message="These are the details entered: "
                                                       f"\nE-Mail/Username: {id_data}"
                                                       f"\nPassword: {pw_data}"
                                                       f"\nIs it OK to save?")

        if is_ok:
            new_data = {
                "Website" : [web_data],
                "ID" : [id_data],
                "PW" : [pw_data]
            }

            new_df = pd.DataFrame(new_data)

            try:
                old_df = pd.read_csv("data.csv")
                update_df = pd.concat([old_df, new_df], ignore_index=True)

            except FileNotFoundError:
                update_df = new_df

            update_df.to_csv("data.csv", index=False)

            website_entry.delete(0, tk.END)
            id_entry.delete(0, tk.END)
            id_entry.insert(0, "example@email.com")
            pw_entry.delete(0, tk.END)
            website_entry.focus()



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

# Website: entry
website_text = tk.Label(text="Website: ",font=FONT_STANDARD)
website_text.grid(row=2, column=1, sticky="e")

website_entry = tk.Entry(width=43, font=FONT_STANDARD)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=2, ipady=3, padx=2, pady=2)

# Email/Username: entry
id_text = tk.Label(text="E-Mail/Username: ", font=FONT_STANDARD)
id_text.grid(row=3, column=1, sticky="e")

id_entry = tk.Entry(width=43, font=FONT_STANDARD)
id_entry.insert(0, "example@email.com")
id_entry.grid(row=3, column=2, columnspan=2, ipady=3, padx=2, pady=2)

# Password: entry width 21
pw_text = tk.Label(text="Password: ", font=FONT_STANDARD)
pw_text.grid(row=4, column=1, sticky="e")

pw_entry = tk.Entry(width=24, font=FONT_STANDARD)
pw_entry.grid(row=4, column=2, ipady=3, padx=2, pady=2)

# Generate Password Button
pw_button = tk.Button(text="Generate Password", font=FONT_STANDARD, command=generate_password)
pw_button.grid(row=4, column=3, padx=2, pady=2, sticky="w")

# Add Button width 36
add_button = tk.Button(text="Add", width=38, font=FONT_STANDARD, command=save_password)
add_button.grid(row=5, column=2, columnspan=2, padx=2, pady=2)

window.mainloop()