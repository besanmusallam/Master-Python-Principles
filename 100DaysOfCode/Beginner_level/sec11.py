# Blackjack Game
# This is a simple implementation of a Blackjack game where you can play against the computer.

import random
cards = [i for i in range(1, 12)]

your_cards = [random.choice(cards), random.choice(cards)]
computer = [random.choice(cards), random.choice(cards)]

print(f"Your cards: {your_cards}")
print(f"Computer's first card: {computer[0]}")

if sum(your_cards) > 21:
    print("you lose")

new = input("Type 'y' to get another card, type 'n' to pass: ")

if new == "y":
    your_cards.append(random.choice(cards))
    if sum(your_cards) > 21:
        print(f"Your Cards: {your_cards}")
        print(f"Computer's Cards: {computer}")
        print("you lose")
    elif sum(computer) < 17:
        computer[0] = random.choice(cards)
else:
    if sum(your_cards) > 21:
        print("you lose")
        print(f"Your Cards: {your_cards}")
        print(f"Computer's Cards: {computer}")
    elif sum(computer) < 17:
        computer[0] = random.choice(cards)

if sum(your_cards) > sum(computer):
    print("You win")
    print(f"Your Cards: {your_cards}")
    print(f"Computer's Cards: {computer}")
elif sum(computer) > sum(your_cards):
    print("you lose")
    print(f"Your Cards: {your_cards}")
    print(f"Computer's Cards: {computer}")
else:
    your_cards[:-1] = random.choice(cards)
    if sum(your_cards) > sum(computer):
        print("You win")
        print(f"Your Cards: {your_cards}")
        print(f"Computer's Cards: {computer}")
    elif sum(computer) > sum(your_cards):
        print("you lose")
        print(f"Your Cards: {your_cards}")
        print(f"Computer's Cards: {computer}")






