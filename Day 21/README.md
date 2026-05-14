## Day 21 - Snake Game Project (Part 2)

---

### 📌 Project Overview

Building the classic **Snake Game** using the turtle module. The goal is to practice creating objects, controlling movement, and handling collisions through hands-on coding.

The project is divided into 7 tasks, split into Part 1 and Part 2.

### 📝 Tasks

Day 20 - Part 1 (Basics):

1. Create the snake body
2. Move the snake
3. Control the snake

Day 21 – Part 2 (Game Mechanics):
4. Detect collision with food

5. Create a scoreboard

6. Detect collision with the wall

7. Detect collision with itself


**Extended feature**:
- Obstacles appear based on score
- Every 5 points → new obstacle added
- Maximum 7 obstacles
- Obstacles reposition dynamically


---

## 🧠 Notes

---

### Class inheritance

**Class inheritance** in Python allows one class to reuse and extend the behaviour of another class.

```python
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
```
Animal is the parent class (or base class).

```python
class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this underwater.")
```
It means Fish inherits from Animal.

So Fish automatically gets:
- the `num_eyes` attribute
- the `breathe()` method
unless it overrides them.


### Why use `super().__init__()`?
When we define a new __init__ inside Fish, Python does not automatically call the parent's __init__.

### Without `super().breathe()`
Fish is overriding the parent's breathe() method.

That means when we call `fish.breath()` Python only executes Fish.breathe().

The parent's version is NOT automatically included.

The original parent behaviour is completely replaced.

Using `super()` means, extend the parent's method instead of completely replacing it.

```python
class Fish(Animal):
    def breathe(self):
        super().breathe()
        print("doing this underwater.")
```
```
Output:
Inhale, exhale.
doing this underwater.
```

### shapesize(stretch_wid, stretch_len, outline)
- stretch_wid: Vertical scaling
- stretch_len: Horizontal scaling
- outline    : Border thickness

```python
from turtle import Turtle

tim = Turtle()

tim.shape("turtle")
tim.shapesize(stretch_len=2, stretch_wid=3)
```
This makes the turtle:
- 2× longer
- 3× taller

`shapesize()` only changes the **visual appearance** of the turtle shape.

It does NOT affect movement or collision logic, only visual representation.

### Slicing
a way to extract part of a sequence such as lists, strings or tuples.
The general syntax is: `sequence[start:end:step]`
```python
my_list[start:end]
```
From index start up to (but not including) index end. The end index is excluded.

Pattern example:
```python
my_list[1:]     # everything except first
my_list[:-1]    # everything except last
my_list[::-1]   # reversed
my_list[:]      # full copy
```
