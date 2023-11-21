from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("#9400FF")
        self.goto(pos)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def go_right(self):
        if not self.can_move():
            self.goto(340, self.ycor())
            return
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_left(self):
        if not self.can_move():
            self.goto(-340, self.ycor())
            return
        new_x = self.xcor() - MOVE_DISTANCE
        # print("y_cor: ", self.ycor())
        # print("New: ", new_y)
        self.goto(new_x, self.ycor())

    def can_move(self):
        if self.xcor() < -340 or self.xcor() > 340:
            return False
        else:
            return True
