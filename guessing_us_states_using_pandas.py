import turtle
#import csv(alternative with pandas, code in commented)
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


##getting screen coordinates at a mouse click location in a turle
#
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 States Correct",
                                    prompt="What's another state's name?")
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state.title() in all_states:
        guessed_states.append(answer_state.title())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state.title()]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state.title(), align='center', font=("Arial", 8, "normal"))


# while game_is_on:
#     screen.update()
#     answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#     with open("50_states.csv") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if row[0] != "state":
#                 if row[0].lower() == answer_state.lower():
#                     t = turtle.Turtle()
#                     t.hideturtle()
#                     t.penup()
#                     x = int(row[1])
#                     y = int(row[2])
#                     state = row[0]
#                     t.goto(x, y)
#                     t.write(state, align='center', font=("Arial", 8, "normal"))

#screen.exitonclick()