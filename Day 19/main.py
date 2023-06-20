from turtle import Turtle, Screen

# Screen conf
screen = Screen()
screen.title("Day 19")

# Turtle conf
karpo = Turtle()
karpo.shape("turtle")
karpo.pencolor("hotpink1")
def move_forward():
    karpo.forward(30)

def turn_right():
    karpo.right(25)

def turn_left():
    karpo.left(25)

def move_back():
    karpo.back(30)

screen.listen()
screen.onkey(key="c", fun=karpo.clear)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)


screen.exitonclick()