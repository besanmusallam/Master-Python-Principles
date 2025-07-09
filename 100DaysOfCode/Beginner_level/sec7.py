# Hangman Game - Step 1
# This is a simple Hangman game where the player has to guess letters of a randomly chosen

import random

# TODO-1: Create a random word list and choose a word from it.
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()
display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
