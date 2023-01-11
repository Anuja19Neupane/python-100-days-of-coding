

from turtle import Turtle, Screen

giby = Turtle()
screen = Screen()


def move_forward():
    giby.forward(10)


def move_backward():
    giby.backward(10)


def turn_left():
    new_heading = giby.heading()+10
    giby.setheading(new_heading)


def turn_right():
    new_heading = giby.heading()-10
    giby.setheading(new_heading)


def clear():
    giby.clear()  # aafule koreko sabei drawing erase garxa
    giby.penup()  # penup garda movement hunxa tara koreko dekhaudaina
    giby.home()  # feri aafno thau maback aauxa
    giby.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen = Screen()
screen.exitonclick()
