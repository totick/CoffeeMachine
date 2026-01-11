
UNITS = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$"
}

drinks = {
    "espresso": {
        "resources": {
            "water": 50,
            "coffee": 18
        },
        "money": 1.5
    },
    "latte": {
        "resources": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "money": 2.5
    },
    "cappuccino": {
        "resources": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "money": 3.0
    }
}

COINS = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

coffee_machine = {
    "resources": {
        "water": 300,
        "milk": 200,
        "coffee": 100
    },
    "money": 0.0
}


def print_report():
    for key, value in coffee_machine["resources"].items():
        print(f"\t{key.capitalize()}:\t{value} {UNITS[key]}")


def check_resources(drink_name: str) -> list[tuple(str, int)]:
    """
    Checks if there are enough resources for creating the drink.
    :param drink_name: THe name of the drink to prepare
    :return: A list with tuples containing the name and the missing amount of the resource, if no missing ingredients
        it returns an empty list.
    """
    drink_resources: dict = drinks[drink_name]["resources"]
    missing_resources: list[tuple(str, int)] = []

    for key, value in drink_resources.items():
        if value >= coffee_machine["resources"][key]:
            missing_amount = abs(coffee_machine["resources"][key] - value)
            missing_resources.append((key, missing_amount))

    return missing_resources


def process_coins(drink_name: str) -> None:
    """
    Takes input from the users payment and adds the sum to the coffee machine.
    Exits function when the user gives a value that is not a coin.
    :param drink_name: The name of the drink to pay for.
    """
    print(f"{drink_name}: {drinks[drink_name]["money"]}$")
    while True:
        left_to_pay = drinks[drink_name]["money"] - coffee_machine["money"]
        print(f"Left to pay: {left_to_pay:.2}$")
        print("Please insert coins (quarter = 25, dime = 10, nickel = 5, penny = 1):")
        payment_input = input(">> ")
        if payment_input.lower() in COINS:
            coin_value = COINS[payment_input]
            coffee_machine["money"] += coin_value
        else:
            break



def prepare_drink(drink_name: str) -> None:
    missing: list = check_resources(drink_name)
    if missing:
        print("Not able to prepare drink. Missing resources:")
        for resource_name, amount in missing:
            print(f"\t{resource_name}: {amount} {UNITS[resource_name]}")
        return

    process_coins(drink_name)
    change = coffee_machine["money"] - drinks[drink_name]["money"]
    if change >= 0:
        print(f"Here is your {drink_name}")
    else:
        print(f"Not enough money")
        print(f"Return = {coffee_machine["money"]}$")
        coffee_machine["money"] = 0.0

    print("User payment: {}".format(coffee_machine["money"]))



while True:
    print("What would you like? (espresso/latte/cappuccino)")
    user_input = input(">> ").strip().lower()

    match user_input:
        case "off":
            break
        case "espresso" | "latte" | "cappuccino":
            prepare_drink(user_input)
        case "report":
            print_report()
        case _:
            print(user_input)

print("Coffee machine off.")