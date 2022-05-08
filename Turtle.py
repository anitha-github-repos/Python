
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle,Screen

screen = Screen()
timmy = Turtle()
turtle.colormode(255)
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
timmy.goto(0,0)
y = 0
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
#screen.screensize(2000,1500)
turtle.speed(10)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
        timmy.pendown()
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

        if dot_count % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

screen.exitonclick()