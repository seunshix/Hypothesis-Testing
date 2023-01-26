# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_1samp, ttest_ind
# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# print(lifespans.head())

# Q1. Does Familiar's most basic package 'Vein pack' have a significant impact on subscribers
# life expectancy

vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']

# print(np.mean(vein_pack_lifespans)) #Output: 76.17
# the average life expectancy is greater than 73 years

ttest, pval = ttest_1samp(vein_pack_lifespans, 73)
# print(pval) # Output: 5.972157921433082e-07

# The pval is lower than the significance threshold we set at 0.05
# Therefore, we can conclude the average lifespan of Vein Pack subscribers is 
# significantly different from 73 years

# Q2. Does Familiar's 'Artery pack' have a significant impact on subscribers
# life expectancy
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']

# print(np.mean(artery_pack_lifespans)) #Output: 74.87
# the average life expectancy for the artery pack is shorter than the vein pack's average

ttest, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(pval) # 0.056

# The pval is larger than the significance threshold we set at 0.05
# Therefore, we can conclude that the average lifespan of Vein Pack 
# subscribers is not significantly differen from the average lifespan 
# of an Artery Pack subscriber


# Side Effects

# print(iron.head())

# is there an association between the pack that a subscriber gets and their iron level?
xtab = pd.crosstab(iron.pack, iron.iron)
print(xtab) # looks like Artery Pack subscribers tend to have high iron while Vein Pack subscribers have low iron

# chi contigency test
chi2, pval, dof, exp = chi2_contingency(xtab)
print(pval)

# The pval is lower that the significance threshold we set at 0.05.
# Therefore, we can conclude there is a significant association between pack and iron level.


