# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:15:02 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')

print(corpus)

items  = corpus.iloc[:, 2]
print('\n')
print(items)

import numpy as np
median = np.median(items)
print('\n Global Median is, ', median)

cutoff = median * 3 # k [1, 4], k = 3

lower, upper = median - cutoff, median + cutoff

print('lower & upper', lower, upper)

for item in items:
    if item < lower or item > upper:
        print(item)