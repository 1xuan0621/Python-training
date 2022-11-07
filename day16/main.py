from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee_maker_on = True

while coffee_maker_on:
    choice = input(f'What would you like? {menu.get_items()}: ')
    if choice == 'report':
        coffe_maker.report()
        money_machine.report()
    elif choice == 'off':
        coffee_maker_on = False
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)