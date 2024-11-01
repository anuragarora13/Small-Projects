from flask import Flask, render_template, request

app = Flask(__name__)

# Your coffee machine logic here
resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

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

money = 0

def check_sufficient_resources(coffe_name):
    for item in MENU[coffe_name]['ingredients']:
        if MENU[coffe_name]["ingredients"][item] > resources[item]:
            return False
    return True

def update_resources(coffe_name):
    for item in MENU[coffe_name]["ingredients"]:
        resources[item] -= MENU[coffe_name]["ingredients"][item]

@app.route('/')
def index():
    return render_template('index.html', menu=MENU, resources=resources)

@app.route('/order', methods=['POST'])
def order():
    coffee_name = request.form['coffee']
    if check_sufficient_resources(coffee_name):
        update_resources(coffee_name)
        return render_template('order.html', coffee_name=coffee_name)
    else:
         return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)