## Day 28 - Building Pomodoro App

---

### 📌 Overview
A simple Pomodoro Timer application built with Python and Tkinter.

---

### 📝 Tasks
- Set up the Pomodoro UI layout
- Implement countdown timer functionality
- Add Start and Reset button features
- Create work, short break, and long break sessions
- Implement timer repetition logic using `after()`
- Display session status dynamically (STUDY / BREAK)
- Add progress check marks (✓)
- Use Canvas to display the tomato image and timer text

---

## 🧠 Notes

### .after()
Executes a function after a specified amount of time.
```python
window.after(1000, function_name)
```
Example:
```python
timer = window.after(1000, count_down, count - 1)
```
- 1000 milliseconds = 1 second
- Commonly used for countdown timers and repeated events.
- Returns a timer ID that can be canceled later.

### after_cancel()
```python
window.after_cancel(timer)
```
- Useful for reset or pause functionality
- Requires the timer ID returned by `after()`

### Canvas
Used to draw graphics, text, and images.
```python
canvas = tk.Canvas(width=200, height=224)
canvas.create_text(100, 130, text="00:00")
```
- Supports custom positioning.
- Useful for building custom UI designs.