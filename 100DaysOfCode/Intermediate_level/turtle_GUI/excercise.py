import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.shape('turtle')
timmy.color("DeepPink4")
screen = Screen()


timmy.pensize(5)
timmy.speed("fastest")
colormode(255)

# Create different shapes with different colors
for i in range(3, 11):
    timmy.color(tuple(random.randint(0,255) for _ in range(3)))
    steps = i
    angle = 360 // steps
    for j in range(steps):
        timmy.forward(50)
        timmy.right(angle)

timmy.pensize(1)
timmy.penup()
timmy.forward(100)
timmy.pendown()

# Draw a spirograph
for i in range(36):
    timmy.color(tuple(random.randint(0,255) for _ in range(3)))
    timmy.circle(100)
    timmy.right(10)






screen.exitonclick()