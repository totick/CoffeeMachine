from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


while True:
    print("What would you like? (espresso/latte/cappuccino)")
    user_input = input(">> ").strip().lower()

    match user_input:
        case "off":
            break
        case "espresso" | "latte" | "cappuccino":
            #prepare_drink(user_input)
            pass
        case "report":
            #print_report()
            pass
        case _:
            print("Not a valid option: ", user_input)

print("Coffee machine off.")