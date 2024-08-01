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

money = 0

def materialAvailability(resources, recipe):
    continueCoffee = True
    for key, value in recipe.items():
        if resources[key] < value:
            continueCoffee = False
            print(f"Sorry there is not enough {key}.")
    
    return continueCoffee

def processCoins(balance = 0):
    userBalance = balance
    quarters = int(input("Insert quarters($0.25): "))
    dimes = int(input("Insert dimes($0.10): "))
    nickles = int(input("Insert nickles($0.05): "))
    pennies = int(input("Insert pennies($0.01): "))
    userBalance += quarters * 0.25
    userBalance += dimes * 0.10
    userBalance += nickles * 0.05
    userBalance += pennies * 0.01
    return userBalance

def processCoffee(resources, recipe):
    for key, value in recipe.items():
        resources[key] = resources[key] - value

    return resources



while True:
    userBalance = 0
    userInput = input("​What would you like? (espresso/latte/cappuccino): ").lower()

    if userInput in MENU:
        if materialAvailability(resources, MENU[userInput]['ingredients']):
            userBalance = processCoins(userBalance)
            if userBalance < MENU[userInput]['cost']:
                print(f"Sorry that's not enough money. Money refunded.")
                continue

            resources = processCoffee(resources, MENU[userInput]['ingredients'])

            print(f"Here is your {userInput}☕. Enjoy the drink")
            money +=  MENU[userInput]['cost']
            if userBalance > MENU[userInput]['cost']:
                print(f"You inserted ${userBalance}. Here is your change ${userBalance - MENU[userInput]['cost']}")
        else:
            continue

    elif userInput == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
        continue
    elif userInput == 'off':
        print(f"The machine if switched off..")
        break
    else:
        print(f"Insert right command")