#! /usr/bin/env python

import sys
fname = sys.argv[1]
f = open(fname).readlines()

my_integer_list = []
for wter in f:
	my_integer_list.append(float(wter.rstrip("\n")))

def my_mean(nums):
	mean_ = sum(nums)/len(nums)
	return mean_

print(my_mean(my_integer_list))

f.close()