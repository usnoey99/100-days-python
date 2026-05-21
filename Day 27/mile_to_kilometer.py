from tkinter import *

window = Tk()
window.title("Mile ↔ Kilometer Converter")
window.config(padx=30, pady=30)

mode = IntVar(value=1)

entry = Entry(width=10)
entry.grid(row=0, column=0)

label_middle = Label(text="is equal to", font=("Arial", 14))
label_middle.grid(row=0, column=1)

result_label = Label(text="          ", font=("Arial", 14))
result_label.grid(row=0, column=2)

def convert():
    try:
        value = float(entry.get())

        if mode.get() == 1:
            result = value * 1.609
        else:
            result = value / 1.609

        result_label.config(text=f"{result:.3f}")

    except ValueError:
        result_label.config(text="          ")

Radiobutton(text="Miles → Km", variable=mode, value=1).grid(row=1, column=0, padx=10)
Radiobutton(text="Km → Miles", variable=mode, value=2).grid(row=1, column=1, padx=10)

Button(text="Convert", command=convert).grid(row=2, column=1)

window.mainloop()