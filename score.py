from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

