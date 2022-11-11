from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score
from wall import Wall
import random


def change_background():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    background_color = (r, g, b)
    screen.bgcolor(background_color)



SPEED = 0.15

screen = Screen()
screen.colormode(255)
screen.setup(600, 600)
change_background()
screen.tracer(0)



snake = Snake()
food = Food()
score = Score()
wall = Wall()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True

while game_on:
    time.sleep(SPEED)
    screen.update()
    snake.move()

    # When snake eats the food
    if snake.head.distance(food) < 10:
        food.change_color()
        food.change_location()
        change_background()
        snake.add()
        SPEED -= 0.01
        score.add_score()
        wall.create_walls()

    # When the snake hit its tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            screen.bgcolor('grey')
            score.game_over()

    # When the snake hit a wall
    for piece in wall.walls_list:
        if snake.head.distance(piece) < 10:
            game_on = False
            screen.bgcolor('grey')
            score.game_over()

screen.exitonclick()