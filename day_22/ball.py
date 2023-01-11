from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # score badhdei jada  ball ko speed badhdei jaos vanera

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # suruma mathi thokyo vaney aba bounce vayepaxi tala aauxa so multiply by -1 and viceversa.
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.99

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # ball feri reset vayepaxi ta speed noram hunu paryo ni ta
        self.bounce_x()
