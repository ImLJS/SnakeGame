from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.color('white')
        self.write(f"Scoreboard : {self.score}", align="center", font=('Ariel', 24, 'normal'))