#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt
import seaborn as sns

# # read in data
# counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# # read in metadata
# metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# # normalize
# counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# # log
# counts_df_logged = np.log2(counts_df_normed + 1)

# # merge with metadata
# full_design_df = pd.concat([counts_df_logged, metadata], axis=1)
# full_design_df.to_csv('full_design_df.csv', index=True)

full_design_df = pd.read_csv('full_design_df.csv', index_col = 0)
print(full_design_df.head())

# # 1.1

# GTEX113JC = full_design_df.loc[['GTEX-113JC']].iloc[:,:-3].transpose()
# # print(GTEX113JC.shape)
# fig1, ax1 = plt.subplots()
# ax1.hist(np.array(GTEX113JC),bins=20)
# ax1.set_xlabel('logged normalized counts')
# ax1.set_ylabel('Frequency')
# ax1.set_title('Distribution of gene expression in subject GTEX-113JC')
# plt.tight_layout()
# fig1.savefig('1-1')

# # 1.2
# df_m = np.array(full_design_df.loc[full_design_df['SEX'] == 1]['MXD4'])
# df_f = np.array(full_design_df.loc[full_design_df['SEX'] == 2]['MXD4'])
# # print(df_f.shape)
# fig2, ax2 = plt.subplots()
# ax2.hist(df_m, bins=20, color='b', alpha = 0.5)
# ax2.hist(df_f, bins=20, color='r', alpha = 0.5)
# ax2.set_xlabel('logged normalized counts')
# ax2.set_ylabel('Frequency')
# ax2.legend(['male','female'])
# ax2.set_title('Distribution of MXD4 in male vs female')
# plt.tight_layout()
# fig2.savefig('1-2.png')

# 1.3
# df_age = full_design_df['AGE']
# print(df_age)
# fig3, ax3 = plt.subplots()
# ax3.hist(df_age)
# ax3.set_xlabel('age')
# ax3.set_ylabel('Frequency')
# ax3.set_title('Distribution of subject age')
# plt.tight_layout()
# fig3.savefig('1-3.png')

# # 1.4
# plt.figure(figsize = (10,6))
# sns.violinplot(data= full_design_df, x='AGE', y='LPXN', hue='SEX', split = True)
# plt.title('Median LPXN Expression over Time Stratified by Sex')
# plt.xlabel('Age')
# plt.ylabel('Logged Normalized Counts')
# plt.savefig('1-4.png')
