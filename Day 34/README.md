## Day 34 - The trivia API and the Quizzler App

---

### 📌 Overview
Building a GUI-based quiz application using Tkinter and data from an external Trivia API.

Instead of using hardcoded questions and answers, the application retrieves random True/False questions from an API each time it runs. The quiz tracks the user's score, provides visual feedback, and displays questions through a graphical user interface.

---

### 📝 Tasks
- Modify the data.py file to fetch quiz questions from an API
- Make a GET request to retrieve 15 True/False questions
- Parse the JSON response and replace the value of question_data
- Build a class-based Tkinter user interface
- Display questions dynamically on a canvas
- Validate user answers and update the score
- Provide visual feedback for correct and incorrect answers
- Disable answer buttons when the quiz is completed

---

## 🧠 Notes

### html.unescape()
Some questions returned by the API contain HTML entities.

Example:
```
Tom Clancy&#039;s Ghost Recon
```
The `html.unescape()` function converts HTML entities into readable characters.

Example:
```
import html
text = "Tom Clancy&#039;s Ghost Recon"
print(html.unescape(text))
```
Output:
```
Tom Clancy's Ghost Recon
```

### Class-Based Tkinter UI
Instead of writing all Tkinter code in a single file, the interface can be organized into a class.

Example:
```python
class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
```
This approach makes it easier to manage widgets, events, and application state while keeping the UI separate from the quiz logic.

### Canvas Text Width
The `width` parameter of `create_text()` controls when text wraps onto the next line.

Example:
```
self.canvas.create_text(
    150,
    125,
    width=280,
    text="Question Text"
)
```
This prevents long questions from extending beyond the canvas boundaries.

### state="disabled"
Widgets can be disabled to prevent further user interaction.

Example:
```
button.config(state="disabled")
```
In the Quizzler app, the answer buttons are disabled when the user reaches the end of the quiz.

### Tkinter's after() Method
While `mainloop()` is running, using `time.sleep()` will freeze the entire interface.

Instead, Tkinter provides the `after()` method to schedule a function call after a specified delay.

Example:
```python
window.after(1000, next_question)
```
This allows the application to briefly display feedback before loading the next question without blocking the GUI.