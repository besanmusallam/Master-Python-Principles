import numpy as np


ls = [i for i in range(256)]



def binary_search(ls, item):
    low = 0
    high = len(ls) - 1
    i = 0

    while low <= high:
        i += 1
        mid = (low + high) // 2
        guess = ls[mid]

        if guess < item:
            low = mid + 1
        elif  guess > item:
            high = mid - 1
        else:
            return mid, i
    return None, i

guess, i = binary_search(ls, 88)
print(f"Guess: {guess}, Iterations: {i}")