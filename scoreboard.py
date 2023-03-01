FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-220,265)
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score :{self.level}", align="center", font=FONT)

    def increase(self):
        self.level+=1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over Score is {self.level}", align="center", font=FONT)

