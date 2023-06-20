from turtle import Turtle, Screen
import random
# Screen conf
screen = Screen()
screen.title("Day 19: Turtle Race")
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []
# Turtles
for turtle_index in range(0,6):
    karpo = Turtle(shape="turtle")
    karpo.penup()
    karpo.color(colors[turtle_index])
    karpo.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(karpo)


is_race_on = False
winner = None
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winner = turtle.pencolor()
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} is the winner!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()