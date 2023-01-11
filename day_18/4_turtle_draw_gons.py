from turtle import Turtle, Screen
import random

giby = Turtle()
giby.shape("turtle")
giby.color("green")

colors = ["red", "green", "black", "blue"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        giby.forward(100)
        giby.right(angle)


# (3,8)garyo vaney 7 samma matra hunxa ie.heptagon.
for shape_side in range(3, 8):
    giby.color(random.choice(colors))
    draw_shape(shape_side)
screen = Screen()
screen.exitonclick()
