import random
from turtle import Turtle, Screen
# If only using it once or twice then just import the whole module and write out this turtle.Turtle
# so that you can see that this module is the one that contains this class and that is imported
# and we're using it to create this object.

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("red")


# Draw a square
for _ in range(4):
    tim.forward(100)
    tim.right(90) # right(angle): 90 grad

tim.left(90) # left(angle): 90 grad


# Draw a Dashed Line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

tim.left(90)


# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for sides in range(3,11): # triangle to decagon
    angle = 360/ sides
    tim.pencolor(random_color())
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


# Draw a Random Walk
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


# Make a Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)): # only integer for range
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(4)

screen.exitonclick()