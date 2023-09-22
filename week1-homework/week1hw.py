#!/usr/bin/env python

import numpy as np
import pandas as pd 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon

############# Exercise 1 wrangle the data #####################
raw_df = pd.read_csv('aau1043_dnm.csv')
print(raw_df)


## cleaning up the data into dictionary
deNovoCount = {}
No_sample = raw_df.shape[0]

for i in range(No_sample):
	Id = int(raw_df.loc[i, 'Proband_id'])
# the id already exist
	try:
		a = deNovoCount[Id]
		if raw_df.loc[i , 'Phase_combined'] == 'mother':
			deNovoCount[Id][0] += 1
		elif raw_df.loc[i , 'Phase_combined'] == 'father':
			deNovoCount[Id][1] += 1
# first encounter of the id	
	except KeyError:
		if raw_df.loc[i , 'Phase_combined'] == 'mother':
			deNovoCount[Id] =[1, 0]
		elif raw_df.loc[i , 'Phase_combined'] == 'father':
			deNovoCount[Id] =[0, 1]
		# print(0, 'the Id is ' + Id)

# print(deNovoCount)


## converting into a dataframe
deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])
print(deNovoCountDF)

## loading the age data
age_df = pd.read_csv('aau1043_parental_age.csv', index_col = 'Proband_id')
# print(age_df)


## combining the 2 datasets
cmb_df = pd.concat([deNovoCountDF, age_df], axis = 1, join = 'inner')
print(cmb_df)



############# Exercise 2 Fit and interpret linear regression models with Python #####################

## plotting the figure
fig1, ax = plt.subplots()
ax.set_xlabel("maternal age(years)")
ax.set_ylabel("maternal de novo mutations")
ax.set_title( "Maternal DNM vs age")
plt.scatter(cmb_df['Mother_age'], cmb_df['maternal_dnm'])
plt.show()
fig1.savefig( "ex2_a.png" )
plt.close(fig1)

fig2, ax = plt.subplots()
ax.set_xlabel("paternal age(years)")
ax.set_ylabel("paternal de novo mutations")
ax.set_title( "Paternal DNM vs age")
plt.scatter(cmb_df['Father_age'], cmb_df['paternal_dnm'])
plt.show()
fig2.savefig( "ex2_b.png" )
plt.close(fig2)

## running the linear model on maternal
maternal_model = smf.ols(formula = 'maternal_dnm ~ 1 + Mother_age', data = cmb_df)
results1 = maternal_model.fit()
print(results1.summary())
print(results1.pvalues)

## running the linear model on paternal
paternal_model = smf.ols(formula = 'paternal_dnm ~ 1 + Father_age', data = cmb_df)
results2 = paternal_model.fit()
print(results2.summary())
print(results2.pvalues)

## predicting father_DNM
# father_predict = pd.DataFrame({"Father_age" : [50.5]})
# print(father_predict.shape)
# print(father_predict)
# print(paternal_model.predict(father_predict))


## difference between the number of maternally vs. paternally inherited DNMs per proband
print(wilcoxon(cmb_df['maternal_dnm'], cmb_df['paternal_dnm']))