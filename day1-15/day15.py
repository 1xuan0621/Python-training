

def check_resources(coffee_para):
    if MENU[coffee_para]["ingredients"]['water'] > resources['water']:
        print('Sorry there is not enough water')
        return 0
    resources['water'] = resources['water'] - MENU[coffee_para]["ingredients"]['water']
    resources['coffee'] = resources['coffee'] - MENU[coffee_para]["ingredients"]['coffee']
    if coffee_para == 'latte' or coffee_para == 'cappuccino':
        if MENU[coffee_para]["ingredients"]['milk'] > resources['milk']:
            print('Sorry there is not enough milk')
            return 0
        resources['milk'] = resources['milk'] - MENU[coffee_para]["ingredients"]['milk']
    return resources


def pay_money(coffee_para):
    print('Please insert coins')
    quarters = int(input('How many quarters? ')) * 0.25
    dimes = int(input('How many dimes? ')) * 0.10
    nickles = int(input('How many nickles? ')) * 0.05
    pennies = int(input('How many pennies? ')) * 0.01
    total_pay = quarters + dimes + nickles + pennies
    change = round(total_pay - MENU[coffee_para]['cost'],2)
    if change < 0:
        return 'Sorry that\' not enough money. '
    resources['money'] += round(total_pay - change,2)
    return f'Here is ${change} in change. '


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def coffee_on():
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        for item in resources:
            print(f'{item} : {resources[item]}')
    elif choice == 'off':
        return 0
    else:
        if check_resources(choice) == 0:
            return
        print(pay_money(choice))
        print(f'Have a nice {choice}')
while coffee_on() != 0:
    pass