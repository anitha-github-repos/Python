from turtle import Turtle, Screen
import time
from Snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
# screen.onkey(snake.up,"U")
# screen.onkey(snake.down,"D")
# screen.onkey(snake.left,"L")
# screen.onkey(snake.right,"R")
game_is_on = True

while game_is_on:
    screen.update()
    screen.onkey(snake.up, "U")
    screen.onkey(snake.down, "D")
    screen.onkey(snake.left, "L")
    screen.onkey(snake.right, "R")
    time.sleep(0.1)
    snake.move()
    # if sq.xcor() > 280:
    #     screen.update()
    #     game_is_on = False
    # for sq in squares:
    #     #sq.penup()
    #     sq.forward(50)
    #     if sq.xcor() > 280:
    #         screen.update()
    #         game_is_on = False




screen.exitonclick()