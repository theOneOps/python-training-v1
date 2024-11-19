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

ressources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

unity=["ml","ml","g","$"]

continue_game=True;
ressources["money"]=0;

def execute(cmd):
  light_on=True;
  while cmd== "report":
    a=0;
    for i in ressources:
      print(f"{i}:{ressources[i]}{unity[a]}")
      a+=1;
    cmd = input("what would you like ? (espresso/latte/cappuccino): ")
  if cmd=="espresso" or cmd=="latte" or cmd=="cappuccino":
    print("please insert coins.")
    quarter=int(input("how many quarter ?: "))
    dimes=int(input("how many dimes ?: "))
    nickles=int(input("how many nickles ?: "))
    pennies=int(input("how many pennies ?: "))
    change_put=(quarter*25+dimes*10+nickles*5+pennies)/100
    if change_put > MENU[cmd]["cost"] :
      for i in MENU[cmd]["ingredients"]:
        a=MENU[cmd]["ingredients"][i]
        if ressources[i] >= MENU[cmd]["ingredients"][i]:
          light_on=light_on and True;
        else:
          light_on=light_on and False;
    else:
        print("Sorry that's not enough money, Money refunded ")
        return;

  if light_on==True:
    for i in MENU[cmd]["ingredients"]:
        a=MENU[cmd]["ingredients"][i]
        b=ressources[i]-MENU[cmd]["ingredients"][i]
        ressources[i]=b;
    print(f"Here is your ${change_put-MENU[cmd]['cost']} in change.")
    print(f"Here is your {cmd} Enjoy it, Have a good day !")
    ressources["money"]+=MENU[cmd]["cost"]
  else:
    print(f"we don't have enough ressources to make your {cmd}, we're sorry...")
    return;

while continue_game==True:
  command=input("what would you like ? (espresso/latte/cappuccino): ")
  execute(cmd=command);








