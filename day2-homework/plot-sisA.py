#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
row = 0
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest
cols1 = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols1.append(i)
cols2 = []
for i in range(len(samples)):
    if "female" not in samples[i]:
        cols2.append(i)
# print(cols1)
# print(cols2)

# Subset data of interest
expression_f = data[row, cols1]
expression_m = data[row, cols2]

# Prepare data
x = ["10","11","12","13","14A","14B","14C","14D"]
y1 = expression_f
y2 = expression_m
print(type(y2))
y3 = 2 * np.array(expression_m)

# Plot female data
fig1, ax = plt.subplots()
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance(RPKM)")
ax.set_title( "sisA(FBtr0073461) female" )
plt.plot(x,y1)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()
fig1.savefig( "sisA(FBtr0073461)_female.png" )
plt.close( fig1 )

# plot female + male data
fig2, ax = plt.subplots()
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance(RPKM)")
ax.set_title( "sisA(FBtr0073461)" )
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(["Female", "Male"])
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()
fig2.savefig( "sisA(FBtr0073461)_female+male.png" )
plt.close( fig2 )

# Plot female + male + 2* female data
fig3, ax = plt.subplots()
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance(RPKM)")
ax.set_title( "sisA(FBtr0073461)" )
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.legend(["Female", "Male", "2* Male"])
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()
fig3.savefig( "sisA(FBtr0073461)_all.png" )
plt.close( fig3 )