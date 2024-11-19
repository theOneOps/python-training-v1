bank: float


def addMoney(money: float = 350) -> int:
    money += 5.
    print(f"money-> {money} ")
    return int(money)


def buyWater():
    global bank
    if bank > 20:
        print("Water bought successfully")
        bank -= 20
        print(f"money-> {bank} ")
    else:
        print("No enough money for water")


bank = 12
bank = addMoney(bank)
bank = addMoney(bank)
bank = addMoney(bank)
buyWater()
buyWater()
