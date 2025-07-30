# # CSV: Comma Separated Values

# # with open("weather_data.csv") as data_file:
# #     content = data_file.read()
# #     print(content)

# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #         print(row)

# # print(temperature)


# import pandas as pd
# data = pd.read_csv("weather_data.csv")

# # series: is a single column in a pandas dataframe

# data_dict = data.to_dict()
# print(data_dict)

# temparature = data['temp'].to_list()
# avg_temp = sum(temparature) // len(temparature) 
# print(f"the average of the temperatures is : {avg_temp}")

# avg_temp = data['temp'].mean()
# print(f"the average of the temperatures is : {avg_temp}")

import pandas as pd

df = pd.read_csv("Squirrel_Data.csv")
# print(df['Primary Fur Color'])

required_table = df.groupby('Primary Fur Color')['Primary Fur Color'].count()
required_table = pd.DataFrame(required_table)
required_table = required_table.rename(columns={'Primary Fur Color': 'Fur', 'Primary Fur Color': 'Count'})
print(required_table)
print(type(required_table))