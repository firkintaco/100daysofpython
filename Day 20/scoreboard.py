from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.show_text()

    def increase(self):
        self.score += 1
        self.show_text()

    def show_text(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center", font=("Courier", 24, "normal"))