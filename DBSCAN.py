# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:40:26 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

data = corpus.iloc[:, [2, 3, 5]].values
print('\n Data', data)

from sklearn.cluster import DBSCAN

#You should know your number of desired clusters before hand
#Keep tuning these two parameters until you get those clusters
dbscan = DBSCAN(eps = 500, min_samples = 2)
print(dbscan)

#Cluster data
result = dbscan.fit_predict(data)

print('\n Multivariate Outliers labeled as -1', result)