
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



def resourceusage(userinput, resources, MENU):
    if userinput == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        return resources
    elif userinput == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        return resources
    elif userinput == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        return resources
    else:
        return resources

def changecontroller(userinput, money, MENU):
    newvalue = money - MENU[userinput]["cost"]
    return newvalue

def ingredientchecker(userinput, resources, MENU):
    if resources["water"] < 0:
        resources["water"] += MENU[userinput]["ingredients"]["water"]
        resources["milk"] += MENU[userinput]["ingredients"]["milk"]
        resources["coffee"] += MENU[userinput]["ingredients"]["coffee"]
        print("Sorry there is not enough water.")
        return "continue"
    elif resources["milk"] < 0:
        resources["water"] += MENU[userinput]["ingredients"]["water"]
        resources["milk"] += MENU[userinput]["ingredients"]["milk"]
        resources["coffee"] += MENU[userinput]["ingredients"]["coffee"]
        print("Sorry there is not enough milk.")
        return "continue"
    elif resources["coffee"] < 0:
        resources["water"] += MENU[userinput]["ingredients"]["water"]
        resources["milk"] += MENU[userinput]["ingredients"]["milk"]
        resources["coffee"] += MENU[userinput]["ingredients"]["coffee"]
        print("Sorry there is not enough coffee.")
        return "continue"
    else:
        return "ok"
   

def coffeemachine():
    money = 0
    coffeemachineon = True
    
    

    while coffeemachineon:
        waterindex = resources["water"]
        milkindex = resources["milk"]
        coffeeindex = resources["coffee"]
        coffeemachineinput = input("What would you like? (espresso/latte/cappuccino): ")
        resourceusage(coffeemachineinput, resources, MENU)
        statement = str(ingredientchecker(coffeemachineinput, resources, MENU))
        
        if coffeemachineinput == "off":
            coffeemachineon = False

        if coffeemachineinput == "report":
            print(f"Water : {waterindex}ml\nMilk : {milkindex}ml\nCoffee: {coffeeindex}g\nMoney: ${money}")
        elif "ok" in statement and coffeemachineon == True:
            print("Please insert coins.")
            quarterinput = int(input("how many quarters?: "))
            #quarter =  25 cents
            dimeinput = int(input("how many dimes?: "))
            #dime = 10 cents
            nickelinput = int(input("how many nickels?: "))
            #nickel = 5 cents
            pennyinput = int(input("how many pennies?: "))
            #penny = 1 cent
        else:
            coffeemachineon = False

        
        
        if coffeemachineinput != "report" and "ok" in statement and coffeemachineon == True:
            money = quarterinput*0.25 + dimeinput*0.10 + nickelinput*0.05 + pennyinput*0.01
            money = round((changecontroller(coffeemachineinput, money, MENU)),2)
            if money < 0:
                print("Sorry that's not enough money. Money refunded.")
                money == 0
            else:
                print(f"Here is ${money} in change.")
                print(f"Here is your {coffeemachineinput} ☕ Enjoy!")
        else:
            coffeemachineon = False

        if statement == "continue":
            coffeemachineon = True




coffeemachine()
