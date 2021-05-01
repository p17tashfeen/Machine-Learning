# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:58:46 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv').values

# raw data
print(corpus)

# detect missing values in the data
print('\nThe records with missing values...')
symbols = ['?', '*', '#', 'Nan']
for row in corpus:
    if set(row) & set(symbols):
        print(row)
        