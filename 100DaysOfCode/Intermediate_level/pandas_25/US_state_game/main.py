# turtle only works with .gif image extention

import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")
print(df.info())

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess = []


while len(guess) < 50:

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    states = df['state'].to_list() 

    if answer_state in states:
        guess.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)





screen.exitonclick() 
