#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

# # Read the 10x dataset filtered down to just the highly-variable genes
# adata = sc.read_h5ad("livecoding/variable_data.h5")
# adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 


# ## computing a neighbour graph
# sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

# ## leiden clustering
# sc.tl.leiden(adata)


# ## visaulizing clusters
# fig1, ax = plt.subplots(1,2)
# sc.tl.umap(adata, maxiter = 900)
# sc.pl.umap(adata, color ='leiden', title = 'umap', ax = ax[0], show = False)
# sc.tl.tsne(adata)
# sc.pl.tsne(adata, color ='leiden', title = 't-sne', ax = ax[1])
# plt.tight_layout()
# fig1.savefig('cluster.png')
# plt.close()


# ## ranking genes in clusters
# wilcoxon_adata = sc.tl.rank_genes_groups(adata, groupby='leiden', method='wilcoxon', use_raw=True, copy=True)
# logreg_adata = sc.tl.rank_genes_groups(adata, groupby='leiden', method='logreg', use_raw=True, copy=True)

# ## visualizing marker genes
# sc.pl.rank_genes_groups(wilcoxon_adata, n_genes=25, title = 'wilcoxon', show = False, sharey=False, use_raw=True, save='_wilcoxon.png')
# sc.pl.rank_genes_groups(logreg_adata, n_genes=25, title = 'logreg', show = False, sharey=False, use_raw=True, save='_logreg.png')


##  IDENTIFYING CLUSTER CELL TYPES
# reload data

# leiden = adata.obs['leiden']
# umap = adata.obsm['X_umap']
# tsne = adata.obsm['X_tsne']

# adata = sc.read_h5ad('filtered_data.h5')
# adata.obs['leiden'] = leiden
# adata.obsm['X_umap'] = umap
# adata.obsm['X_tsne'] = tsne

# adata.write('filtered_clustered_data.h5')
adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

fig, ax = plt.subplots(2,2)
sc.pl.umap(adata, color ='LYZ', ax = ax[0, 0], show = False)
sc.pl.umap(adata, color ='IL7R', ax = ax[0, 1], show = False)
sc.pl.umap(adata, color ='LST1', ax = ax[1, 0], show = False)
sc.pl.umap(adata, color ='NKG7', ax = ax[1, 1], show = False)
fig.savefig('matching.png')
plt.close()

adata.rename_categories('leiden', ['CD4 T', 'CD14 Monocytes', '3', '4', '5', 'NK', '7','8'])
sc.pl.umap(adata, color='leiden', legend_loc='right margin', title='matched umap of cell types', show = False,save='_overall.png')