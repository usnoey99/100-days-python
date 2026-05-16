import random
from turtle import Turtle
# 4-1. Create the ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shape("square")
        self.x_move = random.choice([5, -5])
        self.y_move = random.choice([5, -5])
        self.move_speed = 0.08

    # 4-2 make the ball move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    # 5. Detect collision with wall and bounce
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7
        if self.move_speed < 0.03:
            self.move_speed = 0.03

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()