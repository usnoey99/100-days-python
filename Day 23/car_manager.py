from turtle import Turtle
import random
CAR_SHAPE = ["red_car.gif", "green_car.gif", "blue_car.gif", "white_car.gif", "yellow_car.gif", "truck.gif", "bus.gif"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(random.choice(CAR_SHAPE))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-6, 6) * 40 + 20
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.shape() == "yellow_car.gif":
                car.backward(self.car_speed + 3)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT