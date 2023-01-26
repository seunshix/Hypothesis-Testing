# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test, chi2_contingency, f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Import data
dogs = pd.read_csv('dog_data.csv')

print(dogs.head())

whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']

num_whippet_rescues = np.sum(whippet_rescue)
print(num_whippet_rescues)

num_whippet = len(whippet_rescue)
print(num_whippet)

pval = binom_test(num_whippet_rescues, num_whippet, 0.08)
print(pval)

# The pval is above the significance threshold of 0.05
# Therefore, we can conclude the 8% of whippet population 
# are rescues

# Mid-Sized Dog Weights
wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']

fstat, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(pval)

# The pval is lower than the significance threshold of 0.05
# Therefore there is at least one pair of dog breeds that have
# significantly different average weights

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]
tukey_results = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed, 0.05)
print(tukey_results)

# pitbull and terrier weigh significantly different amounts
# terrier and whippet weigh significantly different amounts

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]
xtab = pd.crosstab(dogs_ps.breed, dogs_ps.color)
print(xtab)

chi2, pval, dof, exp = chi2_contingency(xtab)
print(pval)

# The pval is above the significance threshold
# Therefore we can conclude there is an association between breed and color
