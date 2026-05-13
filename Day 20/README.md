## Day 20 - Snake Game Project (Part 1)

---

### 📌 Project Overview

Building the classic **Snake Game** using the turtle module. The goal is to practice creating objects, controlling movement, and handling collisions through hands-on coding.

The project is divided into 7 tasks, split into Part 1 and Part 2.

### 📝 Tasks

Part 1 (Basics):

1. Create the snake body
2. Move the snake
3. Control the snake


Part 2 (Game Mechanics):

4. Detect collision with food
5. Create a scoreboard
6. Detect collision with the wall
7. Detect collision with itself

---

## 🧠 Notes

---

### screen.tracer()
- Controls automatic screen updates in the turtle module.
- By default, every turtle movement immediately redraws the screen. If you move multiple segments quickly (like a snake), this can look slow or flickery.
```python
screen.tracer(0) # 0 → Turns off automatic updates.
```
- Now, the screen only updates when you call: `screen.update()`
- Any number n > 0 → Turtle will update the screen every n actions.

### time.sleep()
- Pauses the program for a set amount of time.
```python
import time
time.sleep(seconds)
```
Example:
```python
time.sleep(0.5)  # pause for half a second
```
- In Snake, we use it to control the snake's speed.
    - time.sleep(0.2) → The snake moves every 0.2 seconds.
    - Smaller value → snake moves faster
    - Larger value → snake moves slower

### range(start, stop, step)
counts from start to just before stop, in increments of step.
- If step = 1, it counts upwards.
- If step = -1, it counts backwards.