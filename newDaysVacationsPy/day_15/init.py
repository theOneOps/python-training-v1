from main import menu
from main import resources as res

end_game = True
monnaie = 0.


def report(m, money):
    for key in m:
        print(f"{key}: {m[key]}")
    print(f"money: {money}")


def calculateMoney(a, b, c, d):
    return a * 0.01 + b * 0.1 + c * 0.05 + d * 0.25


def enoughMoney(cost, totalmoney):
    return cost < totalmoney


def enoughIngredients(askinput, ressources):
    for key in askinput:
        if askinput[key] > ressources[key]:
            return key
    return True


def toReturn(mymoney, askcost):
    if mymoney - askcost >= 0:
        print(f"Here is ${mymoney - askcost} in change")


def reactualizeResources(myresource, askinput):
    for key in askinput:
        myresource[key] -= askinput[key]
    return myresource


def askSomething(money, resources):
    question = ''

    while question not in menu.keys() and question != "report":
        question = input("what would you like ? (espresso/latte/cappuccino):")

    if question == 'report':
        report(resources, money)
        askSomething(money, resources)

    if question in menu.keys():
        print("Please insert some coins")
        quarter = int(input("How many quarters ? :"))
        dimes = int(input("How many dimes ? :"))
        nickles = int(input("How many nickles ? :"))
        pennies = int(input("How many pennies ? :"))

        inputmoney = calculateMoney(pennies, dimes, nickles, quarter)

        if enoughMoney(menu[question]["cost"], inputmoney):
            if enoughIngredients(menu[question]["ingredients"], resources) is True:
                money += inputmoney
                toReturn(money, menu[question]["cost"])
                money -= inputmoney
                money += menu[question]["cost"]
                data = reactualizeResources(resources, menu[question]["ingredients"])
                resources = data
                print(f"Here is your {question}")

            else:
                print(f"Sorry there's not enough {enoughIngredients(menu[question]['ingredients'], resources)}")

        else:
            print("Sorry, that's not enough money, money refund ")

    askSomething(money, resources)


askSomething(monnaie, res)
