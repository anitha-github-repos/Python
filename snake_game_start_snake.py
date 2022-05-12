from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        #self.x = -50
        #self.y = 0
        self.create_snake()

    def create_snake(self):
        for positions in STARTING_POSITIONS:
        #for i in range(3):
            tim_i = Turtle("square")
            tim_i.color("white")
            tim_i.penup()
            tim_i.goto(positions)
            self.squares.append(tim_i)
        # for i in range(3):
        #     self.squares[i].goto(self.x, self.y)
        #     self.x = self.x+20

    def move(self):
        for sq in range(len(self.squares) - 1, 0, -1):
            new_xcor = self.squares[sq - 1].xcor()
            new_ycor = self.squares[sq - 1].ycor()
            self.squares[sq].goto(new_xcor, new_ycor)
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)



