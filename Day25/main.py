# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
#
# data = pandas.read_csv('weather_data.csv')
# #print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(len(temp_list))
#
# avg = data['temp'].mean()
# print(avg)
#
# maxi = data['temp'].max()
# print(maxi)
#
# #Get Data in Columns
# print(data['condition'])
# print(data.condition)
#
# #Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
#
# #Conversion temperature to Fahrenheit
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#Create a dataframe grom scratch
# data_dict = {
#     'students':['Amy','James','Angela'],
#     'scores':[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])
white_squirrel_count = len(data[data['Primary Fur Color'] == 'White'])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)
print(white_squirrel_count)

data_dict = {
    'Fur Color':['Gray','Cinnamon','Black','White'],
    'Count':[grey_squirrel_count,red_squirrel_count,black_squirrel_count,white_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel.csv')