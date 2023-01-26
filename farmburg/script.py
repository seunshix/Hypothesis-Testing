# Import libraries
import codecademylib3
import pandas as pd
import numpy as np

from scipy.stats import chi2_contingency, binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')
print(abdata.head())
print()

xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(xtab)
print()

# Group A has the highest number of purchases 

chi2, pval, dof, expected = chi2_contingency(xtab)
print(pval)
print()

# The pval is less than the significance threshold.
# Therefore we can conclude that there is a significant 
# difference in the purchase rate for groups A, B, C.

num_visits = len(abdata)
# print(num_visits) # Output: 4998

num_sales_needed_099 = 1000/0.99
p_sales_needed_099 = num_sales_needed_099/num_visits
print(f'To sell the package at 0.99, FarmBurg will need {np.ceil(num_sales_needed_099)} sales and the proportion of sales needed will be {p_sales_needed_099:.2f}')

num_sales_needed_199 = 1000/1.99
p_sales_needed_199 = num_sales_needed_199/num_visits
print(f'To sell the package at 1.99, FarmBurg will need {np.ceil(num_sales_needed_199)} sales and the proportion of sales needed will be {p_sales_needed_199:.2f}')


num_sales_needed_499 = 1000/4.99
p_sales_needed_499 = num_sales_needed_499/num_visits
print(f'To sell the package at 4.99, FarmBurg will need {np.ceil(num_sales_needed_499)} sales and the proportion of sales needed will be {p_sales_needed_499:.2f}')

samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

samp_size_499 = np.sum(abdata.group == 'B')
sales_499 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

pvalA = binom_test(sales_099, samp_size_099, p_sales_needed_099, alternative = 'greater')
print(f'The pval for Group A is {pvalA}')

pvalB = binom_test(sales_199, samp_size_199, p_sales_needed_199, alternative = 'greater')
print(f'The pval for Group B is {pvalB}')

pvalC = binom_test(sales_499, samp_size_499, p_sales_needed_499, alternative = 'greater')
print(f'The pval for Group C is {pvalC}')

# The Group C pval is below the threshold of 0.05. Therefore the C group is the only group
# we can conclude that the purchase rate is significantly higher than the target needed 
# to reach $1000 revenue per week. Therefore Brian should charge $4.99 for the upgrade.