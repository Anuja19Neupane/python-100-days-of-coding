from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# 'width' and 'height' lekhna compulsory haina value matra lekhda hunxa tara chinna ko lagi lekheko maile
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="make your bet", prompt="which turtle will win the race?  orange, yellow, green, blue, purple, red?:  ")
print(f"you choose: {user_bet}")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):  # position:0,1,2,3,4,5
    giby = Turtle(shape="turtle")
    giby.color(colors[turtle_index])
    giby.penup()
    giby.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(giby)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"you won! the {winning_color} turtle is the winner. ")
            else:
                print(
                    f"you lost! the {winning_color} turtle is the winner. ")
        rand_distance = random.randint(0, 10)  # 0 dekhi 10
        turtle.forward(rand_distance)


screen.exitonclick()
