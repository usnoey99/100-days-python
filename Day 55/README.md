# Day 55 - Advanced Decorators, Rendering HTML, Parsing URLs and Flask Debugging

---

## 📌 Overview
Expanded Flask knowledge by rendering HTML templates, creating dynamic routes with URL parameters, and debugging Flask applications.  

Built a simple **Higher-Lower number guessing game** as a web application using Flask.  
The game generates a random number and gives feedback (too high / too low / correct) based on user input.

---
## 📝 Tasks
- The server generates a random number
- The user submits guesses through a web form
- The app responds with:
  - "Too high"
  - "Too low"
  - "Correct!"


### ✨ Additional Features
- Mobile-friendly UI improvements (larger input fields and buttons)
- Improved UX with GIF feedback for each result state
- Clean separation of result and input screens using Jinja templates
- Conditional rendering: input form is hidden when the game is completed
- "Start New Game" button appears only after correct answer

---

## 🧠 Notes

### Flask(__name__)
`Flask(__name__)` creates a Flask application instance.
`__name__` is a special built-in Python variable. Its value is `__main__` when the file is executed directly, or the module name when it is imported.  

Flask uses this value to determine the application's location, allowing it to find resources such as the `templates` and `static` folders.

### Flask URL Routes
A route maps a URL to a Python function.

```python
@app.route("/")
def home():
    return  "Hello, Flask!"
```
When a user visits `/`, Flask executes `home()` and returns the function's response.

### Dynamic URL Routing
Flask can capture values directly from the URL.

```python
@app.route("/user/<username>")
def greet(username):
    return f"Hello, {username}~"
```

Visiting:
```
/user/Alice
```

returns:
```
Hello, Alice~
```

### Rendering HTML
Flask can render HRML templates instead of returning plain text responses.
```python
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
```
Flask automatically searches for HTML files inside the `templates/` directory.

Project structure:

```text
project/
│
├── app.py
└── templates/
    └── index.html
```

Example `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask</title>
</head>
<body>
    <h1>Hello, Flask!</h1>
</body>
</html>
```

When a user visits `/`, Flask loads `templates/index.html`, renders it, and sends the resulting HTML to the browser.

### Advanced Decorators with `*args` and `**kwargs`
Basic decorators only work with functions that have fixed parameters.  

Using `*args` and `**kwargs` allos a decorator to wrap functions with any number of positional and keyword arguments.

```python
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        return  function(*args, **kwargs)
    return wrapper

@logging_decorator
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
```

Output:
```text
Calling greet
Hello, Alice!
```