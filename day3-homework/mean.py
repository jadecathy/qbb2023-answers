#!/usr/bin/env python

test_list = [1,3,5,7,9,11,13,15]

def my_mean(nums):
	mean_ = sum(nums)/len(nums)
	return mean_

print(my_mean(test_list))