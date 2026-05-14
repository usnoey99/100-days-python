from turtle import Turtle
ALIGNMENT = "center"
BASIC_FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score_board()


    def update_score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=BASIC_FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 20, "normal"))
