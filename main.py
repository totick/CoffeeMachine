
drinks = {
    "espresso": {
        "water": {"amount": 50, "unit": "ml"},
        "coffee": {"amount": 18, "unit": "g"}
    },
    "latte": {
        "water": {"amount": 200, "unit": "ml"},
        "milk": {"amount": 150, "unit": "ml"},
        "coffee": {"amount": 24, "unit": "g"}
    },
    "cappuccino": {
        "water": {"amount": 250, "unit": "ml"},
        "milk": {"amount": 100, "unit": "ml"},
        "coffee": {"amount": 24, "unit": "g"}
    }
}

resources = {
    "water": {"amount": 100, "unit": "ml"},
    "milk": {"amount": 50, "unit": "ml"},
    "coffee": {"amount": 76, "unit": "g"},
    "money": {"amount": 0, "unit": "$"}
}

def print_report():
    for key, value in resources.items():
        print(f"\t{key.capitalize()}:\t{value["amount"]}{value["unit"]}")


def check_resources(drink_name: str) -> bool:
    pass


while True:
    print("What would you like? (espresso/latte/capuccino)")
    user_input = input("> ").lower()

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
