#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ############# Exercise 1.2 ####################

# # Load data and the top 2 PCs
# pcs = np.loadtxt("pca.eigenvec", usecols=(2, 3))
# # print(pcs)

# # Create scatter plot.
# plt.subplots()
# plt.scatter(pcs[:, 0], pcs[:, 1], color='b', marker='o', alpha=0.5)
# plt.title("PCA visualization")
# plt.xlabel("Principal Component 1")
# plt.ylabel("Principal Component 2")
# plt.savefig("genotype_pca_plot.png")
# # plt.show()
# plt.close()


# ############# Exercise 2.2 ####################
# # load AF
# allele_frequencies = np.loadtxt("allele_frequencies.frq", skiprows=1, usecols=4)

# # plot allele frequencies.
# plt.subplots()
# plt.hist(allele_frequencies, bins = 50, color='b', edgecolor='black', alpha=0.7)
# plt.title("Allele Frequency Spectrum")
# plt.xlabel("Allele Frequency")
# plt.ylabel("Count")
# plt.savefig("allele_frequency_spectrum.png")
# # plt.show()
# plt.close()

############# Exercise 3.2 ####################

# Load GWAS results
gwas_results_CB1908 = pd.read_csv('CB1908_gwas_results.assoc.linear', delim_whitespace=True)
gwas_results_GS451 = pd.read_csv('GS451_IC50_gwas_results.assoc.linear', delim_whitespace=True)
# print(gwas_results_GS451.head())

# Define p-value threshold
p_value_threshold = 1e-5

# Function to plot Manhattan plot and highlight significant SNPs.
def plot_manhattan(data, title):
    fig,ax = plt.subplots()
    plt.scatter(data['BP'], -np.log10(data['P']), color ='blue', alpha=0.5)
    plt.axhline(-np.log10(p_value_threshold), color ='red', linestyle='--', label=p_value_threshold)
    significant_snps = data[data['P'] < p_value_threshold]
    plt.scatter(significant_snps['BP'], -np.log10(significant_snps['P']), color ='red', label='p < 1e-5')
    ax.set_xlabel('Position')
    ax.set_ylabel('-log10(p-value)')
    ax.set_title(title)
    fig.savefig(title)
    plt.close()

# print(gwas_results_CB1908.index)
# print(gwas_results_CB1908.columns)

# fig1 = plot_manhattan(gwas_results_CB1908, 'GWAS Results CB1908')
# fig2 = plot_manhattan(gwas_results_GS451, 'GWAS Results GS451')


############# Exercise 3.3 ####################
# I chose GS451



# Find the SNP with the lowest p-value associated with the chosen trait
top_snp = gwas_results_GS451.nsmallest(1, 'P')['SNP'].values[0]
top_snp2 = gwas_results_CB1908.nsmallest(1, 'P')['SNP'].values[0]
# print(gwas_results_GS451.head())
# print(top_snp)



# Filter data for the top SNP
filtered_data = gwas_results_GS451.loc[gwas_results_GS451['SNP'] == top_snp]
filtered_data2 = gwas_results_CB1908.loc[gwas_results_GS451['SNP'] == top_snp]
print(filtered_data2.head())
