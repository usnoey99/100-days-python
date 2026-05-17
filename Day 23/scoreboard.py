from turtle import Turtle
import time

FONT = ("Courier", 22, "normal")
FINISH_FONT = ("Courier", 65, "bold")
ALIGNMENT = "center"

# 7. Display level information and game over message
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(-210, 260)
        self.write(f"LEVEL: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FINISH_FONT)


    def full_level(self):
        self.color("yellow")
        self.goto(0, 80)
        self.write("ALL", align=ALIGNMENT, font=FINISH_FONT)

        self.goto(0, 0)
        self.write("LEVELS", align=ALIGNMENT, font=FINISH_FONT)

        self.goto(0, -80)
        self.write("COMPLETE", align=ALIGNMENT, font=FINISH_FONT)