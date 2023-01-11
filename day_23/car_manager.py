from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # 1 dekhi  6 samma euta number pick garxa
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # car dherai ota aayoso kam garna ko lagi yo gareko
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=2, stretch_len=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # -300 ra +300 kina nagareko vaney turtle uvvina ra last ma pugda feri pani space chainxa.
            random_y = random.randint(-250, 250)

            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # ek palta cross vaisakeypaxi car ko speed badauna
        self.car_speed += MOVE_INCREMENT
