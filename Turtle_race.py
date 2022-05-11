
import turtle
from turtle import Turtle,Screen
import random

# tim = Turtle()
# tim.shape("turtle")
# tim.color("Red")
#
# tim2 = Turtle()
# tim2.shape("turtle")
# tim2.color("Yellow")
#
# tim3 = Turtle()
# tim3.shape("turtle")
# tim3.color("pink")

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle wil;l win the race? Enter a color: ")

colors = ["red","Green","Blue","purple","yellow","orange"]
y = -125
x = -230
is_race_on = False
all_turtles = []

for i in range(6):
    tim_i = Turtle()
    tim_i.shape("turtle")
    tim_i.color(colors[i])
    tim_i.penup()
    tim_i.goto(x, y)
    y = y+50
    all_turtles.append(tim_i)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


# tim.penup()
# tim.goto(x = -230,y = 0)
# tim2.goto(x= -230, y = 50)
# tim3.goto(x = -230, y = -50)

screen.exitonclick()

