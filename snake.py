from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


class Snake:
    def __init__(self):
        self.x_position = 0
        self.all_turtle = []
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

        self.all_turtle[0].forward(20)

    def up(self):
        self.all_turtle[0].setheading(90)

    def down(self):
        self.all_turtle[0].setheading(270)

    def left(self):
        self.all_turtle[0].setheading(180)

    def right(self):
        self.all_turtle[0].setheading(0)