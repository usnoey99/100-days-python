from turtle import Turtle, Screen
import random
from tkinter import messagebox


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
is_over = False

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []
winner = ""
winner_colour = ""

def check_bet():
    if winner_colour == user_bet:
        messagebox.showinfo("Race Result", f"You've won! The >>{winner_colour}<< turtle is the winner 🐢")
    else:
        messagebox.showinfo("Race Result", f"You've lost! The >>{winner_colour}<< turtle is the winner 🐢")

    newRace = screen.textinput(title="New Race", prompt="Do you want to place another bet?\nType y or n: ")

    return  newRace

def reset_game():
    for turtle in turtles:
        turtle.hideturtle()
    turtles.clear()

while not is_over:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\n"
                                                              "Enter a colour (red/orange/yellow/green/blue/purple): ")

    for i in range(len(colours)):
        t = Turtle()
        t.shape("turtle")
        t.color(colours[i])
        t.penup()
        t.goto(x=-230, y=y_positions[i])

        turtles.append(t)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            random_speed = random.randint(0,10)
            turtle.forward(random_speed)

            if turtle.xcor() > 230:
                winner = turtle
                winner_colour = turtle.pencolor()
                is_race_on = False


    newRace = check_bet()

    if newRace == "n":
        is_over = True

    reset_game()

screen.exitonclick()