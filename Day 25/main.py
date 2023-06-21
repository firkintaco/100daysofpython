# data = []
#
# with open("./weather_data.csv") as weather_data:
#     content = weather_data.readlines()
#     for weather in content:
#         data.append(weather.replace("/n", "").strip())
#
# print(data)
#
# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for weather in data:
#         if weather[1] != "temp":
#             temperatures.append(int(weather[1]))
#     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
#
# def calculate_average(temp_list):
#     total_temp = 0
#     for temp in temp_list:
#         total_temp += temp
#     return round(total_temp/ len(temp_list),1)
#
# print(calculate_average(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in colum
# print(data.condition)

# Get data in row
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# def to_f(c):
#     return (c * 9)/5 + 32
#
#
# print(monday.temp.apply(to_f))
# print(monday)

# Create dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Jessice"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")