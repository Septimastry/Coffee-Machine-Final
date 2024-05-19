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

stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Variables
money = 0.0
P = 0.01
N = 0.05
D = 0.1
Q = 0.25
start = True


# Check ingredients
def check_possible(name):
    name = name.lower()
    poss = True
    for x in MENU[name]["ingredients"]:
        if MENU[name]["ingredients"][x] > stock[x]:
            poss = False
            print(f"Not enough {x}")
    if not poss:
        return False
    else:
        return True


# Take out ingredient
def deduct(name):
    for x in MENU[name]["ingredients"]:
        stock[x] -= MENU[name]["ingredients"][x]


# Take coins
def take_coins(q, d, n, p, name, m):
    total = float(q)*Q + float(d)*D + float(n)*N + float(p)*P
    if total > MENU[name]["cost"]:
        change = total - MENU[name]["cost"]
        profit = MENU[name]["cost"]
        m += profit
        return change, m, True
    else:
        print("Not enough money, coins refunded.")
        return 0, m, False


# Make coffee
def make_coffee(name, mon):
    possible = check_possible(name)
    if possible:
        print("Please insert coin.")
        quarter = input("How many quarters?")
        dime = input("How many dimes?")
        nickel = input("How many nickels?")
        penny = input("How many pennies?")
        change, mon, proceed = take_coins(quarter, dime, nickel, penny, name, mon)
        if proceed:
            print(f"Here is ${round(change, 2)} change.")
            print(f"Here is your {name} ☕ enjoy!")
            deduct(name)
        return mon


while start:
    user = str(input("What do you want?"))
    user = user.lower()
    if user != "off" and user != "report" and user != "latte" and user != "espresso" and user != "cappuccino":
        print("Invalid input")
    elif user == "off":
        start = False
    elif user == "report":
        print(f"Water: {stock["water"]}\nMilk: {stock["milk"]}\nCoffee: {stock["milk"]}\nProfit: {money}")
        # Print current ingredient left
    else:
        money = make_coffee(user, money)
