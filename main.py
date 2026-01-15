
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
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}

coffee_machine = {
    "resources": {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }
}


def print_report() -> None:
    """
    Prints the resources available in the coffee machine
    """
    for key, value in coffee_machine["resources"].items():
        print(f"\t{key.capitalize()}:\t{value} {UNITS[key]}")


def check_resources(drink_name: str) -> list[tuple]:
    """
    Checks if there are enough resources for creating the drink.
    :param drink_name: THe name of the drink to prepare
    :return: A list with tuples containing the name and the missing amount of the resource, if no missing ingredients
        it returns an empty list.
    """
    drink_resources: dict = drinks[drink_name]["resources"]
    missing_resources: list[tuple] = []

    for key, value in drink_resources.items():
        if value > coffee_machine["resources"][key]:
            missing_amount = abs(coffee_machine["resources"][key] - value)
            missing_resources.append((key, missing_amount))

    return missing_resources


def process_payment(drink_name: str) -> bool:
    """
    Gets payment input from the user. Returns True if payment for drink was successful.
    :param drink_name: The name of the drink
    :return: True if payment was enough, otherwise False
    """
    total: float = 0
    payment_success = False
    price_of_drink = drinks[drink_name]["money"]
    print(f"{drink_name}: ${price_of_drink:.2f}")
    print("Please insert coins (quarter = 25, dime = 10, nickel = 5, penny = 1):")
    for name, value in COINS.items():
        amount = int(input(f"{name}s = "))
        total += amount * value
        if total >= price_of_drink:
            payment_success = True
            break

    change = total - price_of_drink
    print(f"Money back = ${change:.2f}")
    return payment_success


def update_resources(drink_name: str) -> None:
    """
    Updates the resources of the coffee machine (water, milk, coffee) but subtracting the resources needed for the drink
    :param drink_name: Then name of the drink
    """
    drink_resources = drinks[drink_name]["resources"]
    for resource_name, resource_value in drink_resources.items():
        coffee_machine["resources"][resource_name] -= resource_value


def prepare_drink(drink_name: str) -> None:
    missing: list = check_resources(drink_name)
    if missing:
        print("Not able to prepare drink. Missing resources:")
        for resource_name, amount in missing:
            print(f"\t{resource_name}: {amount} {UNITS[resource_name]}")
        return

    payment_success = process_payment(drink_name)
    if payment_success:
        update_resources(drink_name)
        print(f"Here is your {drink_name}")
    else:
        print(f"Not enough payment")


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