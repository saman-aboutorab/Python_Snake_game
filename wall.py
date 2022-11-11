import random
from turtle import Turtle


class Wall:

    def __init__(self):
        self.walls_list = []
        self.create_walls()

    def create_walls(self):

        random_x = 20 * random.randint(-12, 12)
        random_y = 20 * random.randint(-12, 12)
        x_or_y = random.randint(0,1)
        for distance in range(3):
            new_wall = Turtle()
            new_wall.shape('square')
            new_wall.color('black')
            new_wall.penup()
            if x_or_y == 0:
                new_wall.goto(random_x + distance * 20, random_y)
            elif x_or_y == 1:
                new_wall.goto(random_x, random_y + distance * 20)

            self.walls_list.append(new_wall)


