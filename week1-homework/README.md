###### Exersise 2.2
1. What is the “size” of this relationship? In your own words, what does this mean? Does this match what you observed in your plots in step 2.1?
- Answer: The "size" of relationship refers to the co-efficient between mother age and mother_DNM, which is 0.3776 in this case. It means for each year mother_age increases, the mean of mother_DMN is likely to go up by a factor of 0.3776. Yes it matches my observation. in the scatter plot, I can see the general trend that mother_DMN increases as the mother_age increases.

2. Is this relationship significant? How do you know?
- Answer: the relationship is significant. The P value is 6.878208e-24, much smaller than 0.05.


###### Exersise 2.3
1. Answer: The "size" of relationship refers to the co-efficient between father age and father_DNM, which is 1.3538 in this case. It means for each year mother_age increases, the mean of mother_DMN is likely to go up by a factor of 01.3538. Yes it matches my observation. in the scatter plot, I can see the general trend that mother_DMN increases as the mother_age increases.

2. Answer: the relationship is very significant. The P value is 1.552294e-84, much smaller than 0.05 (nearly 0).


###### Exercise 2.4
- Answer: The answer i got is 78.6932. 
I have two ways to get the answer. First is to use the summary of the fit model to come up with the equation: father_DNM = 1.3538 * father_age +10.3263, and do then take father_age = 50.5; Second is to use the built-in prediction method in smf.


###### Exercise 2.6
1. What statistical test did you choose? Why?
- Answer: I chose paired sample t test. Because here we have two paired sets of data taken from each individuals, our null hypothesis is that the mean of mother_DNM and father_DNM are identical per proband. And specifically wilcoxin as a non-parametric paired t-test. 

2. Was your test result statistically significant? Interpret your result as it relates to the number of paternally and maternally inherited DNMs.
- Answer: Yes, because the p value is 1.196072299459786e-66, much smaller than 0.05 and enough to reject the null hypothesis. Therefore, we can say that the number of paternally and maternally inherited DNMs are significantly different in each proband. 


