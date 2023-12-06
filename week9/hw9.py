#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt


## formatting the files
# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalization
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

counts_df_normed = np.log2(counts_df_normed + 1)

full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

# print(full_design_df.head(20))

# # running the regression
# model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
# results = model.fit()
# slope = results.params[1]
# pval = results.pvalues[1]
# print(results)
# print(slope)
# print(pval)

# slopes_lst = []
# pval_lst = []
# for every_col in list(full_design_df.columns.values)[:-3]:
# 	model = smf.ols(formula = 'Q(every_col) ~ SEX', data=full_design_df)
# 	results = model.fit()
# 	slope = results.params[1]
# 	pval = results.pvalues[1]
# 	slopes_lst.append(slope)
# 	pval_lst.append(pval)

# output = pd.DataFrame({'gene':list(full_design_df.columns.values)[:-3],
# 	'slope': slopes_lst,
# 	'pval': pval_lst
# 	})

# output.to_csv('output.txt')

# ## FDR correction
# output = pd.read_csv('output.txt')
# FDR_test = multitest.fdrcorrection(output['pval'], alpha=0.1, method='indep', is_sorted=False)[0]
# # print(FDR_test)

# # print(sum(FDR_test[0]))
# significant_df = output.loc[FDR_test]
# print(significant_df.head())
# significant_df['gene'].to_csv('gene_o_i.txt')


## deseq

# dds = DeseqDataSet(
#     counts=counts_df,
#     metadata=metadata,
#     design_factors="SEX",
#     n_cpus=4,
# )

# dds.deseq2()
# stat_res = DeseqStats(dds)
# stat_res.summary()
# results = stat_res.results_df

# results.to_csv('deseq_results.txt')
# gene_o_i_deseq = results.loc[results['padj']< 0.1]
# gene_o_i_deseq.to_csv('gene_o_i_deseq.txt')



# ## compare
# ols = list(pd.read_csv('gene_o_i.txt')['gene'])
# deseq = list(pd.read_csv('gene_o_i_deseq.txt')['Unnamed: 0'])
# ols_set = set(ols)
# deseq_set = set(deseq)
# print(ols_set)
# print(deseq_set)
# print('intesection:', len(ols_set.intersection(deseq_set)))
# print('union:', len(ols_set.union(deseq_set)))
# print('percentage:', len(ols_set.intersection(deseq_set))/len(ols_set.union(deseq_set)))


## plotting
df = pd.read_csv('gene_o_i_deseq.txt')
print(df.head())
real_important = df.loc[ (abs(df['log2FoldChange']) > 1) & (df['padj'] < 0.1) ]
fig, ax = plt.subplots()
log_padj_all = - np.log10(df['padj'] + 1e-300)
log_padj_sub = - np.log10(real_important['padj'] + 1e-300)
ax.scatter(df['log2FoldChange'],log_padj_all)
ax.scatter(real_important['log2FoldChange'],log_padj_sub, color = 'r')
ax.set_xlabel('gene expression difference')
ax.set_ylabel('p_val')
ax.set_title(' Differential expression between male and female')
plt.tight_layout()
fig.savefig('thankyouTA.png')



