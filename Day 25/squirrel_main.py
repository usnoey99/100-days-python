import pandas

DATA_FILE = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pandas.read_csv(DATA_FILE)

colours = squirrel_data["Primary Fur Color"]

# for colour in colours:
#     if colour == "Gray":
#         grey_count += 1
#     elif colour == "Cinnamon":
#         red_count += 1
#     elif colour == "Black":
#         black_count += 1


grey_squirrels = squirrel_data[colours == "Gray"]
red_squirrels = squirrel_data[colours == "Cinnamon"]
black_squirrels = squirrel_data[colours == "Black"]

grey_count = len(grey_squirrels)
red_count = len(red_squirrels)
black_count = len(black_squirrels)

colours_dict = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : [grey_count, red_count, black_count]
}

colours_dict_data = pandas.DataFrame(colours_dict)
colours_dict_data.to_csv("squirrel_count.csv")
