from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#C70039")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-20, -100)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 45, "normal"))

    def point(self):
        self.score += 1
        self.update()
