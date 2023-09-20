Exercise4  
Qi Wang

Plot1 and 2 – trajectories and histogram

First comment is on the trajectories I got from Exercise 2. I fixed the population size and the starting allele frequency, ran the Wright-Fisher Model over 1000 times and visualized each trial. In some of the trials the frequency eventually got to 1, which means that the allele was fixed. In others the allele disappeared within the population.

Second comment is on the histogram, also from exercise 2. The x axis refers to the time to fixation, and the y axis refers to the time to fixation. It looks similar to the poisson distribution, which makes perfect sense, as it describes the time it took to reach allele fixation/deletion for the population.


Assumption 1:

In the Wright-Fisher Model we assume that there is no natural selection. But in real-life scenario, some rare allele polymorphism (like CCR5 delta 32) actually exists. This would make no sense in the Wright-Fisher Model since the probability of success in a single trial is purely based on allele frequencies. If we want to simulate selection in our program, we might modify the p we use in the binomial trial and maybe put more weight on some resistant allele type.



