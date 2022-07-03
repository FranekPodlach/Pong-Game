from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.listen()

screen.delay(0)
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
screen.onkey(r_paddle.up ,"Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
sleep_time = 0.1
while game_is_on:
    time.sleep(sleep_time)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        sleep_time -= 0.005
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.reset()
        sleep_time = 0.1
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.reset()
        sleep_time = 0.1
        scoreboard.r_point()
        




screen.exitonclick()