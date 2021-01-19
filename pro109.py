import csv
import pandas as pd 
import statistics 
import random

df=pd.read_csv('data1.csv')
data=df["math score"].tolist()

math_mean=statistics.mean(data)
print('mean is:',math_mean)

math_mode=statistics.mode(data)
print('mode is:',math_mode)

math_median=statistics.median(data)
print('median is:',math_median)

math_sd=statistics.stdev(data)
print('stdev is:',math_sd)


first_std_deviation_start,first_std_deviation_end=math_mean-math_sd,math_mean+math_sd

second_std_deviation_start,second_std_deviation_end=math_mean-(2*math_sd),math_mean+(2*math_sd)

third_std_deviation_start,third_std_deviation_end=math_mean-(3*math_sd),math_mean+(3*math_sd)


list_of_data_within_1_std_deviation = [ result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]

list_of_data_within_2_std_deviation = [ result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]

list_of_data_within_3_std_deviation = [ result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]


print("{} % of data lies in first std".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{} % of data lies in second std".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{} % of data lies in third std".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))