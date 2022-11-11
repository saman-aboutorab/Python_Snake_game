from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT_TOP_EDGE = 300
LEFT_DOWN_EDGE = -300
color = 'white'

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.snake_color = color

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def check_edge(self,head):
        if head.xcor() >= RIGHT_TOP_EDGE:
            transported_x = (head.xcor() - RIGHT_TOP_EDGE) + LEFT_DOWN_EDGE
            head.goto(transported_x, head.ycor())
        elif head.xcor() <= LEFT_DOWN_EDGE:
            transported_x = (head.xcor() - LEFT_DOWN_EDGE) + RIGHT_TOP_EDGE
            head.goto(transported_x, head.ycor())
        if head.ycor() >= RIGHT_TOP_EDGE:
            transported_y = (head.ycor() - RIGHT_TOP_EDGE) + LEFT_DOWN_EDGE
            head.goto(head.xcor(), transported_y)
        elif head.ycor() <= LEFT_DOWN_EDGE:
            transported_y = (head.ycor() - LEFT_DOWN_EDGE) + RIGHT_TOP_EDGE
            head.goto(head.xcor(), transported_y)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color(color)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.check_edge(self.head)
        self.head.forward(MOVE_DISTANCE)

    def add(self):
        last_seg_x = self.segments[len(self.segments) - 1].xcor()
        last_seg_y = self.segments[len(self.segments) - 1].ycor()
        last_seg_heading = self.segments[len(self.segments) - 1].heading()
        new_segment = Turtle("square")
        new_segment.color(color)
        new_segment.penup()

        if last_seg_heading == 0:
            new_segment.goto(last_seg_x - 20, last_seg_y)
        elif last_seg_heading == 90:
            new_segment.goto(last_seg_x, last_seg_y - 20)
        elif last_seg_heading == 180:
            new_segment.goto(last_seg_x + 20, last_seg_y)
        elif last_seg_heading == 270:
            new_segment.goto(last_seg_x, last_seg_y + 20)

        self.segments.append(new_segment)

