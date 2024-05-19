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
P = 0.01
N = 0.05
D = 0.1
Q = 0.25
total = float(0)
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
def take_coins(q, d, n, p, name):
    total = q*Q + d*D + n*N +p*P
    if total > MENU[name]["cost"]:



# Make coffee
def make_coffee(name):
    possible = check_possible(name)
    if possible:
        print("Please insert coin.")
        quarter = input("How many quarters?")
        dime = input("How many dimes?")
        nickel = input("How many nickels?")
        penny = input("How many pennies?")
        take_coins(quarter, dime, nickel, penny, name)
        deduct(name)


while start:
    user = str(input("What do you want?"))
    user = user.lower()
    if user != "off" or user != "report" or user != "latte" or user != "espresso" or user != "cappuccino":
        print("Invalid input")
    elif user == "off":
        start = False
    elif user == "report":
        print(f"Water: {stock["water"]}\nMilk: {stock["milk"]}\nCoffee: {stock["milk"]}")
        # Print current ingredient left
    else:
        make_coffee(user)
