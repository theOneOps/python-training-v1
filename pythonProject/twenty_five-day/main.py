import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

dict = {
    "Fun Color":["red", "gray","black"],
    "Count":[data[data["Primary Fur Color"] == "Gray"].count()["Primary Fur Color"],
    data[data["Primary Fur Color"] == "Cinnamon"].count()["Primary Fur Color"],
    data[data["Primary Fur Color"] == "Black"].count()["Primary Fur Color"]]}

new_data = pandas.DataFrame(dict)
print(new_data)
new_data.to_csv("new_squirrel_Census")