
resources = {
    "water": (100, "ml"),
    "milk": (50, "ml"),
    "coffee": (76, "ml"),
    "money": (0, "$")
}

def print_report():
    for key, value in resources.items():
        amount, unit = value
        print(f"\t{key.capitalize()}:\t{amount}{unit}")


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
