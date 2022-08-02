# An attempt of simulating a coffee machine program
coffee_cup = """
 ( (
    ) )
  ........
  |      |]
  \      /    
   `----'
"""
resource = {
    'water': 2500,
    'milk': 1500,
    'coffee': 240,
    'money' : 0
}

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def report_resource():
    print(f"Water: {resource['water']}ml\n"
          f"Milk: {resource['milk']}ml\n"
          f"Coffee: {resource['coffee']}g\n"
          f"Money: ${resource['money']}")


def turn_off():
    print("Please wait...\n"
          "Power off...")


def make_drink(drink):
    print(f"Please wait. Making {drink}.")


def check_ingredients(request):
    if resource['water'] < menu[request]['ingredients']['water']:
        print("Please fill the water reservoir")
        return False
    if resource['milk'] < menu[request]['ingredients']['milk']:
        print("Please fill the milk reservoir")
        return False
    if resource['coffee'] < menu[request]['ingredients']['coffee']:
        print(f"Insufficient coffee to complete your {request}.")
        return False


def deduct_ingredients(coffee_name):
    resource['water'] -= menu[coffee_name]['ingredients']['water']
    resource['milk'] -= menu[coffee_name]['ingredients']['milk']
    resource['coffee'] -= menu[coffee_name]['ingredients']['coffee']
    resource['money'] += menu[coffee_name]['cost']


def money(coin):
    try:
        received = int(input(f"How many {coin} did you put in the slot?"))
    except (ValueError):
        print("Unrecognised currency.\nPlease try again.")
    else:
        return received


quarters, dimes, nickles,pennies = 0.25, 0.1, 0.05, 0.01


def take_money():
    print("Please insert your money!\n")
    coins = ['quarters', 'dimes', 'nickles', 'pennies']
    try:
        q = quarters * money(coins[0])
        d = dimes * money(coins[1])
        n = nickles * money(coins[2])
        p = pennies * money(coins[3])
        money_inserted = round(q+d+n+p, 2)
    except TypeError:
        pass
    else:
        return money_inserted


# prompting the user for a command
message = "Please wait..."
serving = True
while serving:
    prompt = input('What would you like? (espresso/latte/cappuccino) > ')
    if prompt.lower() == 'off':
        turn_off()
        break

    if prompt.lower() == 'report':
        report_resource()

    else:
        money_taken = take_money()
        print(f"\n${money_taken} received.")
        money_checked = True

        if money_taken > menu[prompt]['cost']:
            change = round(money_taken - menu[prompt]['cost'], 2)
            print(f"Here is your ${change} change!")
            money_checked = True
            check_ingredients(prompt)
            if check_ingredients(prompt):
                deduct_ingredients(prompt)
            print(message)
        if money_taken < menu[prompt]['cost']:
            print("Money insufficient to complete order!")
            money_checked = False
            serving = False
        if money_taken == menu[prompt]['cost']:
            print(message)
            money_checked = True
            check_ingredients(prompt)
            if check_ingredients(prompt):
                deduct_ingredients(prompt)

        if money_checked:
            deduct_ingredients(prompt)
            print(f"Here's your {prompt.title()}")
            print(coffee_cup)
            print("Enjoy!")

        else:
            print("Please try again later.")





