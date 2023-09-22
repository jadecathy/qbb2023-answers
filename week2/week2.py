#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

#==============#
#  Exercise 1  #
#==============#

def simulate_coverage(coverage, genome_length, read_length, figname):
	
	# initialize
	coverage_arr = np.zeros(genome_length)
	num_reads = int(coverage * genome_length / read_length)

	# random simulation
	ran_start = 0
	ran_end = genome_length - read_length
	start_positions = np.random.randint(low = ran_start, high = ran_end +1, size = num_reads)

	for start in start_positions:
		coverage_arr[start:start+read_length] += 1

	sim_0cov = genome_length - np.count_nonzero(coverage_arr)
	sim_0cov_pct = 100 * sim_0cov / genome_length
	print(f'in the simulation, there are {sim_0cov} bases with 0')
	print(f'There are {sim_0cov_pct} % of the genome')
	

	x = np.arange(0, max(coverage_arr)+1)

	# Get poisson distribution
	y_possion = poisson.pmf(x, mu = coverage) * genome_length

	# Get normal distribution


	#make fig
	fig, ax = plt.subplots()
	ax.hist(coverage_arr, bins = x, alpha = .5, label='simulation')
	ax.plot(x, y_possion, label='poisson')
	ax.set_xlabel('Coverage')
	ax.set_ylabel('Frequency(bp)')
	plt.tight_layout()
	fig.savefig(figname)

simulate_coverage(3, 1000_000, 100, 'tmp.png')




