from turtle import Screen, Turtle
from snake import Snake
import time

# -----------------------
# Screen setup
# -----------------------
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0) # 0 → Turns off automatic updates.

snake = Snake()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")



# -----------------------
# Main game loop
# -----------------------
game_is_on = True
while game_is_on:
    screen.update()  # manually update screen
    time.sleep(0.1)  # control the speed

    snake.move()



screen.exitonclick()