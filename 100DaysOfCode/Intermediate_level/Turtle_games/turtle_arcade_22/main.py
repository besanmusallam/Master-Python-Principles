from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

PADDLE1_POSITION = (350, 0)
PADDLE2_POSITION =(-350, 0)

# TODO: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)


# TODO: Create and move a paddle
paddle1 = Paddle(PADDLE1_POSITION)
paddle2 = Paddle(PADDLE2_POSITION)
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "e")
screen.onkey(paddle2.down, "d")


# TODO: Create the ball and make it move
ball = Ball()
player1 = ScoreBoard(1, (150, 240))
player2 = ScoreBoard(2, (-150, 240))




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

# TODO: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

# TODO: Detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:  
        ball.bounce_paddle()


# TODO: Detect when paddle misses
    
    if ball.xcor() > 350 :
        ball.reset()
        player2.increase_score()

    if ball.xcor() < -350 :
        ball.reset()
        player1.increase_score()
    
# TODO: Keep score





screen.exitonclick()