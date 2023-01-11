from turtle import Turtle, Screen
import random

giby = Turtle()
colors = ["red", "green", "black", "blue"]
directions = [0, 90, 180, 2700]  # it's like choosing east west north south
# giby.pensize(15)  # yesle tyo koreko line lai thik banauxa
giby.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        giby.color(random.choice(colors))
        giby.circle(100)  # yo 100 chai radius ho
        giby.setheading(giby.heading() + size_of_gap)


draw_spirograph(5)  # yo 5 chai size of gap ho

screen = Screen()
screen.exitonclick()
