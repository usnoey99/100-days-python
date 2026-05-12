## Day 19 - Turtle Race Game (Instances, State and Higher Order Functions)

---

### 📌 Project Overview

Today I built a **Turtle Racing Game** using Python’s `turtle` module.  
The game allows the user to bet on a turtle color and watch a random race.

Key concepts used:
- Instances (multiple turtle objects)
- State (position, color, movement)
- Higher-order functions (keyboard events)
- User input with popups
- Game reset logic

---

### 🎮 Game Features

- 6 racing turtles with different colors
- User places a bet using a popup window
- Random movement for each turtle
- Winner detection based on x-coordinate
- Result popup (win / lose)
- Option to play again
- Game reset system

---

## 🧠 Notes

---

### `screen.listen()`

Starts listening for keyboard input.

- Without this, `onkey()` and `onkeypress()` will not work properly.
- Must be called before keyboard events.


### `screen.onkey()`

```Python
screen.onkey(function_name, "key")
```

- Connects a key to a function
- Pass function name only (no parentheses)

Correct: 
```Python
screen.onkey(move_forwards, "Up")
```

Incorrect: 
```Python
screen.onkey(move_forwards(), "Up")
```

### `screen.onkeypress()`

- Runs when key is pressed (more immediate response)


### Higher Order Functions

Functions as Inputs

takes another function as input, or returns a function

```Python
def function_a(func):
    func()

def function_b():
    print("Hello")

function_a(function_b)
```
We pass the function name without ()