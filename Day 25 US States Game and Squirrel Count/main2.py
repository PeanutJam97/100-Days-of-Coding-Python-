import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = data["Primary Fur Color"].to_list()
grey_list = 0
red_list = 0
black_list = 0

for color in color_list:
    if color == "Gray":
        grey_list += 1
    if color == "Cinnamon":
        red_list += 1
    if color == "Black":
        black_list += 1

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_list, red_list, black_list]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

