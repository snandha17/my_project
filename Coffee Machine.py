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

profit=0
is_on = True
def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"water: {water}ml")
    print(f"milk: {milk}ml")
    print(f"coffee: {coffee}g")
    print(f"Money: ${profit}")

def resource_reduce(which_type):
    global profit
    global is_on
    if which_type == 'espresso':
        if resources["water"] >= MENU[which_type]['ingredients']["water"] and resources["coffee"] >=MENU[which_type]['ingredients']["coffee"]:
            resources["water"] = resources["water"] - MENU[which_type]['ingredients']["water"]
            resources["coffee"] = resources["coffee"] - MENU[which_type]['ingredients']["coffee"]
            amount = coin_process()
            if amount >= MENU["espresso"]["cost"]:
                change = amount - MENU["espresso"]["cost"]
                profit += MENU["espresso"]["cost"]
                print(f"Here is ${round(change,3)}in change. ")
                print("Here is your espresso ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough water.")
            is_on = False
    elif which_type == 'latte' or which_type == 'cappuccino':
        if resources["water"] >=  MENU[which_type]['ingredients']["water"] and resources["coffee"] >= MENU[which_type]['ingredients']["coffee"] and     resources["milk"] >= MENU[which_type]['ingredients']["milk"]:
            resources["water"] = resources["water"] - MENU[which_type]['ingredients']["water"]
            resources["milk"] = resources["milk"] - MENU[which_type]['ingredients']["milk"]
            resources["coffee"] = resources["coffee"] - MENU[which_type]['ingredients']["coffee"]
            amount = coin_process()
            if amount >= MENU[which_type]["cost"]:
                change = amount - MENU[which_type]["cost"]
                profit += MENU[which_type]["cost"]
                print(f"Here is ${round(change, 3)}in change. ")
                print(f"Here is your {which_type} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough water.")
            is_on = False
def coin_process():
    print("Please enter the coins")
    quarters = int(input("how many quarters?: "))*0.25
    dimes = int(input("how many dimes?: "))*0.10
    nickles = int(input("how many nickles?: "))*0.05
    pennies = int(input("how many pennies?: "))*0.01
    total = quarters+dimes+nickles+pennies
    return total


while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "off":
        is_on = False
    if user_choice == "report":
        report()
    resource_reduce(user_choice)
