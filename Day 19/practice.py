from turtle import Turtle, Screen

tut = Turtle()
screen = Screen()

def move_forwards():
    tut.forward(10)

screen.listen() # This function starts listening for keyboard input.

screen.onkey(fun=move_forwards, key="space")
# screnn.onkey(funktion_name, "key"): used to handle keyboard events.

screen.exitonclick()