## Day 22 - Pong Game Project

---

### 📌 Project Overview

Building the classic **Pong Game** using the turtle module.

The goal is to recreate the original arcade-style Pong game with:
- Two paddles
- A moving ball
- Collision detection
- Scoring system

---

### 🛠️ Features

- Player-controlled paddles (left & right)
- Ball movement with bouncing physics
- Collision detection with walls and paddles
- Score tracking system
- Game loop with real-time updates
- Increase ball speed over time

---

### 📝 Tasks

1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score

---

## 🎮 Controls

- Right Paddle: `Up` / `Down`
- Left Paddle: `W` / `S`

---

## 🧠 Notes

- Built using `turtle.Screen.tracer(0)` for smooth animation
- Game loop uses `time.sleep()` for frame control
- Collision detection based on distance and coordinate checks