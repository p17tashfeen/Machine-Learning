# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:32:30 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

#Mode

cities = corpus.iloc[: , 1].values
print(cities)

print('\n total cities', len(set(cities))

#finding mode
from scipy import stats             #install scipy first using !pip install scipy
mode = stats.mode(cities)[0][0]
print('\n Mode of Cities', mode)

new_cities = []
for city in cities:
    if city == '?':
        new_cities.append(mode)
    else:
        new_cities.append(city)
        
print('\n New Cities', new_cities)