# Secret Auction Program

# TODO-1: Ask the user for input
auction = {}
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("what is your bid?: "))

auction[name] = bid
new = input("Are there any other bidders? Type 'yes' or 'no' ")

while new == "yes":
    name = input("What is your name?: ")
    bid = int(input("what is your bid?: "))
    new = input("Are there any other bidders? Type 'yes' or 'no' ")

    auction[name] = bid

j = 0
for i in auction:
    if auction[i] > j:
        j = auction[i]

name = [key for key, val in auction.items() if val == j]
print(f"The winner is {name[0]} with a bid of {j}")



