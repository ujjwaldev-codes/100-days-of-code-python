# Using OOP this time
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()
status ="on"
while status =="on":
    payment=0
    order =input(f"What would you like? {menu.get_items()}: ")
    if order =="off":
        status="off"
    elif order =="report":
        coffee_maker.report()
        moneyMachine.report()
    elif order =="espresso"or  order =="latte" or order =="cappuccino": 
        drink =menu.find_drink(order)
        if(coffee_maker.is_resource_sufficient(drink)):
            if(moneyMachine.make_payment(drink.cost)):
               coffee_maker.make_coffee(drink)
    else:
        print("Wrong input !")

