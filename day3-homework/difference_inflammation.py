#!/usr/bin/env python

import sys 
patient1_id = 10
patient2_id = 22

fname = sys.argv[1]
f = open(fname).readlines()

diff_list =[]

def diff_patient_mean(pID1 = 1 , pID2 = 1):
	allday_list_1 = f[pID1-1].rstrip("\n").rsplit(",")
	allday_list_2 = f[pID2-1].rstrip("\n").rsplit(",")
	for i in range(len(allday_list_1)):
		diff_list.append(float(allday_list_1[i])-float(allday_list_2[i]))
	return diff_list

print(diff_patient_mean(patient1_id,patient2_id))