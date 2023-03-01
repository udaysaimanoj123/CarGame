COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import time
import random
from turtle import Turtle
from scoreboard import Scoreboard
score=Scoreboard()

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        if random.randint(1,6)==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            randy=random.randint(-250,250)
            new_car.goto(300,randy)
            self.all_cars.append(new_car)

    def create_car(self):
        for i in range(2*(score.level)+1):
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            randy=random.randint(-250,250)
            new_car.goto(300,randy)
            self.all_cars.append(new_car)

    def move_cars(self):
        for i in self.all_cars:
            i.backward(STARTING_MOVE_DISTANCE+(score.level*2))
        time.sleep(0.1)














