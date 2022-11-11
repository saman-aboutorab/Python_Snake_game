from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.write(f"SCORE: {self.score}", False, 'center', font=('Courier', 8, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", False, 'center', font=('Courier', 8, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, 'center', font=('Courier', 16, 'normal'))