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

def update_resources(coffe_name):
    global resources
    for i in MENU[coffe_name]["ingredients"]:
        left = resources[i] - MENU[coffe_name]["ingredients"][i]
        resources[i] = left

def check_sufficient_resources(coffe_name):
    for item in MENU[coffe_name]['ingredients']:
        if MENU[coffe_name]["ingredients"][item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True



def report(resource):
    global money
    for i in resource:
        print(f"{i}: {resource[i]}")
    print(f"Money: ${money}")

def restock():
    global resources
    print("Restocking resources...")
    resources['water'] += int(input("How much water do you want to add?: "))
    resources['coffee'] += int(input("How much coffee do you want to add?: "))
    resources['milk'] += int(input("How much milk do you want to add?: "))
    print("Resources have been restocked!")


def admin_mode():
    password='1234'
    user_input=input('Enter your password')
    if user_input==password:
        while True:
            admin_choice = input("Admin Options: (restock/report/off): ").lower().strip()
            if admin_choice == "restock":
                restock()
            elif admin_choice == "report":
                report(resources)
            elif admin_choice == "off":
                print("Exiting admin mode.")
                break
            else:
                print("Invalid option. Choose restock, report, or off.")
    else:
        print("Incorrect password.")


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
    global  money

    if MENU[coffe_name]['cost'] > user_coin:
        print(f"{coffe_name} cost : ${MENU[coffe_name]['cost']} but you only inserted ${user_coin}")
        print("Sorry that is not enough Money.Money refunded")
        return

    elif MENU[coffe_name]['cost'] < user_coin:
        change = user_coin - MENU[coffe_name]['cost']
        print(f"here is your ${round(change,2)} in change")
        print(f"here is your ${coffe_name} ☕ Enjoy!!")
        money += float(MENU[coffe_name]['cost'])
        update_resources(coffe_name)
    elif  MENU[coffe_name]['cost'] == user_coin:
        print(f"Here is your {coffe_name} ☕ Enjoy!!")
        money += float(MENU[coffe_name]['cost'])
        update_resources(coffe_name)


while coffe_machine:

    choose = input("What would you like? (espresso/latte/cappuccino/report/admin/off): ").lower().strip()
    # Strip to remove extra spaces

    # Handle empty or invalid input

    if choose=='':
        print("You didn't enter anything. Please choose espresso, latte, or cappuccino.")
    elif choose == "off":
        coffe_machine = False
    if choose == 'report':
        report(resources)
    elif choose == "admin":
        admin_mode()

    elif choose in MENU:
        if check_sufficient_resources(choose):
            user_coins = process_coins()
            check_transaction(choose, user_coins)
        else:
            print("Not enough resources to make that drink.")
    else:
        print("Invalid choice. Please select from espresso, latte, or cappuccino.")