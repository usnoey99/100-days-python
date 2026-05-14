from turtle import Screen
from obstacle import Obstacle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# -----------------------
# Screen setup
# -----------------------
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0) # 0 → Turns off automatic updates.
WALL = 295
game_speed = 0.2

snake = Snake()
food = Food()
score_board = Scoreboard()
obstacle = Obstacle()





answer = screen.textinput("Snake Game", "Type 'y' or 'n'")
if answer == 'y':
    game_is_on = True
else:
    game_is_on = False

screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")


# -----------------------
# Main game loop
# -----------------------
while game_is_on:
    screen.update()  # manually update screen
    time.sleep(game_speed)  # control the speed

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 10:
        food.refresh()
        score_board.increase_scoreboard()
        snake.extend()
        # like level system
        game_speed = max(0.05, game_speed * 0.95)

        if score_board.score % 5 == 0:
            obstacle.add_block(food, snake.segments)

        obstacle.refresh_all(food, snake.segments)


    # Detect collision with tail.
    # IF head collision with any segment in the tail:
    for seg in snake.segments[1:]: # python slicing
        if snake.head.distance(seg) < 5:
            # trigger game_over
            game_is_on = False
            score_board.game_over()

    # Detect collision with obstacles.
    for block in obstacle.blocks: # python slicing
        if snake.head.distance(block) < 5:
            # trigger game_over
            game_is_on = False
            score_board.game_over()


    # Detect collision with wall.
    if snake.head.xcor() > WALL or snake.head.xcor() < -WALL or snake.head.ycor() > WALL or snake.head.ycor() < -WALL:
        game_is_on = False
        score_board.game_over()





screen.exitonclick()