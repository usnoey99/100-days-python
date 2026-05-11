###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
# rgb_colours = []
# Print out a list of all the colours extracted from the image
# and each item in the list to be a tuple that you create
# colours = colorgram.extract('image.jpg', 30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_colours.append((r,g,b))
# print(rgb_colours)

from turtle import Turtle, Screen
import random

colours_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# setting
dot_painter = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
dot_painter.penup()
dot_painter.hideturtle()
dot_painter.speed("fastest")
dot_painter.goto(-300,-250) # starting point, left bottom

def painting():
    dot_painter.penup()
    dot_painter.forward(55)
    dot_painter.pendown()
    for _ in range(10):
        dot_painter.dot(20, random.choice(colours_list))
        dot_painter.penup()
        dot_painter.forward(55)

def turn_left():
    dot_painter.left(90)
    dot_painter.penup()
    dot_painter.forward(55)
    dot_painter.left(90)

def turn_right():
    dot_painter.right(90)
    dot_painter.penup()
    dot_painter.forward(55)
    dot_painter.right(90)

for i in range(10):
    if i % 2 == 0:
        painting()
        turn_left()
    else:
        painting()
        turn_right()

screen.exitonclick()

