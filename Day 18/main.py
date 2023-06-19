from turtle import Turtle, Screen, colormode
from random import choice

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
screen = Screen()
screen.title("Karpolla maalaa")
karpo = Turtle()
karpo.shape("turtle")
karpo.pensize(30)
colormode(255)
karpo.speed("fastest")
karpo.hideturtle()


def draw_line():
    for i in range(10):
        karpo.color(choice(colors))
        karpo.pendown()
        # karpo.forward(1)
        karpo.dot(30, choice(colors))
        karpo.penup()
        karpo.forward(50)
        karpo.penup()


for _ in range(10):
    draw_line()
    # karpo.setheading(90)
    # karpo.forward(50)
    karpo.setheading(0)
    karpo.sety(round(karpo.ycor(), 1)+50)
    karpo.setx(0)

karpo.home()
karpo.setheading(270)
karpo.fd(100)

karpo.pencolor(choice(colors))
karpo.write("Maalasin juuri tämän!", font=('Segoe UI', 32, 'normal'))
karpo.setheading(0)
karpo.pencolor(choice(colors))
karpo.pendown()
karpo.pensize(10)
karpo.forward(430)
karpo.dot(50, choice(colors))



screen.exitonclick()
