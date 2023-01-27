from turtle import Screen
from snake import Snake

screen = Screen()
snake = Snake()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

is_game_on = False
game = False

if snake:
    is_game_on = True

if is_game_on:
    game = True

while game:
    snake.move()
    if snake.all_turtle[0].xcor() >= 245 or snake.all_turtle[0].xcor() <= -245:
        game = False
    if snake.all_turtle[0].ycor() >= 245 or snake.all_turtle[0].ycor() <= -245:
        game = False

screen.exitonclick()
