# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:21:36 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

#median for imputation
items = corpus.iloc[:, 2].values
print(items)

import numpy as np
median = np.median(items)
print('\n median \n', median)

def isNoiseValue(x):
    if x > 1000:
        return True
    
#Handling noise values with imputation through median    
new_items = []
for item in items:
    if isNoiseValue(item):
        new_items.append(median)
    else:
        new_items.append(item)
print('\n New items \n', new_items)

#Imputation can also be applied with a local context
# In which case only the median of the local context i.e., values of a single label
# can be used for finding the median value (one for each local context)

#The values detected as noise will be replaced with the median of their respective local context