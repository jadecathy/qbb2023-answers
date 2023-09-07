#!/usr/bin/env python

import sys 
patient1_id = 1
patient2_id = 10

fname = sys.argv[1]
f = open(fname).readlines()

def mean_patient(patient_id):
	calc_list =[]
	allday_list = f[patient_id-1].rstrip("\n").rsplit(",")
	for i in allday_list:
		calc_list.append(float(i))
	mean_ = sum(calc_list)/len(calc_list)
	return mean_

print(mean_patient(patient1_id))
print(mean_patient(patient2_id))