# 2022/02/24
# import csv

# with open('day25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas

# data = pandas.read_csv('day25/weather_data.csv')
# print(data)

# temp_list = data['temp'].to_list()

# monday = data[data.day == 'Monday']
# print(int(monday.temp)*(9/5)+32)

data = pandas.read_csv('day25/Central_Park_Squirrel_Data.csv')

gray = data[data['Primary Fur Color'] == 'Gray']
red = data[data['Primary Fur Color'] == 'Cinnamon']
black = data[data['Primary Fur Color'] == 'Black']

grey_count = len(gray['Primary Fur Color'])
red_count = len(red['Primary Fur Color'])
black_count = len(black['Primary Fur Color'])

data_dict = {
    'Fur_Color' : ['gray', 'red', 'black'],
    'Count' : [grey_count, red_count, black_count],
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv('day25/new_data.csv')
