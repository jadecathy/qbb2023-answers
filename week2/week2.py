#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import norm
import sys

#==============#
#  Exercise 1  #
#==============#

# def simulate_coverage(coverage, genome_length, read_length, figname):
	
# 	# initialize
# 	coverage_arr = np.zeros(genome_length)
# 	num_reads = int(coverage * genome_length / read_length)

# 	# random simulation
# 	ran_start = 0
# 	ran_end = genome_length - read_length
# 	start_positions = np.random.randint(low = ran_start, high = ran_end +1, size = num_reads)

# 	for start in start_positions:
# 		coverage_arr[start:start+read_length] += 1

# 	sim_0cov = genome_length - np.count_nonzero(coverage_arr)
# 	sim_0cov_pct = 100 * sim_0cov / genome_length
# 	print(f'in the simulation, there are {sim_0cov} bases with 0')
# 	print(f'{sim_0cov_pct} % of the genome has not been covered.')
	

# 	x = np.arange(0, max(coverage_arr)+1)

# 	# Get poisson distribution
# 	y_possion = poisson.pmf(x, mu = coverage) * genome_length

# 	# Get normal distribution
# 	y_norm = norm.pdf(x, coverage, np.sqrt(coverage)) * genome_length

# 	#make fig
# 	fig, ax = plt.subplots()
# 	ax.hist(coverage_arr, bins = x, alpha = .5, label='simulation')
# 	ax.plot(x, y_possion, label='poisson')
# 	ax.plot(x, y_norm, label='normal')
# 	ax.set_xlabel('Coverage')
# 	ax.set_ylabel('Frequency(bp)')
# 	ax.set_title('simulation of sequencing')
# 	ax.legend()
# 	plt.tight_layout()
# 	plt.show()
# 	fig.savefig(figname)

# simulate_coverage(3, 1000_000, 100, 'ex1_3x_cov.png')
# simulate_coverage(10, 1000_000, 100, 'ex1_10x_cov.png')
# simulate_coverage(10, 1000_000, 180, 'ex1_30x_cov.png')


#==============#
#  Exercise 2  #
#==============#

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

graph = set()
k_mer = 3

for read in reads:
	generation_kmer = []
	for i in range(len(read) - k_mer):
		kmer1 = read[i: i+k_mer]
		kmer2 = read[i+1: i+1+k_mer]
		graph.add(kmer1 + ' -> ' + kmer2)

for edge in graph:
	print(edge)

sys.stdout = open('log.txt', 'w')
sys.stdout.write('digraph{\n')
for edge in graph:
	sys.stdout.write(edge + '\n')
sys.stdout.write('}\n')



