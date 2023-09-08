#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


# Get a starting frequency and a population size 
# Input parameters for function


## writing the simulation function
def pesudo_evolution(al_freq, pplt_size):
	i = 0
	while al_freq < 1 and al_freq > 0:
		nppp = np.random.binomial(2*pplt_size, al_freq)
		al_freq = nppp/(2*pplt_size)
		freq_hist_list.append(al_freq)
		i += 1
		count_generation_list.append(i)
	return freq_hist_list


fig, (ax1,ax2) = plt.subplots(1,2)

## generate the multiple population size

for k in range(200):
	freq_hist_list = []
	count_generation_list = []  # defining the variables needed
	allele_starting_freq = 0.3
	population_size_list = []
	time_to_fixation_list1 = []

	population_size = np.random.uniform(100,10000)
	num_generation = len(pesudo_evolution(allele_starting_freq, population_size))

	population_size_list.append(population_size)
	time_to_fixation_list1.append(num_generation)

	# plotting!
	ax1.scatter(population_size_list, time_to_fixation_list1)

ax1.set_ylim(0,50000)
ax1.set_xlabel("population size")
ax1.set_ylabel("time to fixation")
ax1.set_title("population size vs num_generation")


# generate multiple 


for k in range(10):
	freq_hist_list = []
	count_generation_list = []
	population_size = 1000
	time_to_fixation_list2 = []

	allele_starting_freq_list = []
	allele_starting_freq = np.random.uniform(0,1)
	allele_starting_freq_list.append(allele_starting_freq)

	num_generation = len(pesudo_evolution(allele_starting_freq, population_size))
	time_to_fixation_list2.append(num_generation)
	ax2.scatter(allele_starting_freq_list,time_to_fixation_list2)


ax2.set_xlabel("allele_starting_freq")
ax2.set_ylabel("time to fixation")
ax2.set_title("allele_starting_freq vs num_generation")

fig.tight_layout()
fig.savefig( "exercise3.png" )
plt.show()
