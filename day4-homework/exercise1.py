#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get a starting frequency and a population size 
# Input parameters for function
allele_starting_freq = 0.1
population_size = 100


# Make a list to store our allele frequencies
freq_hist_list = []



# While our allele frequency is between 0 and 1:
# 	Get the new allele frequency for next generation by drawing from the binomial distribution
#	(convert number of successes into a frequency)
#	Store our allele frequency in the AF list
# Return a list of allele frequency at each time point

num_generation_list = []
def pesudo_evolution(al_freq, pplt_size):
	i = 0
	while al_freq < 1 and al_freq > 0:
		nppp = np.random.binomial(2*pplt_size, al_freq)
		al_freq = nppp/(2*pplt_size)
		freq_hist_list.append(al_freq)
		i += 1
		num_generation_list.append(i)
	return freq_hist_list

# Number of generations to fixation 
# is the length of your list

num_generation = len(pesudo_evolution(allele_starting_freq, population_size))
print(num_generation)

fig, ax = plt.subplots()
print(type(range(num_generation)))
ax.set_xlabel("generations")
ax.set_ylabel("frequency of the allele")
ax.set_title("Exercise1 trajectories")

plt.plot((num_generation_list),freq_hist_list)
fig.savefig('exercise1_trajectory.png')
plt.show()

