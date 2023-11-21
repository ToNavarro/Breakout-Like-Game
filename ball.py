from turtle import Turtle

# Not using it: MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("#9400FF")
        self.x_move = 5
        self.y_move = 6
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce(self):
        if self.ycor() > 280 or self.ycor() < - 280:
            self.y_move *= -1
        if self.xcor() > 380 or self.xcor() < - 380:
            self.x_move *= -1

    def hit(self):
        self.y_move *= -1
        # self.move_speed *= 0.9

    def restart(self):
        y = self.ycor()
        self.home()
        self.sety(y)
        self.hit()
        self.move_speed = 0.05

    def brick_collision(self, side):
        if not side:
            self.y_move *= -1
        else:
            self.x_move *= -1

