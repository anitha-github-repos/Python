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
        self.head = self.squares[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)
        #for i in range(3):

        # for i in range(3):
        #     self.squares[i].goto(self.x, self.y)
        #     self.x = self.x+20

    def add_segment(self,position):
        tim_i = Turtle("square")
        tim_i.color("white")
        tim_i.penup()
        tim_i.goto(position)
        self.squares.append(tim_i)

    def reset(self):
        for seg in self.squares:
            seg.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def extend(self):
        self.add_segment(self.squares[-1].position())

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



