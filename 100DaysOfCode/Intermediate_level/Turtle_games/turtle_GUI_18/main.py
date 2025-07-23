import random
import turtle
from turtle import Turtle, Screen, colormode

tim = Turtle()
screen = Screen()
colormode(255)


screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

tim.pensize(5)
tim.speed("fastest")
for i in range(1, 20):
    for j in range(23):
        tim.color(tuple(random.randint(0,255) for _ in range(3)))
        tim.dot()
        tim.penup()
        tim.forward(30)
        tim.pendown()

    if i % 2 == 1:
        tim.left(90)
        tim.penup()
        tim.forward(30)
        tim.pendown()
        tim.left(90)
    else:
        tim.right(90)
        tim.penup()
        tim.forward(30)
        tim.pendown()
        tim.right(90)



screen.exitonclick()