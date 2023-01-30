from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(0.5,0.5)
        self.pu()
        self.speed('fastest')
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(random_x, random_y)
