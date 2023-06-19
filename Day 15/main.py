from menu import resources, MENU as menu


# TODO 4: Check is sufficient resources
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO 5: Process coins
def process_coins():
    """Asks user coins and calculates them"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Todo 6: PRocess payment
def process_payment(drink_cost, payment):
    if drink_cost <= payment:
        print(f"Here is your change {round(payment - drink_cost, 2)}€.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money. Money refunded.")
        return False


# Todo 7: Make cofeee and remove from list
def make_coffee(drink_name, ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink_name}. Enjoy!")

# TODO 1: Ask user what he wants
profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO 2:Turn off the coffee machine by entering off
    if choice == "off":
        print("Exiting")
        is_on = False

# TODO 3: Print report
    elif choice == "report":
        print(f"Water: {resources['water']}ml.\nMilk: {resources['milk']}ml.\nCoffee: {resources['coffee']}g.\nMoney: {profit}€.")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if process_payment(drink['cost'], payment):
                make_coffee(choice, drink['ingredients'])