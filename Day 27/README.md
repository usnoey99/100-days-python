## Day 27 - Graphical User Interfaces with Tkinter and Function Arguments

---

### 📌 Overview
Learned how to create graphical user interfaces using the Python Tkinter module.

Practiced creating labels and buttons, handling button click events, accepting user input, and designing application layouts.

Also explored advanced Python function features including default arguments, `*args`, and `**kwargs`.

---

### 📝 Tasks
- Create a Tkinter window with labels, buttons, and entry widgets.
- Practice using .pack(), .grid(), and .place() for layout.
- Build a simple button click event using command.
- Get user input using .get() and display/update results.
- Practice using *args and **kwargs in simple functions.
- Build a basic Mile ↔ Kilometer converter project.

---

## 🧠 Notes

### Tk()
Creates the main application window.
```python
import tkinter as tk
window = tk.Tk()
window.title("My App")
window.mainloop()
```
- every Tkinter app starts with `Tk()`
- `mainloop()` keeps the window running

### .minsize()
Sets the minimum size of the window.
```python
window.minsize(width=300, height=300)
```
- prevents the window from becoming smaller than the given size.

### Label()
Creates a text label widget.
```python
label = tk.Label(text="Hello World")
label.pack()
```
Common options:
```python
label = tk.Label(
    text="Hello",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="yellow"
)
```
- `font` - font style and size
- `fg` - text colour
- `bg` - background colour

### .pack()
Places widgets automatically relative to each other on the screen

Position options:
```python
label.pack(side="left")
```
-`"top"` (default), `"bottom"`, `"left"`, `"right"`
Padding:
```python
label.pack(padx=10, pady=10)
```
- `padx` - horizontal spacing
- `pady` - vertical spacing

### .place()
Place widgets using exact coordinates.
```python
label.place(x=100, y=50)
```

### .grid()
Places widgets using rows and columns.
```python
label = tk.Label(text="Hello")
label.grid(row=0,column=0)
tk.Entry().grid(row=0,column=1)
```
Looks like a table structure.

Do not mix `pack()` and `grid()` inside the same parent window.

This causes `_tkinter.TclError`.


### Button()
Creates a clickable button.
```python
def button_clicked():
    print("Button was clicked")
button = tk.Button(
    text="Click Me",
    command=button_clicked
)
button.pack()
```
- `command` runs a function when the button is clicked.
- do not use parentheses in `command=button_clicked`.

### Entry()
Creates a text input field.
```python
entry = tk.Entry(width=20)
entry.pack()
```
Get user input:
```python
user_text = entry.get()
print(user_text)
```
- `.get()` returns the current text inside the entry box.

### .config()
Changes widget properties after creation.
```python
label.config(text="Edit")
```
Another way to modify widgets:
```python
label["text"] = "Edit"
```
Updates the label text using dictionary-style syntax.

### .get()
```python
input.get()
```
- `input.get()` runs immediately.
- The user has not typed anything yet.
- So the label becomes an empty string.

### *args - Unlimited Arguments
Accepts multiple positional arguments.
```python
def add(*args):
    total = sum(args)
    print(total)

add(1, 2, 3) # Output: 6
```
- `args` is treated as a tuple.

### *kwargs - Many Keyworded Arguments
Accepts multiple keyword arguments.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="Kim", age=25)
```
Output:
```python
name Kim
age 25
```
Internal dictionary:
```python
{
    "name": "Kim",
    "age": 25
}
```
- `kwargs` is treated as a dictionary.
- useful for flexible function arguments.

