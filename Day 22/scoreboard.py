from turtle import Turtle
ALIGNMENT = "center"
BASIC_FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"{self.score_left}   :   {self.score_right}", align=ALIGNMENT, font=BASIC_FONT)

    def increase_left_score(self):
        self.score_left += 1
        self.clear()
        self.update_score_board()

    def increase_right_score(self):
        self.score_right += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 80, "normal"))
