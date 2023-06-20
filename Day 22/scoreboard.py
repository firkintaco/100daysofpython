from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Right: {self.score1}\nLeft: {self.score2}", align="center", font=("Courier", 24, "normal"))
    def left_increase(self):
        self.score1 += 1

    def right_increase(self):
        self.score2 += 1