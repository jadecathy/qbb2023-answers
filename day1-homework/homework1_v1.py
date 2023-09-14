#!/usr/bin/env python
# Author: Qi Wang, Date:09/05/2023

import numpy as np

f = open("inflammation-01.csv","r");
lines = f.readlines() # type is list


## Exercise 1 reding the data #####################################
# for this part, print the number of flare-ups that the fifth patient had on the first, tenth, and last day.
data_ary = np.array(lines)
# print(data_ary[0])
patient1_ary = data_ary[4].split(",")
# print(patient1_ary)
print("exercise1\n")
print("first day", patient1_ary[0]);
print("tenth day", patient1_ary[9]);
print("last day", patient1_ary[-1]);


## Exercise 2 calculating the average #####################################
# For each patient, calculate the average number of flare-ups per day. Print the average values for the first 10 patients.
# These are the row averages - for example, patient 1 has 5.45 flare-ups per day on average; patient 2 has 5.425 flare-ups per day on average.

print("exercise2\n")
data_ary_stripped = np.char.rstrip(data_ary)
average_list = []
for each_p in data_ary_stripped:
 	# print(each_p)
	each_p_list = each_p.split(",")
	for i in range(len(each_p_list)):
		each_p_list[i] = int(each_p_list[i])
	average_list.append(sum(each_p_list)/len(each_p_list))
print(average_list[0:10])

first_10_av = (sum(average_list[0:10])/10)
print("average of first 10 is", first_10_av,"\n")


## Exercise 3  ###############################
# Using the average flare-ups per day calculated in part 2, print the highest and lowest average number of flare-ups per day.
print("exercise3\n")
print(max(average_list))
print(min(average_list),"\n")


## Exercise 4  ###############################
# or each day, print the difference in number of flare-ups between patients 1 and 5.
print("exercise4\n")
patient1_ary = data_ary[0].split(",")
patient5_ary = data_ary[4].split(",")
for k in range(len(patient1_ary)):
	difference = int(patient1_ary[k]) - int(patient5_ary[k])
	print("day " + str(k) + " " + "difference is " + str(difference))

# close document
f.close()