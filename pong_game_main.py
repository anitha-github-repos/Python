from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.listen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


# tim = Turtle()
# tim.color("white")
# tim.shape("square")
# tim.shapesize(stretch_wid=5,stretch_len=1 )
# tim.penup()
# tim.goto(x=350,y=0)
#
#
#
# def move_up():
#     new_y = tim.ycor()+20
#     tim.goto(tim.xcor(), new_y)
#
#
# def move_down():
#     new_y = tim.ycor() - 20
#     tim.goto(tim.xcor(), new_y)


screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()