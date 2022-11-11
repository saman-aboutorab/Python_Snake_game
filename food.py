from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.change_color()
        self.penup()
        self.speed('fastest')
        self.change_location()

    def change_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        FOOD_COLOR = (r, g, b)
        self.color(FOOD_COLOR)

    def change_location(self):
        random_x = 20 * random.randint(-12, 12)
        random_y = 20 * random.randint(-12, 12)
        self.goto(random_x, random_y)