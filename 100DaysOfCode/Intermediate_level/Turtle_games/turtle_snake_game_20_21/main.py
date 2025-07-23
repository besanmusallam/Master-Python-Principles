from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



# TODO: 1. Create snake body
# TODO: 2. Move the snake
snake = Snake()
food = Food()
# TODO: 5. Create a scoreboard
scoreboard = ScoreBoard()

# TODO: 3. Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # illusion of smooth motion
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: 4. Detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # TODO: 6. Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # TODO: 7. Detect collision with tail
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
