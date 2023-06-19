import turtle
import random
karpo = turtle.Turtle()
karpo.shape("turtle")

screen = turtle.Screen()
screen.title("Spirograph (mikä?)")
screen.bgcolor("black")
karpo.speed("fastest")
turtle.colormode(255)
karpo.pensize(3)

def random_color():
    color = color = (random.randint(1,250),random.randint(1,250),random.randint(1,250))
    return color

for angle in range(360):
    if angle % 5 == 0:
        karpo.setheading(angle)
        karpo.color(random_color())
        karpo.circle(200)

karpo.penup()
karpo.right(50)
karpo.color("white")
karpo.forward(500)
karpo.write("I'm boss here", font=('Arial', 32, 'normal'))

screen.exitonclick()