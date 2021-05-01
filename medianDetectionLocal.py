# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:15:02 2020

@author: Dr. Taimoor
"""

import pandas as pd
import numpy as np
corpus = pd.read_csv('D:\\Dataset.csv')

print(corpus)

yes_items = corpus[corpus['Transaction'] == 'yes'].iloc[:, 2].values
no_items = corpus[corpus['Transaction'] == 'no'].iloc[:, 2].values

print('\n Yes Items', yes_items)
print('\n No Items', no_items)

#range of normality for the label yes
yes_median = np.median(yes_items)
yes_cutoff = yes_median * 3 # k = 3
yes_lower, yes_upper = yes_median - yes_cutoff, yes_median + yes_cutoff
print('\nYes lower, Yes upper', yes_lower, yes_upper)

# detecting noise values for yes label
print('\n Noise values with Yes context are...')
for item in yes_items:
    if item < yes_lower or item > yes_upper:
        print(item)


# range of normality for the label no
no_median = np.median(no_items)
no_cutoff = no_median * 3 # k = 3
no_lower, no_upper = no_median - no_cutoff, no_median + no_cutoff
print('\nNo lower, No upper', no_lower, no_upper)

#detecting noise values for no label
print('\n Noise values with No context are...')
for item in no_items:
    if item < no_lower or item > no_upper:
        print(item)
