from turtle import Turtle, Screen
import time
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True

while game_is_on:
    screen.update()
    # screen.onkey(snake.up, "Up")
    # screen.onkey(snake.down, "Down")
    # screen.onkey(snake.left, "Left")
    # screen.onkey(snake.right, "Right")
    time.sleep(0.1)
    snake.move()
    if snake.squares[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        #game_is_on = False
        #scoreboard.game_over()
    for segment in snake.squares[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            #game_is_on = False
            #scoreboard.game_over()


screen.exitonclick()