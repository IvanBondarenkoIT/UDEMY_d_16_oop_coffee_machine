from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = input(f"What would you like? {menu.get_items()}:")
    if user_choice == "off":
        break
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        user_choice = menu.find_drink(user_choice)
        if user_choice:
            if coffee_maker.is_resource_sufficient(user_choice):
                if money_machine.make_payment(user_choice.cost):
                    coffee_maker.make_coffee(user_choice)