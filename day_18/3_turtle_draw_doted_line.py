
from turtle import Turtle, Screen

giby = Turtle()
giby.shape("turtle")
giby.color("green")

for _ in range(15):
    giby.forward(10)
    giby.penup()
    giby.forward(10)
    giby.pendown()

screen = Screen()
screen.exitonclick()
