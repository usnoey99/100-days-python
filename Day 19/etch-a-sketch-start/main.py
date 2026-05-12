from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

'''
W = Forwards
S = Backwards
A = Counter-Clockwise
D = Clockwise
C = Clear drawing
'''

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_counter_clockwise():
    angle = tim.heading()
    tim.setheading(angle+5)
def move_clockwise():
    angle = tim.heading()
    tim.setheading(angle-5)
def clear_drawing():
    tim.clear()

screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards,"s")
screen.onkeypress(move_counter_clockwise, "a")
screen.onkeypress(move_clockwise, "d")
screen.onkeypress(clear_drawing, "c")
screen.exitonclick()
