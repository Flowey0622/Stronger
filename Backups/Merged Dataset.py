import pandas as pd
import numpy as np

# loading dataset into the program
dataset1 = pd.read_csv(r"D:\SNS\London 2000-01-01 to 2024-02-17.csv", index_col="datetime")
dataset2 = pd.read_csv("london_weather.csv", index_col="date", parse_dates=["date"])

# combine two datasets
merged_data = pd.merge(dataset1, dataset2, left_index=True, right_index=True, how='outer')

# change index type to datetime
merged_data.index = pd.to_datetime(merged_data.index)
print(merged_data.index)

# Print with the merged data
pd.set_option('display.max_rows', None)  # display all rows
pd.set_option('display.max_columns', None)  # display all columns
pd.set_option('display.width', None)  # no limitation with width
print(merged_data.head())
print(merged_data)
print(merged_data.columns)

# just keep five same parameters
final_data = merged_data.copy()

# create avg_max_temp
final_data.loc['1979-01-01':'1999-12-31', 'avg_max_temp'] = final_data.loc['1979-01-01':'1999-12-31', 'max_temp']
avg_maxtemp_2000_2020 = final_data.loc['2000-01-01':'2020-12-31', ['max_temp', 'tempmax']].mean(axis=1)
final_data.loc['2000-01-01':'2020-12-31', 'avg_max_temp'] = avg_maxtemp_2000_2020
final_data.loc['2021-01-01':, 'avg_max_temp'] = final_data.loc['2021-01-01':, 'tempmax']

# create avg_min_temp
final_data.loc['1979-01-01':'1999-12-31', 'avg_min_temp'] = final_data.loc['1979-01-01':'1999-12-31', 'min_temp']
avg_mintemp_2000_2020 = final_data.loc['2000-01-01':'2020-12-31', ['min_temp', 'tempmin']].mean(axis=1)
final_data.loc['2000-01-01':'2020-12-31', 'avg_min_temp'] = avg_mintemp_2000_2020
final_data.loc['2021-01-01':, 'avg_min_temp'] = final_data.loc['2021-01-01':, 'tempmin']

# create avg_mean_temp
final_data.loc['1979-01-01':'1999-12-31', 'avg_mean_temp'] = final_data.loc['1979-01-01':'1999-12-31', 'mean_temp']
avg_temp_2000_2020 = final_data.loc['2000-01-01':'2020-12-31', ['mean_temp', 'temp']].mean(axis=1)
final_data.loc['2000-01-01':'2020-12-31', 'avg_mean_temp'] = avg_temp_2000_2020
final_data.loc['2021-01-01':, 'avg_mean_temp'] = final_data.loc['2021-01-01':, 'temp']

# create avg_cloud_cover
final_data.loc['1979-01-01':'1999-12-31', 'avg_cloud_cover'] = final_data.loc['1979-01-01':'1999-12-31', 'cloud_cover']
avg_cloudcover_2000_2020 = final_data.loc['2000-01-01':'2020-12-31', ['cloud_cover', 'cloudcover']].mean(axis=1)
final_data.loc['2000-01-01':'2020-12-31', 'avg_cloud_cover'] = avg_cloudcover_2000_2020
final_data.loc['2021-01-01':, 'avg_cloud_cover'] = final_data.loc['2021-01-01':, 'cloudcover']

# create avg_precipitation
final_data.loc['1979-01-01':'1999-12-31', 'avg_precipitation'] = final_data.loc['1979-01-01':'1999-12-31', 'precipitation']
avg_precipitation_2000_2020 = final_data.loc['2000-01-01':'2020-12-31', ['precipitation', 'precip']].mean(axis=1)
final_data.loc['2000-01-01':'2020-12-31', 'avg_precipitation'] = avg_precipitation_2000_2020
final_data.loc['2021-01-01':, 'avg_precipitation'] = final_data.loc['2021-01-01':, 'precip']

print(final_data.head())
print(final_data.tail())
#print(final_data)
print(final_data.columns)

# just select five parameters
columns_to_keep = ['avg_max_temp', 'avg_min_temp', 'avg_mean_temp', 'avg_cloud_cover', 'avg_precipitation']
selected_data = final_data[columns_to_keep].copy()

print(selected_data)
print(selected_data.head())
print(selected_data.tail())