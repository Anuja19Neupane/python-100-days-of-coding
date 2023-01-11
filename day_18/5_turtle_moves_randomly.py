from turtle import Turtle, Screen
import random

giby = Turtle()
colors = ["red", "green", "black", "blue"]
directions = [0, 90, 180, 2700]  # it's like choosing east west north south
giby.pensize(15)  # yesle tyo koreko line lai thik banauxa
giby.speed("fastest")


for _ in range(20):  # 20 palta randomly direction choose gardei move garxa
    giby.color(random.choice(colors))
    giby.forward(30)
    giby.setheading(random.choice(directions))
    # setheading le turtle ko orientation set garxa to the angle
