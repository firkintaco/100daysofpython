FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.penup()
        self.goto(-250, 240)
        self.draw()

    def increase_score(self):
        self.score += 1
        self.draw()
    def draw(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", font=FONT, align="center")