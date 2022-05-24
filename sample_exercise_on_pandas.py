import csv
temperatures = []

with open("weather_data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == "temp":
            continue
        temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
#print(data["temp"])

print(data["temp"].mean())
print(data["temp"].max())

s = data[data.condition == "Sunny"]
print(s.day)

count = []
squirrel = {}

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"].dropna().unique()
print(colors)
gray_count_frame = data[data["Primary Fur Color"] == "Gray"]
gray_count = gray_count_frame["Primary Fur Color"].count()
# count.append(gray_count)
# print(count)

for color in colors:
    color_count_frame = data[data["Primary Fur Color"] == color]
    color_count = color_count_frame["Primary Fur Color"].count()
    count.append(color_count)

squirrel["Fur Color"] = colors
squirrel["Count"] = count


d = pandas.DataFrame(squirrel)
d.to_csv("squirrel.csv")

