MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO: 1. Print report of resources

def print_report():
    """Print the current resources available"""
    print("water: ", resources["water"], "ml")
    print("milk: ", resources["milk"], "ml")
    print("coffee: ", resources["coffee"], "g")
    print("Money: $", resources["money"])

def change_report(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

# TODO: 2. Check if resources Are sufficient
def check_resources(drink):
    total = 0
    """Check if there are enough resources to make the drink"""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] <=  resources[ingredient]:
            total +=1
            if ingredient == ["water"]:
                print("Water: ", ingredient(), "ml")
            elif ingredient == ["Milk"]:
                print("Milk: ", ingredient(), "ml")
            elif ingredient == ["Coffee"]:
                print("Coffee: ", ingredient(), "g") 

        else:
            if ingredient == ["water"]:
                print("Sorry there is not enough water.")
            elif ingredient == ["Milk"]:
                print("Sorry there is not enough milk.")
            elif ingredient == ["Coffee"]:
                print("Sorry there is not enough coffee.") 
    
    return total == 3

def coins_request():
    coins = {}
    coins["quarter"] = int(input("quarters: "))
    coins["dimes"] = int(input("dimes: "))
    coins["nickels"] = int(input("nickels: "))
    coins["pennies"] = int(input("pennies: "))
    return coins

# TODO: 3. Process coins
def process_coins(coins):
    """Process coins into Total amounts in dollars $"""
    quarter = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    total = 0
    total += coins["quarter"] * quarter
    total += coins["dimes"] * dimes
    total += coins["nickels"] * nickels
    total += coins["pennies"] * pennies

    return total

# TODO: 4. Check if the transaction was successful
def check_transaction(drink):
    return process_coins >= MENU[drink["cost"]]


# TODO: 5. Make Coffee

def make_coffee():
    """Make a coffee function"""
    
    print_report()
    drink = input("What would you like? (espresso/latte/cappuccino) ")
    if check_resources(drink):
        coins = coins_request()
        total = process_coins(coins)
        if check_transaction:
            change = total - MENU[drink]["cost"]
            change_report(drink)
            print_report()
            print(f"Your change is {change}$")
            print(f"Here is your {drink}. Enjoy!")
        else:
            print("Not enough money")
    else:
        print("please fill resources")

make_coffee()









