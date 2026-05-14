# -----------------------
# Snake setup
# -----------------------

from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)] # starting 3 segments
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    # -----------------------
    # Snake creat
    # -----------------------
    def creat_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        if len(self.segments) == 0:
            segment.color("yellow")
        else:
            segment.color("white")

        segment.penup()  # don't draw lines when moving
        segment.goto(position)
        self.segments.append(segment)

    # -----------------------
    # Snake extend
    # -----------------------
    def extend(self):
        self.add_segment(self.segments[-1].position())
        # self.segments[-1].position() == (-40, 0)


    # -----------------------
    # Snake movement
    # -----------------------
    def move(self):
        # move segments from tail to head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)