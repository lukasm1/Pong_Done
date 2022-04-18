from turtle import Screen
from score import Score
from paddles import Paddle
from ball import Ball
import time

STARTING_POSITIONS = [(350, 0), (-350, 0)]

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.bgpic('./light.png')
screen.tracer(0)

screen.listen()

ball = Ball()
score = Score()
r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

game = True

while game:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.reverse_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.reverse_x()
    elif ball.xcor() < -380:
        score.pc_point()
        ball.reset_ball()
    elif ball.xcor() > 380:
        score.user_point()
        ball.reset_ball()

    screen.update()

screen.exitonclick()
