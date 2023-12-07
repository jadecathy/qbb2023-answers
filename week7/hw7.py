#!/usr/bin/env python

import sys 
import matplotlib.pyplot as plt
import numpy as np


bis, ont, bis_normal, bis_tumor, ont_normal, ont_tumor, out_fname = sys.argv[1:8]
# command line: ./hw7.py bisulfite.cpg.chr2.bedgraph ONT.cpg.chr2.bedgraph normal.bisulfite.chr2.bedgraph
# tumor.bisulfite.chr2.bedgraph normal.ONT.chr2.bedgraph tumor.ONT.chr2.bedgraph OOTD

def load_data(fname):
    data = []
    met_score = {}
    cov = {}
    for line in open(fname):
        line = line.rstrip().split()
        data.append([
            line[0], float(line[1]),float(line[3]),int(line[4])])
        met_score[float(line[1])]= float(line[3])
        cov[float(line[1])] = int(line[4])
    return data, met_score, cov


def compare_two(fname1, fname2):

	# Load data from files
	data1 = load_data(fname1)[0]
	data2 = load_data(fname2)[0]
	# print(data1[0:10])
	# print(data2[0:10])

	# Find reads that appear more than once in datasets
	data1_set = set()
	for i in range(len(data1)):
		if data1[i][1] not in data1_set:
			data1_set.add(data1[i][1])

	data2_set = set()
	for i in range(len(data2)):
		if data2[i][1] not in data2_set:
			data2_set.add(data2[i][1])

	data1_diff = data1_set.difference(data2_set)
	data2_diff = data2_set.difference(data1_set)
	data_shared = data1_set - data1_diff

	# print(len(data1_set), len(data2_set), len(data_1diff))

	# Print statistics about unique vs multimapping reads
	print(f"{fname1} unique reads: ({len(data1_diff) / (len(data1_diff) + len(data2_set))  * 100}) %")
	print(f"{fname2} unique reads: ({len(data2_diff) / (len(data2_diff) + len(data1_set)) * 100}) %")
	print(f"shared reads: ({(len(data1) - len(data1_diff)) / (len(data2_diff) + len(data1_set)) * 100}) %")

	return data1, data2, data_shared   # data1,2 : everything in it


fig, ax = plt.subplots(2, 2, figsize=(9,9))


# create coverage histogram
bis_data, ont_data, bis_ont_shared_data = compare_two(bis, ont)
bis_cov =[]
ont_cov =[]
for i in bis_data:
	bis_cov.append(i[3])
for i in ont_data:
	ont_cov.append(i[3])
x_lst =[]
for i in range(50):
	x_lst.append(i * 2)
ax[0,0].hist(bis_cov, bins = x_lst, alpha = 0.3, color = 'r')
ax[0,0].hist(ont_cov, bins = x_lst, alpha = 0.3, color = 'b')
ax[0,0].set_xlabel('coverage')
ax[0,0].set_ylabel('counts')
ax[0,0].legend(['Bisulfite', 'Nanopore'])
ax[0,0].set_title('Distribution Of Coverage')


# create relationship between methylation scores
bis_metscore = load_data(bis)[1]
ont_metscore = load_data(ont)[1]
bis_score = []
ont_score = []
for every in bis_ont_shared_data:
	bis_score.append(bis_metscore[every])
	ont_score.append(ont_metscore[every])
# print(type(bis_score))
bis_score_log = np.log10(np.array(bis_score)+1)
ont_score_log = np.log10(np.array(ont_score)+1)
hist2D, x_edges, y_edges = np.histogram2d(bis_score_log, ont_score_log)
im = ax[0,1].imshow(hist2D)
cax = fig.add_axes([0.925, 0.51, 0.02, 0.35])  # [left, bottom, width, height]
cbar = fig.colorbar(im, cax=cax)
cbar.set_label('Methylation score(in log10)')
coef1 = float(np.corrcoef(bis_score, ont_score)[1,0])
print(coef1)
ax[0,1].set_xlabel('Methylation (Nanopore)')
ax[0,1].set_ylabel('Methylation (Bisulfite)')
ax[0,1].set_title(f'Bisulfite and Nanopore Met Score Pearson R: {coef1:.3f})')

# create violin plot
bis_normal_data, bis_tumor_data,bis_normal_tumor = compare_two(bis_normal, bis_tumor)
bis_normal_data_metscore = load_data(bis_normal)[1]
bis_tumor_data_metscore = load_data(bis_tumor)[1]
bis_score_change = []	
for every in bis_normal_tumor:
	if bis_normal_data_metscore[every] != bis_tumor_data_metscore[every]:
		bis_score_change.append(bis_tumor_data_metscore[every] - bis_normal_data_metscore[every])
# print(bis_score_change)
ax[1,0].violinplot(bis_score_change)
ax[1,0].set_xlabel('counts')
ax[1,0].set_ylabel('Methylation score change')
ax[1,0].set_title('Bisulfite Methylation Change')

ont_normal_data, ont_tumor_data, ont_normal_tumor = compare_two(ont_normal, ont_tumor)
ont_normal_data_metscore = load_data(ont_normal)[1]
ont_tumor_data_metscore = load_data(ont_tumor)[1]
ont_score_change = []	
for every in ont_normal_tumor:
	if ont_normal_data_metscore[every] != ont_tumor_data_metscore[every]:
		ont_score_change.append(ont_tumor_data_metscore[every] - ont_normal_data_metscore[every])
ax[1,1].violinplot(ont_score_change)
ax[1,1].set_xlabel('counts')
ax[1,1].set_ylabel('Methylation score change')
ax[1,1].set_title('Nanopore Methylation Change')


# calculate pearson corelation of methy score change
common_sites = ont_normal_tumor - ont_normal_tumor.difference(bis_normal_tumor)
bis_r = []
ont_r = []
for every in common_sites:
	bis_r.append(bis_tumor_data_metscore[every] - bis_normal_data_metscore[every])
	ont_r.append(ont_tumor_data_metscore[every] - ont_normal_data_metscore[every])
coef2 = float(np.corrcoef(bis_r,ont_r)[1,0])
print(np.corrcoef(bis_r,ont_r))
fig.suptitle(f'Pearson R: {coef2:.3f}', x=0.5, y=0.06, ha='center')

# plt.tight_layout()
plt.savefig(out_fname)

