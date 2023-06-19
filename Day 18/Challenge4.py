from turtle import Turtle, Screen, colormode
import random

# Screen conf
screen = Screen()
screen.title("Random walk")

# Colors list
# colours = ["MediumPurple", "PaleGreen3", "tomato", "red", "SkyBlue", "violet", "goldenrod2", "DodgerBlue","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

karpo = Turtle()
karpo.pensize(20)
karpo.speed("fastest")
colormode(255)
karpo.shape("turtle")

def random_color():
    color = color = (random.randint(1,250),random.randint(1,250),random.randint(1,250))
    return color


for _ in range(200):
    karpo.pencolor(random_color())
    karpo.forward(50)
    karpo.setheading(random.choice(directions))

karpo.write("Finished!!")
screen.exitonclick()