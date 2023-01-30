from turtle import Turtle
ALIGN = "center"
FONT = ('Ariel', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0,200)
        self.color('white')
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}",align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(" Game Over ", align=ALIGN, font=FONT)

