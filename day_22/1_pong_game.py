from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
# paddle le center bata side samma aako nadeki padle surumei side ma aaos vanera
screen.tracer(0)

r_paddle = Paddle((350, 0))  # paddle ko lagi co-ordinates deko
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()  # listen vaneko yo command follow garxa
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # tracer use gareyapxi update garna is compulsory.
    ball.move()

    # detect collision with wall

    # screen ko y co-ordinates 600 xa s0 half is 300 ani tyo vanda thorei kam linu parxa
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    # detect r_paddle missies
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

      # detect l_paddle missies
    if ball.xcor() < -380: 
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
