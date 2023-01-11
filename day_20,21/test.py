from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background_color
screen.title("My snake game")

# square overlap nahos vanera co-ordinatesmention nagareko
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    # 3 ota square jodera snake jasto banauna khojeko
    new_segment = Turtle("square")
    new_segment.color = ("white")
    new_segment.goto(position)


screen.exitonclick()
