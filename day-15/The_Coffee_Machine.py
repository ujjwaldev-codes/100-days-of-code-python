"""
Coffee Machine Program Requirements
1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “ off ” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""
menu ={
    "espresso":{"ingredients":{
        "water":50,
        "coffee":18,
        "milk":0,
    },
    "cost":1.5,},
    "latte":{"ingredients":{
        "water":200,
        "milk":150,
        "coffee":24,
    },
    "cost":2.5,},
    "cappuccino":{"ingredients":{
        "water":250,
        "milk":100,
        "coffee":24,
    },
    "cost":3.8,}

}
resource={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0,
}
def updateResources(choice, amount):
    resource["money"]=resource["money"]+amount
    resource["water"]=resource["water"]-menu[choice]["ingredients"]["water"]
    resource["milk"]=resource["milk"]-menu[choice]["ingredients"]["milk"]
    resource["coffee"]=resource["coffee"]-menu[choice]["ingredients"]["coffee"]

def resources():
    print(f"Water : {resource["water"]}ml\nMilk : {resource["milk"]}ml\nCoffee : {resource["coffee"]}ml\nMoney : {resource["money"]}")
def checkResources(choice):
    c =0
    if menu[choice]["ingredients"]["milk"]<=resource["milk"]:
        c=c+1
    else:
        print("Sorry, milk is not enough for the order !")
    if menu[choice]["ingredients"]["water"]<=resource["water"]:
        c=c+1 
    else:
        print("Sorry, water is not enough for the order !")
    if menu[choice]["ingredients"]["coffee"]<=resource["coffee"]:
        c=c+1
    else:
        print("Sorry, coffee is not enough for the order !")
    return c
def checkTransaction():
    print("Please insert the money :  ")
    dimes = int(input("How many dimes :  "))
    quaters = int(input("How many quaters :  "))
    nickles = int(input("How many nickles :  "))
    pennies = int(input("How many pennies :  "))
    return (quaters*0.25 + dimes*0.10 + nickles*0.05+ pennies*0.01)
status = "on"
print("\n\n==================================================== THE COFFEE MACHINE (ON)====================================================\n")
while status =="on":
    payment=0
    order =input("What would you like? (espresso/latte/cappuccino): ")
    if order =="off":
        status="off"
    elif order =="report":
        resources()
    elif order =="espresso"or  order =="latte" or order =="cappuccino": 
        if(checkResources(order)==3):
           payment =checkTransaction()
           if payment<menu[order]["cost"]:
               print("Sorry there is not enough money !")
               print("Here is refund of $"+str(payment))
           else:
               print(f"Order successful, here is the change of ${(payment-menu[order]["cost"]):.2f}.")
               print("Enjoy your "+order)
               updateResources(order, menu[order]["cost"])
    else:
        print("Wrong input !")
        
    
print("\n\n==================================================== THE COFFEE MACHINE (OFF) ====================================================\n")
