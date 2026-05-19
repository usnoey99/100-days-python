import turtle
import pandas
from pandas.core.ops import missing

BACKGROUND = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725,height=500)
screen.addshape(BACKGROUND)
turtle.shape(BACKGROUND)

data_set = pandas.read_csv("50_states.csv")
all_states = data_set.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data_set[data_set.state == answer_state]
        t.goto(int(state_data.x.values[0]), int(state_data.y.values[0]))
        t.write(answer_state)



screen.exitonclick()