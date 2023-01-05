from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_create = CoffeeMaker()
money_check = MoneyMachine()
is_on = True

coffee_create.report()
money_check.report()

while is_on:
    options = menu.get_items()
    want = input(f"What would you like? ({options}): ")
    if want == "off":
        is_on = False
    elif want == "report":
        coffee_create.report()
        money_check.report()
    else:
        chose = menu.find_drink(want)
        if coffee_create.is_resource_sufficient(chose) and money_check.make_payment(chose.cost):
            coffee_create.make_coffee(chose)