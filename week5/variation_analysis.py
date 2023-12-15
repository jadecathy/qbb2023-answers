#!/usr/bin/env python

import sys 
import matplotlib.pyplot as plt

# looking at the VCF
# i=0
# for line in open('annotated.vcf'):
#     if line.startswith('#'):
#         continue
#     fields = line.rstrip('\n').split('\t')
#     while i< 10:
#         print(fields,'\n','\n')
#         print(len(fields))
#         i += 1

# parsing the VCF
read_depth = []
GQ = []
AF = []
for line in open('annotated.vcf'):
	if line.startswith('#'):
		continue
	fields = line.rstrip('\n').split('\t')
	for thing in fields[9:]:
		# print(thing)
		if thing.split(':')[2] != '.':
			read_depth.append(float(thing.split(':')[2]))
	for thing in fields[9:]:
		# print(thing)
		if thing.split(':')[2] != '.':
			GQ.append(float(thing.split(':')[1]))
	if ',' not in fields[7].split(';')[3]:
		AF.append(float(fields[7].split(';')[3][3:]))
	else:
		AF.append(float(fields[7].split(';')[3][3:].split(',')[0]))
		AF.append(float(fields[7].split(';')[3][3:].split(',')[1]))
	# for thing in fields
# print(read_depth)

fig1, ax1 = plt.subplots()
ax1.hist(read_depth, bins = [0,1,2,3,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50])
ax1.set_xlabel('read depth')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution of read depth at each variant across all sample')
plt.tight_layout()
fig1.savefig('3-1.png')

fig2, ax2 = plt.subplots()
ax2.hist(GQ)
ax2.set_xlabel('Genotyping quality')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of genotyping quality at each variant across all samples')
plt.tight_layout()
fig2.savefig('3-2.png')

fig3, ax3 = plt.subplots()
ax3.hist(AF)
ax3.set_xlabel('allele frequency')
ax3.set_ylabel('Frequency')
ax3.set_title('Distribution of genotyping quality at each variant across all samples')
plt.tight_layout()
fig3.savefig('3-3.png')

