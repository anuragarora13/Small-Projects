resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}


coffe_machine = True

quarters = dimes = nickles = pennies = money = 0

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
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

def check_sufficient_resources(coffe_name):
    # MENU[coffe_name][ingredients]=
    global resources

    for i in  MENU[coffe_name]["ingredients"]:
        left=resources[i]- MENU[coffe_name]["ingredients"][i]
        resources[i]=left




def report(resource):
    global money
    for i in resource:
        print(f"{i}: {resource[i]}")
    print(f"Money: ${money}")


def process_coins():
    print('please insert coins: ')
    global quarters, dimes, nickles, pennies
    quarters = float(input('How manu quarters?: '))
    dimes = float(input('How manu dimes?: '))
    nickles = float(input('How manu nickles : '))
    pennies = float(input('How manu  pennies?: '))
    total_value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_value


def check_transaction(coffe_name, user_coin):
    global MENU, money

    if MENU[coffe_name]['cost'] > user_coin:
        print(f"{coffe_name} cost : ${MENU[coffe_name]['cost']} but you only inserted ${user_coin}")
        print("Sorry that is not enough Money.Money refunded")
        money = 0
        check_sufficient_resources()
    elif MENU[coffe_name]['cost'] < user_coin:
        change = user_coin - MENU[coffe_name]['cost']
        print(f"here is your ${round(change,2)} in change")
        print(f"here is your ${coffe_name} ☕ Enjoy!!")
        money = float(MENU[coffe_name]['cost'])
        check_sufficient_resources(coffe_name)



while coffe_machine:
    choose = input("What would you like?  (espresso/latte/cappuccino):  ").lower()
    if choose == 'report':
        report(resources)
    elif choose == 'latte':
        user_coins = process_coins()
        check_transaction(choose, user_coins)
    elif choose == 'off':
        coffe_machine = Fals