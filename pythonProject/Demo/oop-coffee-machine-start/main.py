from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

continue_game=True;
def execute():
    command = input(f"what would you like ? {menus} ")
    while command=="report":
        CoffeeMaker().report();
        command = input(f"what would you like ? {menus} ")
    if command != "report":
        drink=Menu().find_drink(command)
        possible_drink=CoffeeMaker().is_resource_sufficient(drink)
        if possible_drink:
            if MoneyMachine().make_payment(drink.cost):
                CoffeeMaker().make_coffee(drink)


while continue_game==True:
    menus=Menu().get_items()
    execute()

