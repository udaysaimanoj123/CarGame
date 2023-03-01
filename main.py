import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

game_is_on = True

car=CarManager()
turt=Player()
score=Scoreboard()

screen.onkey(turt.move_up,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    if turt.ycor()>=290:
        turt.refresh()
        score.increase()

    for i in car.all_cars:
        if turt.distance(i) <28:
            score.game_over()
            game_is_on=False





screen.exitonclick()
