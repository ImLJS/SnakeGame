from turtle import Screen
from snake import Snake

screen = Screen()
snake = Snake()

is_game_on = False
game = False

if snake:
    is_game_on = True

if is_game_on:
    game = True

while game:
    snake.move()
    if snake.all_turtle[0].xcor() >= 245:
        game = False

screen.exitonclick()
