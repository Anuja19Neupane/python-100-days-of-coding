from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(). __init__()
        self.score = 0
        with open("day_20,21/data.txt") as data:
            self.high_score = int(data.read())
        # score lai kaha print garney vanera co_ordinateas deko
        self.goto(0, 265)
        # mandatory to change color kinaki black background xa so change coolor.
        self.color("white")
        self.penup()

        self.hideturtle()  # screen ma turtle nadekhaos vanera

    def update_scoreboard(self):
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center",
                   font=("arial", 24, "normal"))  # 24 size jastei ho

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.clear()
            with open("day_20,21/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()  # suruma score 0 hunxa , hamile clear use garinam vaney tyai mathi 1,2,3..... print hudeijanxa
        self.update_scoreboard()
