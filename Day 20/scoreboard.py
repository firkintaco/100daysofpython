from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_from_file()
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
        self.write(f"Score: {self.score} | High score: {self.high_score}",align="center", font=("Courier", 22, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_to_file()
        self.score = 0
        self.show_text()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!",align="center", font=("Courier", 24, "normal"))

    def write_to_file(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def load_from_file(self):
        with open("highscore.txt") as file:
            self.high_score = int(file.read())