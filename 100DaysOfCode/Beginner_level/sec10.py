# Calculator Program
# This program implements a simple calculator that can perform addition, subtraction, multiplication, and division.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


def calculator(n1, n2):
    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multi(n1, n2)
    elif operation == "/":
        return division(n1, n2)
    else:
        return "you picked wrong operation"

n1 = int(input("what's your first number? "))
print("+ \n - \n * \n /")
operation = input("Pick an operation: ")
n2 = int(input("what's your next number? "))


result = calculator(n1, n2)
print(f"{n1} {operation} {n2} = {result}")

cont = input(f"type 'y' to continue with {result}, or type 'n' to start a new calculation: ")

while cont == "y":
    n1 = result
    operation = input("Pick an operation: ")
    n2 = int(input("what's your next number? "))
    result = calculator(n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    cont = input(f"type 'y' to continue with {result}, or type 'n' to start a new calculation: ")






