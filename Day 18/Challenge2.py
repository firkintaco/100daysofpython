from turtle import Screen, Turtle

# Screen config
screen = Screen()
screen.title("Challenge2")

# Turtle config
karpo = Turtle()
karpo.shape("turtle")
karpo.color("hotpink1")

# Draw dashed line
def dashed_line():
    for _ in range(10):
        karpo.forward(10)
        karpo.penup()
        karpo.forward(10)
        karpo.pendown()

for _ in range(4):
    dashed_line()
    karpo.left(90)
    karpo.forward(50)
    karpo.left(90)
    dashed_line()
    karpo.right(90)
    karpo.forward(50)
    karpo.right(90)
karpo.write("Finished")
karpo.home()
# Exit on click
screen.exitonclick()