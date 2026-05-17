from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 1. Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
Y_WALL = 280
X_WALL = 360



# 2. Create a paddle
paddle_right = Paddle(350, 0)
# 3. Create another paddle
paddle_left = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

# move the paddles
key_bindings = {
    "Up": paddle_right.go_up,
    "Down": paddle_right.go_down,
    "w": paddle_left.go_up,
    "s": paddle_left.go_down
}

screen.listen()

for key, action in key_bindings.items():
    screen.onkeypress(action, key)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # 5. Detect collision with wall and bounce
    if ball.ycor() > Y_WALL or ball.ycor() < -Y_WALL:
        ball.bounce_y()

    # 7. Detect when paddle misses
    if ball.xcor() > X_WALL:
        score.increase_left_score()
        ball.reset_position()
    elif ball.xcor() < -X_WALL:
        score.increase_right_score()
        ball.reset_position()

    # 6. Detect collision with paddle
    # Right paddle collision
    if ball.distance(paddle_right) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    # Left paddle collision
    if ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # 8. Keep score

    if score.score_left >= 5 or score.score_right >= 5:
        score.game_over()
        game_is_on = False


screen.exitonclick()