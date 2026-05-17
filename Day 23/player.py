from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# 1. Create a turtle object
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("player_turtle.gif")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def level_up(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)