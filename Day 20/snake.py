from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    segments = []
    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates 3 squares"""
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.segments.append(new_part)

    def extend(self):
        """Extends snake """
        self.add_segment(self.segments[-1].position())
    def move(self):
        """Moves snake forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_y = self.segments[seg_num - 1].ycor()
            new_x = self.segments[seg_num - 1].xcor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Turn's snake direction to up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn's snake direction to down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        """Turn's snake direction to left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn's snake direction to right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)