# rock, paper, scissors game
# This is a simple game where the player chooses rock, paper, or scissors, and the

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.choice(game)
print(game[player])

print("computer chose: ")
print(computer)

if game[player] == computer :
    print("it's a draw")
elif game[player] == rock and computer == paper:
    print("You Lose")
elif game[player] == rock and computer == scissors:
    print("You Win")
elif game[player] == paper and computer == rock:
    print("You Win")
elif game[player] == paper and computer == scissors:
    print("You lose")
elif game[player] == scissors and computer == rock:
    print("You lose")
elif game[player] == scissors and computer == paper:
    print("You Win")
