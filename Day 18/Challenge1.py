from turtle import Turtle, Screen

# Screen config
screen = Screen()
screen.title("Neliö")

# Turtle config
karpo = Turtle()
karpo.shape("turtle")

for i in range(4):
    karpo.forward(100)
    karpo.left(90)

screen.exitonclick()