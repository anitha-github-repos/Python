
def report(resource,money):
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']
    if 'money' in resource:
        resource['money'] += money
    else:
        resource['money'] = 0
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def coffee_selection(flavor, resource, menu):
    water_used = menu[flavor]['ingredients']['water']
    if flavor != 'espresso':
        milk_used = menu[flavor]['ingredients']['milk']
    coffee_used = menu[flavor]['ingredients']['coffee']
    cost_of_coffee = menu[flavor]['cost']
    resource['water'] -= water_used
    if flavor != 'espresso':
        resource['milk'] -= milk_used
    resource['coffee'] -= coffee_used
    if 'money' in resource:
        resource['money'] += cost_of_coffee
    else:
        resource['money'] = cost_of_coffee
    return resource


def resource_check(resource, menu, flavor):
    if resource['water'] >= menu[flavor]['ingredients']['water'] and resource['coffee'] >= menu[flavor]['ingredients']['coffee']:
        if flavor!= 'espresso' and resource['milk'] >= menu[flavor]['ingredients']['milk']:
            return True
        else:
            return True
    else:
        return False



#report(resources, 0)
#print(resources)
#print(MENU['cappuccino']['ingredients']['water'])

#print(coffee_selection('espresso', resources))


def coffee():
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
    }
    continue_or_not = True
    user_choice = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    while continue_or_not:
        if user_choice == 'report':
            if 'money' not in resources:
                report(resources, 0)
            else:
                report(resources, resources['money'])
        elif resource_check(resources, MENU, user_choice):
            resources = coffee_selection(user_choice, resources, MENU)
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_cost = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            if total_cost > MENU[user_choice]['cost']:
                change = total_cost - MENU[user_choice]['cost']
                change = round(change, 2)
            if total_cost == MENU[user_choice]['cost']:
                print(f"Here is your {user_choice} ☕. Enjoy!")
            elif total_cost > MENU[user_choice]['cost']:
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['water'] >= MENU[user_choice]['ingredients']['water']:
                print("  Sorry there is not enough water.")
            elif resources['milk'] >= MENU[user_choice]['ingredients']['milk']:
                print("  Sorry there is not enough milk.")
            else:
                print("  Sorry there is not enough coffee.")
        user_choice = input("  What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'off':
            continue_or_not = False



coffee()