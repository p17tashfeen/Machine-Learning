# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:42:34 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

#---------------------------Global Context
prices = corpus.iloc[:, 3].values
print('\nPrices', prices)

from scipy import stats

zscores = stats.zscore(prices)
print('\n Zscores', zscores)

lower, upper = -3, 3 # k = 3
print('\n Lower, Upper', lower ,upper)

print('\n Noise Values are...')
for zscore in zscores:
    if zscore < lower or zscore > upper:
        print(zscore)

#-------------------------Local Context (Yes)
yes_prices = corpus[corpus['Transaction'] == 'yes'].iloc[:, 3]
print('\n Yes Prices', yes_prices)

yes_zscores = stats.zscore(yes_prices)
print('\n Yes Zscores', yes_zscores)

yes_lower, yes_upper = -3, 3 # k = 3
print('\n Yes lower, Yes upper', yes_lower, yes_upper)

print('\nNoise Values with Yes Context are...')
for yzscore in yes_zscores:
    if yzscore < yes_lower or yzscore > yes_upper:
        print(yzscore)

#--------------------------Do for Context No the same way        