import random
from turtle import Turtle, Screen

screen = Screen()

def game():

    screen.setup(width=500, height=400)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_position = [-70, -40, -10, 20, 50, 80]

    is_race_on = False
    guess = screen.textinput(title="make you bet", prompt="Who do you think will win the race? ")
    if guess:
        is_race_on = True

        turtles = []
        for i in range(6):
            new = Turtle("turtle")
            new.penup()
            new.color(colors[i])
            new.goto(x=-230, y=y_position[i])
            turtles.append(new)

    while is_race_on:
        
        for turtle in turtles:  

            if turtle.xcor() > 230:
                is_race_on = False
                win = turtle.pencolor()
                if win == guess:
                    print("You win!")
                    break
                else:
                    print("Game Over")
                    break

            radnom_dist = random.randint(0, 10)
            turtle.forward(radnom_dist)

game()

screen.exitonclick()