from turtle import Turtle
ALIGNMENT = "center"
BASIC_FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score_board()


    def update_score_board(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=BASIC_FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score_board()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 20, "normal"))
