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


money_spent = 0
continuar = True

while continuar == True:
    # ASK WHAT USER WANTS
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    # TURN OFF
    if coffee == "off":
        print("Turning off...")
        break

    # REPORT
    if coffee == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Money: {money_spent}")

    # CHECK IF RESOURCES ARE SUFFICIENT
    if coffee in MENU:
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            print("Sorry there is not enough water.")
            break
        elif coffee == "latte" or coffee == "cappuccino":
            if resources['milk'] < MENU[coffee]['ingredients']['milk']:
                print("Sorry there is not enough milk.")
                break
        elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            break

        # CHECK IF THERE'S ENOUGH MONEY
        print("Please insert coins.")
        quarter_value = 0.25
        dime_value = 0.10
        nickel_value = 0.05
        penny_value = 0.01
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        money = (quarters * quarter_value) + (dimes * dime_value) + (nickels * nickel_value) + (pennies * penny_value)
        if money > MENU[coffee]['cost']:
            change = money - MENU[coffee]['cost']
            money_spent += MENU[coffee]['cost']
            print("Total money inserted:", money)
            resources['water'] -= MENU[coffee]['ingredients']['water']
            if coffee == "latte" or coffee == "cappuccino":
                resources['milk'] -= MENU[coffee]['ingredients']['milk']
            resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
            print(f"Here is your change {change:.2f}")
            print(f"Here is your {coffee} ☕️, enjoy it.")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Invalid choice. Please select a valid option.")
