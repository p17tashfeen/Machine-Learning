# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:34:43 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

data = corpus.iloc[: , 2 : 6].values

data[0][2] = 0  #hard coded imputation of missing value of payment in first record
print(data)

from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors = 2)
print(lof)

result = lof.fit_predict(data)

print('\n Multivariate Outliers (Records) labeled with -1', result)