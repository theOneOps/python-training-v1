
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temp = []
    for i in data:
        if i[1] != "temp":
            temp.append(int(i[1]))


import pandas

datas = pandas.read_csv('weather_data.csv')
print(datas["temp"])