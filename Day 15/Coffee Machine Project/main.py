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

def is_enough_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def coin_insert():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total_insert = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies

    return total_insert

def report():
    print(f"Water: {resources["water"]}\n"
          f"Milk: {resources["milk"]}\n"
          f"Coffee: {resources["coffee"]}\n"
          f"Money: ${resources["money"]}\n")

def process_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)

        if change > 0:
            print(f"Here is ${change} dollars in change.")

        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while True:
    order = input("What would you like? (espresso/latte/cppuccino): ").lower()

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if order == "off":
        print("Turning off the machine. Goodbye!")
        break

# TODO 3. Print report.
    elif order == "report":
        report()

    # When the user chooses a drink, the program should check
    # if there are enough resources to make that drink.
    # It should not continue to make the drink
    # but print: “Sorry there is not enough water.”

    elif order == "espresso" or order == "latte" or order == "cppuccino":
        drink = MENU[order]
        # TODO 4. Check resources sufficient?
        if is_enough_resources(drink["ingredients"]):
            # TODO 5. Process coins.
            total_insert = coin_insert()
            # TODO 6. Check transaction successful?
            if total_insert < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                break
            else:
                process_transaction(total_insert, drink["cost"])

                # TODO 7. Make Coffee.
                make_coffe(drink["ingredients"])
                print(f"Here is your {order} ☕️ Enjoy!")





