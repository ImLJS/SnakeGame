from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


class Snake:
    def __init__(self):
        self.x_position = 0
        self.all_turtle = []
        self.head = self.all_turtle[0]
        self.create_snake()

    def create_snake(self):
        for turtle in range(3):
            tim = Turtle(shape='square')
            tim.color('white')
            tim.pu()
            tim.goto(self.x_position, 0)
            self.x_position -= 20
            self.all_turtle.append(tim)

    def move(self):
        screen.update()
        time.sleep(0.1)
        for turtle in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[turtle - 1].xcor()
            new_y = self.all_turtle[turtle - 1].ycor()
            self.all_turtle[turtle].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)