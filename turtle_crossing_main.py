from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_generate()
    car_manager.move_cars()
    # detect turtle collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.game_reset()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()