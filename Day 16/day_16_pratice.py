# docs.python.org/3/library/turtle.html

import turtle
# or from turtle import Turtle

timmy = turtle.Turtle() # timmy = Turtle()
print(turtle) # <module 'turtle' from 'C:\\Python\\Lib\\turtle.py'>
# actually an object printed
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100) # Move the turtle forward by 100 paces

my_screen = turtle.Screen()
print(my_screen.canvheight) # 300
my_screen.exitonclick() # allow to continue running until we click on the screen and then it exits the code

from prettytable import PrettyTable

table = PrettyTable() # Create new Constructor

table.add_column("City", ["Berlin","Paris","Seoul","Madrid"])
table.add_column("Country", ["Germany","France","Korea","Spain"])
table.align = "r"
print(table)
