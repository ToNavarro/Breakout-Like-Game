from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=650, starty=20, startx=None)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

# Create Paddle
pad = Paddle((0, -280))
# Create Ball
ball = Ball()
# Create Bricks
bricks = []
colors = ["#49FF00", "#FBFF00", "#FF9300", "#FF0000"]
y_build = 50
for row in range(8):
    x_build = -355
    if row < 2:
        color = colors[0]
    elif row < 4:
        color = colors[1]
    elif row < 6:
        color = colors[2]
    else:
        color = colors[3]

    for n in range(11):
        bricks.append(Brick(pos=(x_build, y_build), color=color))
        x_build += 70

    y_build += 30

# Create Scoreboard
score = Scoreboard()

screen.listen()
screen.onkeypress(pad.go_left, "Left")
screen.onkeypress(pad.go_right, "Right")

brick_count = len(bricks)

while brick_count > 0:
    screen.update()
    time.sleep(0.02)
    ball.move()

    # Detect collisions with wall
    if ball.ycor() > 280 or ball.xcor() > 380 or ball.xcor() < - 380:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(pad) < 50 and ball.ycor() < -250:
        ball.hit()

    # Detect collision with brick
    for br in bricks:
        if br.xcor()-20 <= ball.xcor() <= br.xcor()+20:
            if br.ycor()-20 <= ball.ycor() <= br.ycor()+20:
                br.goto(1000, 1000)
                ball.brick_collision(side=False)
                bricks.remove(br)
                score.point()

    # Detect lost live
    if ball.ycor() > 290:
        ball.restart()

screen.exitonclick()


# TODO: Add Lives and show below score
# TODO: Add side collision with bricks
# TODO: Adjust collision in x-axis
# TODO: Adjust collision in brick corners
