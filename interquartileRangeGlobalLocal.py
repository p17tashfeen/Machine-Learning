# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:54:19 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

items = corpus.iloc[: , 2].values
print('\n Items', items)

import numpy as np

#------------------------------Global context
q25 = np.percentile(items, 25)
q50 = np.percentile(items, 50)
q75 = np.percentile(items, 75)

print('\n q25, q50, q75', q25, q50, q75)

iqr = q75 - q25
print('\niqr', iqr)

cutoff = iqr * 3 # k = 3
print('\nCutoff', cutoff)

lower, upper = q25 - cutoff, q75 + cutoff
print('\nLower, Upper', lower, upper)

print('\n Noise Values are...')
for item in items:
    if item < lower or item > upper:
        print(item)
        
#----------------------------- You may try for Local Context        