import pandas

data = pandas.read_csv("Squirrel_Data_2018.csv")
allColors = data["Primary Fur Color"].tolist()
singleColors = list(set(allColors))
for i in singleColors:
    if type(i) != str:
        singleColors.remove(i)
ColorsCount = [allColors.count(i) for i in singleColors]
theDict = {"FurColors": singleColors,
           "count": ColorsCount}
print(theDict)
data = pandas.DataFrame(theDict)
data.to_csv("theNewSquirrel_Data_Day25.csv")