
UNITS = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$"
}

drinks = {
    "espresso": {
        "water": 50,
        "coffee": 18
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24
    }
}

resources = {
    "water": 100,
    "milk": 50,
    "coffee": 76,
    "money": 0
}

def print_report():
    for key, value in resources.items():
        print(f"\t{key.capitalize()}:\t{value} {UNITS[key]}")


def check_resources(drink_name: str) -> list[tuple(str, int)]:
    """
    Checks if there are enough resources for creating the drink.
    :param drink_name: THe name of the drink to prepare
    :return: A list with tuples containing the name and the missing amount of the resource, if no missing ingredients
        it returns an empty list.
    """
    drink: dict = drinks[drink_name]
    missing_resources: list[tuple(str, int)] = []

    for key, value in drink.items():
        if value >= resources[key]:
            missing_amount = resources[key] - value
            missing_resources.append((key, missing_amount))

    return missing_resources


while True:
    print("What would you like? (espresso/latte/capuccino)")
    user_input = input("> ").strip().lower()

    match user_input:
        case "off":
            break
        case "espresso":
            pass
        case "latte":
            pass
        case "cappuccino":
            pass
        case "report":
            print_report()
        case _:
            print(user_input)

print("Coffee machine off.")