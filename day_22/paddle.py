from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):  # method always has first attribute as self.
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # remember square 20-20 pixel ko hunxa.
        self.penup()  # paddle center ma xa so teslai side ma lana ko lagi nakoriyos vanera
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
