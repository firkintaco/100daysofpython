from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Configurin the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Day 22: Pong")

screen.tracer(0)

paddle = Paddle((350,0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


game_is_on = True
game_speed = 0.1
while game_is_on:
    if game_speed <= 0.01:
        game_speed = 0.1
    screen.update()
    ball.move()
    time.sleep(game_speed)

    # Detect collision with wall and bounce
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        game_speed -= 0.01

    # Detect when Right paddle misses
    if ball.xcor() > 380:
        print("Left player gets point")
        scoreboard.left_increase()
        scoreboard.update()
        ball.reset_position()
        game_speed = 0.1

    # Detect when Left paddle misses
    if ball.xcor() < -380:
        print("Right player gets the point")
        scoreboard.right_increase()
        scoreboard.update()
        ball.reset_position()
        game_speed = 0.1


screen.exitonclick()