from turtle import Screen
from ball1 import Ball
from paddle1 import Paddle
from scoreboard1 import Scoreboard
import time


screen = Screen()
screen.setup(width= 800,height=600)
screen.bgcolor("#000")
screen.title("Welcome to Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with ball
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    #Detect collision with right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.left_point()

    #Detect L paddle misses
    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.right_point()




    screen.exitonclick()