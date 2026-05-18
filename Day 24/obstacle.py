from turtle import Turtle
import random

class Obstacle(Turtle):
    def __init__(self, count=1):
        self.blocks = []

    def add_block(self, food, snake_segments):
        if len(self.blocks) >= 7:
            return

        block = Turtle("triangle")
        block.penup()
        block.color("green")
        block.shapesize(0.9, 0.9)
        block.speed("fastest")

        self.blocks.append(block)

        self.refresh_all(food, snake_segments)


    def get_safe_position(self, food, snake_segments):
        while True:
            x = random.randint(-14, 14) * 20
            y = random.randint(-14, 14) * 20

            if food.distance((x, y)) < 20:
                continue

            collision = False
            for seg in snake_segments:
                if seg.distance((x, y)) < 20:
                    collision = True
                    break

            if not collision:
                return x, y

    def refresh_all(self, food, snake_segments):
        for block in self.blocks:
            x, y = self.get_safe_position(food, snake_segments)
            block.goto(x, y)