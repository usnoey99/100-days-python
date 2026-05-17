import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#505050")
screen.tracer(0)

# Extend Version
screen.register_shape("blue_car.gif")
screen.register_shape("red_car.gif")
screen.register_shape("green_car.gif")
screen.register_shape("white_car.gif")
screen.register_shape("yellow_car.gif")
screen.register_shape("truck.gif")
screen.register_shape("bus.gif")

screen.register_shape("player_turtle.gif")


# draw road
def draw_road():
    road = Turtle()
    road.hideturtle()
    road.penup()
    road.color("white")
    road.pensize(2)

    for y in range(-240, 241, 40):
        road.goto(-300, y)
        for _ in range(15):
            road.pendown()
            road.forward(20)
            road.penup()
            road.forward(20)

draw_road()

# 1. Create a turtle object
player_turtle = Player()

# 2. Generate multiple cars dynamically
car_manager = CarManager()

score = Scoreboard()

screen.listen()
screen.onkey(player_turtle.move, "Up")
screen.onkey(player_turtle.move_left, "Left")
screen.onkey(player_turtle.move_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()

    # 3. Move cars across the screen
    car_manager.move_cars()

    # 4. Detect collisions with cars
    for car in car_manager.all_cars:
        if player_turtle.distance(car) < 25:
            score.game_over()
            game_is_on = False

    # 5. Detect when the player reaches the finish line
    if player_turtle.ycor() >= FINISH_LINE_Y:
        score.increase_level()
        player_turtle.level_up()
        # 6. Increase car speed after each level
        car_manager.speed_up()

    if score.level == 7:
        score.full_level()
        game_is_on = False


screen.exitonclick()