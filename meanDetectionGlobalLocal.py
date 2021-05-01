# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:28:18 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

price = corpus.iloc[: , 3].values

print('\nPrice', price)

import numpy as np

#---------------------------Global Detection
mean = np.mean(price)
std = np.std(price)

print('\nMean & Standard Deviation', mean, std)

cutoff = std * 3 # k = 3
lower, upper = mean - cutoff, mean + cutoff
print('\nLower, Upper', lower, upper)

print('\nNoise Values in Global Context...')
for p in price:
    if p < lower or p > upper:
        print(p)

#-------------------------Local Detection (with Yes Context)        
yes_price = corpus[corpus['Transaction'] == 'yes'].iloc[: ,3].values
print('\nYes Price', yes_price)

yes_mean = np.mean(yes_price)
yes_std = np.std(yes_price)

yes_cutoff = yes_std * 3 # k = 3

yes_lower, yes_upper = yes_mean - yes_cutoff, yes_mean + yes_cutoff
print('\nYes Lower, Yes Upper', yes_lower, yes_upper)

print('\nNoise Values in Local (Yes) Context...')
for py in yes_price:
    if py < yes_lower or py > yes_upper:
        print(py)
        
#---------------------------Local Detection (with No Context)    
no_price = corpus[corpus['Transaction'] == 'no'].iloc[: ,3].values
print('\nNo Price', no_price)

no_mean = np.mean(no_price)
no_std = np.std(no_price)

no_cutoff = no_std * 3 # k = 3

no_lower, no_upper = no_mean - no_cutoff, no_mean + no_cutoff
print('\nNo Lower, No Upper', no_lower, no_upper)

print('\nNoise Values in Local (No) Context...')
for pn in no_price:
    if pn < no_lower or pn > no_upper:
        print(pn)
        