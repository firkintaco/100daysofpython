from turtle import Screen, Turtle
from random import choice
# Colors
colors = ["MediumPurple", "PaleGreen3", "tomato", "red", "SkyBlue", "violet", "goldenrod2", "DodgerBlue"]
# Screen config
screen = Screen()
screen.title("Muotoja")
screen.screensize(canvwidth=100, canvheight=100, bg="black")

# Turtle Config
karpo = Turtle()
karpo.width(5)

# Draw shape
def draw_shape(sides, forward):
    angle = 360/sides
    for _ in range(sides):
        karpo.forward(forward)
        karpo.right(angle)
def triangle():
    karpo.color(choice(colors))
    for _ in range(3):
        karpo.forward(100)
        karpo.left(120)


def square():
    karpo.color(choice(colors))
    for _ in range(4):
        karpo.forward(100)
        karpo.left(90)


def pentagon():
    karpo.color(choice(colors))
    for _ in range(5):
        karpo.forward(100)
        karpo.left(72)


def hexagon():
    karpo.color(choice(colors))
    for _ in range(6):
        karpo.forward(100)
        karpo.left(60)


def heptagon():
    karpo.color(choice(colors))
    for _ in range(7):
        karpo.forward(100)
        karpo.left(51.42)


def octagon():
    karpo.color(choice(colors))
    for _ in range(8):
        karpo.forward(100)
        karpo.left(45)


def polygon():
    karpo.color(choice(colors))
    for _ in range(9):
        karpo.forward(100)
        karpo.left(40)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
polygon()

for i in range(3, 11):
    karpo.color(choice(colors))
    draw_shape(i, 100)



screen.exitonclick()