from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

rahakone = MoneyMachine()
kahvikone = CoffeeMaker()
menu = Menu()
is_on = True

def get_report():
    kahvikone.report()
    rahakone.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        get_report()
    else:
        drink = menu.find_drink(choice)
        if kahvikone.is_resource_sufficient(drink) and rahakone.make_payment(drink.cost):
            kahvikone.make_coffee(drink)