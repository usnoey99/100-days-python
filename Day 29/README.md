## Day 29 - Building a Password Manager

---

### 📌 Overview
A local password manager application built with Python and Tkinter.

It allows users to generate strong random passwords and securely store them in a local data file.  
The app also includes basic input validation and user confirmation dialogs to prevent accidental or incomplete data saving.

---

### 📝 Tasks
- Build the basic UI layout using Tkinter
- Implement input validation to prevent saving empty fields
- Add a popup warning if any required field is empty
- Add a confirmation dialog before saving data
- Save confirmed data
- Generate strong random passwords with letters, numbers, and symbols

---

### Improvements
- Auto-focus on website input field at startup
- Default email inserted automatically
- Automatically copy generated passwords to the clipboard
- Save confirmed data into a local CSV file using pandas

---

## 🧠 Notes

### tkinter Entry (delete / insert)
```python
entry.delete(0, tk.END)
entry.insert(0, "text")
```

### messagebox
Used to show popup dialogs for user interaction.
```python
messagebox.showinfo(title, message) # Displays an information popup
messagebox.askokcancel(title, message) # Displays a confirmation dialog
# Returns True (OK) or False (Cancel)
```

### columnspan, sticky
Allows spanning multiple columns, aligns widget to the east (right)
```python
widget.grid(row=2, column=2, columnspan=2, sticky="e")
```

### pyperclip
A library used to copy text to the clipboard.
```python
pyperclip.copy(generated_password)
```
- Automatically copies the generated password.
- Removes the need for manual copying.