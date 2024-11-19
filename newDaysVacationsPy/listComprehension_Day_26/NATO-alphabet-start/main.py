import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
theDict = {value.letter: value.code for (key, value) in data.iterrows()}
continueGame = True

def askname():
    try:
        theName = input("What is your name ? \n").upper().strip()
        decode = print([theDict[i] for i in theName])
    except KeyError:
        print("your name need to have no digits in it, only alphabet letters")
        askname()
    else:
        print(decode)

askname()
