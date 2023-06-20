from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()

        self.color("white")
        self.penup()
        self.shape("square")
        self.turtlesize(5, 1)
        self.goto(pos)

    def up(self):
        position_y = self.ycor()
        new_position = position_y + 20
        self.goto(self.xcor(), new_position)

    def down(self):
        new_position = self.ycor() -20
        self.goto(self.xcor(), new_position)