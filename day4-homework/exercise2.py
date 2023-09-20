#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


# Get a starting frequency and a population size 
# Input parameters for function
allele_starting_freq = 0.3
population_size = 100


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


fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

## generate the trajectoies

for k in range(40):
	freq_hist_list = []
	count_generation_list = []
	num_generation = len(pesudo_evolution(allele_starting_freq, population_size))
	# print(num_generation)
	ax1.plot(count_generation_list,freq_hist_list)

ax1.set_xlabel("generations")
ax1.set_ylabel("frequency of the allele")
ax1.set_title("exercise2_trajectories")
fig1.savefig( "exercise2_trajectory.png" )


# visualize time to fixation

time_to_fixation_list = []

for k in range(1000):
	freq_hist_list = []
	count_generation_list = []
	num_generation = len(pesudo_evolution(allele_starting_freq, population_size))
	time_to_fixation_list.append(num_generation)
	# print(num_generation)
# print(time_to_fixation_list)
ax2.hist(time_to_fixation_list)
ax2.set_xlabel("time to fixation")
ax2.set_ylabel("frequencies")
ax2.set_title("exercise2_histogram")


fig2.savefig( "exercise2_Time To Fixation.png" )

plt.show()