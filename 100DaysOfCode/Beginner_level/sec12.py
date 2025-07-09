# Number Guessing Game
# This is a simple number guessing game where the player has to guess a randomly chosen number within

import random


print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
num = random.randint(1, 100)


def random_number(num, guess):
    if num > guess:
        return "Too Low"
    elif num < guess:
        return "Too High"
    else:
        return "You guessed right"

if level == 'hard':
    print("you have 5 attempts")
    for i in range(5):
        guess = int(input("Make a guess: "))
        x = random_number(num, guess)
        print(x)
        if x == "You guessed right":
            break
elif level == 'easy':
    print("you have 10 attempts")
    for i in range(10):
        guess = int(input("Make a guess: "))
        x = random_number(num, guess)
        print(x)
        if x == "You guessed right":
            break
else:
    print("Name error")