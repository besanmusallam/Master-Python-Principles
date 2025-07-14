# TODO: 1. Print report.
# TODO: 2. check resources sufficient?
# TODO: 3. Process coins.
# TODO: 4. Check transaction successful?
# TODO: 5. Make Coffee.

from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    drink = input("What would you like? (espresso/latte/cappuccino) ")
    drink = menu.find_drink(drink)
    if coffee_maker.is_resource_sufficient(drink):
        money_machine.make_payment(drink.cost)
        coffee_maker.make_coffee(drink)
    else:
        print("Resouce is insufficient")
    coffee_maker.report()
    money_machine.report()
    is_on = bool(input(""))


