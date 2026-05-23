# Read cvs Files
import csv


with open("weather_data.csv", "r") as data_file:
    weather_data = csv.reader(data_file)
    temperatures = []
    for row in weather_data:
        # only temperature in the list
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)


# Using pandas library
import pandas
weather_data = pandas.read_csv("weather_data.csv")
print(weather_data)
print(weather_data["temp"])

weather_data_dict = weather_data.to_dict()
print(weather_data_dict)

temp_list = weather_data["temp"].to_list()
print(temp_list)

# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
print(weather_data["temp"].mean())
print(weather_data["temp"].max())
print(weather_data["temp"].min())

# Get Data in Columns
print(weather_data["condition"])
print(weather_data.condition)

# Get Data in Row
print(weather_data[weather_data.day == "Monday"])
print(weather_data[weather_data.temp == weather_data["temp"].max()])

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy","James","Angela"],
    "score": [76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")