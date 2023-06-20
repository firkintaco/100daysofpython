from turtle import Screen
from time import sleep
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player


screen = Screen()
screen.title("Day 23")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.register_shape("turtle.gif")
screen.register_shape("pizza.gif")


scoreboard = Scoreboard()
player = Player()
car = CarManager()
screen.listen()
screen.onkey(player.move, "Up")


game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    car.add_car()
    car.move_cars()

    # Detect collision with car
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 30:
            game_on = False
            scoreboard.game_over()
            screen.exitonclick()

    # Detect succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_score()

