from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
snake = Snake()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

food = Food()
score = Score()

is_game_on = False
game = False

if snake:
    is_game_on = True

if is_game_on:
    game = True

while game:
    snake.move()
    if snake.head.distance(food) < 15:
        food.create_food()
        score.score += 1
        score.update_score()

    if snake.all_turtle[0].xcor() >= 245 or snake.all_turtle[0].ycor() >= 245 or snake.all_turtle[0].xcor() <= -245 or \
            snake.all_turtle[0].ycor() <= -245:
        game = False
        score.game_over()


screen.exitonclick()
