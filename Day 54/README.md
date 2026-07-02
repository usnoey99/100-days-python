# Day 54 - Command Line, Python Decorators and Web Development with Flask

---

## 📌 Overview

Learned the fundamentals of **Flask**, a lightweight Python web framework, and built a simple web server.

This project also introduced Python decorators and core concepts like __name__ and __main__, which are essential for understanding how Python scripts and web applications are executed.

---

## 📝 Tasks

* Build a simple web server with Flask
* Run a Flask application from the command line
* Create routes using decorators
* Understand how URL routing works
* Learn the roles of `__name__` and `__main__`

---

## 🧠 Notes

### Running Flask Applications

The recommended way to run a Flask application is without setting environment variables.

```bash
flask --app hello run
```

or

```bash
python -m flask --app hello run
```

These commands tell Flask to locate the `app` object inside `hello.py` and start the development server.

To stop the server, press **Ctrl + C**.

---

### `__name__`

`__name__` is a built-in Python variable that stores the name of the current module.

`hello.py`

```python
print(__name__)
```

When the file is executed directly:

```bash
python hello.py
```

Output:

```text
__main__
```

This means the file is being executed as the program's entry point.

When the file is imported by another module:

```python
import hello
```

Output:

```text
hello
```

In this case, `hello.py` is imported as a module, so its module name is displayed instead of `__main__`.

---

### `__main__`

`__main__` is a special string assigned to `__name__` when a Python file is executed directly.

```python
if __name__ == "__main__":
    print("Run")
```

This block is executed only when the file is run directly, not when it is imported by another module.

---

### Python Decorators

A decorator is a Python feature that allows additional functionality to be added to a function without modifying its original code.

```python
@app.route("/")
def hello():
    return "Hello"
```

is functionally equivalent to:

```python
def hello():
    return "Hello"

hello = app.route("/")(hello)
```
Flask registers the `hello` function in its internal routing table, allowing it to be called whenever a user visits the `/` URL.


Example:
```python
def speed_calc_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
    return wrapper
```
Equivalent to:
```python
fast_function = speed_calc_decorator(fast_function)
```
