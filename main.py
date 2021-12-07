from data import MENU
from data import resources

# Setting up global variables
machine_is_on = True
machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources["coffee"]


# Print a report of remaining resources
def report():
    """Returns a report of the global variables in the coffe machine"""
    global machine_water
    global machine_milk
    global machine_coffee
    print(f"Water: {machine_water}\nMilk: {machine_milk}\nCoffe: {machine_coffee}")


# Have the customer choose a drink
def drink_choice():
    """Asks the user to choose a drink, returns the drink as a string"""
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    choice.lower()
    if choice == "off":
        off()
        start()
    elif choice == "report":
        report()
        start()
    else:
        return choice


# Have the customer enter their money
def entered_cash():
    """Asks the user to insert money, returns inserted money as a float"""
    total_cash = 0
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    quarters = quarters * 0.25
    dimes = int(input("How many dimes? "))
    dimes = dimes * 0.10
    nickles = int(input("How many nickles? "))
    nickles = nickles * 0.05
    pennies = int(input("How many pennies? "))
    pennies = pennies * 0.01
    total_cash = quarters + dimes + nickles + pennies
    return total_cash


# Make an Off button
def off():
    """Exits the machine, aka stops the program from running"""
    global machine_is_on
    machine_is_on = False
    exit()


# Function to compare prices
def return_change(user_choice, money):
    """Returns the change depending on the cost and money, also checks if its enough money and restarts machine if
    its not """
    cost = MENU[user_choice]["cost"]
    change = money - cost

    if change < 0.0:
        print("Sorry that's not enough money. Money refunded")
        start()
    else:
        print(f"Your change is ${round(change,2)}")
        print(f"Here is your {user_choice} enjoy!")


# Function to reduce resources
def reduce_resources(user_choice):
    """Reduces resources from the machine and stops the restarts the machine if there is not enough
    reports to user which resource is missing"""
    global machine_water
    global machine_milk
    global machine_coffee
    if machine_water < MENU[user_choice]["ingredients"]["water"]:
        print("Sorry, not enough water.")
        start()
    elif machine_milk < MENU[user_choice]["ingredients"]["milk"]:
        print("Sorry, not enough milk.")
        start()
    elif machine_coffee < MENU[user_choice]["ingredients"]["coffee"]:
        print("Sorry, not enough coffee.")
        start()
    else:
        machine_water = machine_water - MENU[user_choice]["ingredients"]["water"]
        machine_milk = machine_milk - MENU[user_choice]["ingredients"]["milk"]
        machine_coffee = machine_coffee - MENU[user_choice]["ingredients"]["coffee"]


# Function to start machine
def start():
    while machine_is_on:
        user_choice = drink_choice()
        reduce_resources(user_choice)
        user_cash = entered_cash()
        return_change(user_choice,user_cash)


start()