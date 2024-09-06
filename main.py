from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My  snake Game")
screen.tracer(0)

# create a snake
snake = Snake()
score = Score()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
# move the snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.count()
        snake.extend()

    pos_x = snake.head.xcor()
    pos_y = snake.head.ycor()
    if pos_x < -290 or pos_x > 290 or pos_y < -290 or pos_y > 290:
        score.reset()
        snake.reset()

    # detect collision with tail

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            score.reset()


screen.exitonclick()