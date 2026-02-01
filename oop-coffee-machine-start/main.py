from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
m = Menu()

while True:
    print("What would you like?")
    print(m.get_items())
    user_input = input(">> ").strip().lower()

    match user_input:
        case "off":
            break
        case "espresso" | "latte" | "cappuccino":
            drink = m.find_drink(user_input)
            if cm.is_resource_sufficient(drink):
                enough_money = mm.make_payment(drink.cost)
                if enough_money:
                    cm.make_coffee(drink)
                else:
                    print("Not enough money, no drink for you!!!")
            else:
                print("Unable to make drink")
        case "report":
            cm.report()
            mm.report()
        case _:
            print("Not a valid option: ", user_input)

print("Coffee machine off.")