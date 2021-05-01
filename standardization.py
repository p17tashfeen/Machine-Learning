# -*- coding: utf-8 -*-
"""
Created on Fri May 15 04:00:21 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

#Get features for scaling 
features = corpus.iloc[:, [2, 3, 4, 5]].values

#Manually handling missing value
features[0][2] = 0
print('\nFeatures\n')
print(features)

#normalize features using Standard Scaler
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
normalized_features = ss.fit_transform(features)

print('\nStandardized Features\n')
import numpy as np
np.set_printoptions(suppress = True)
print(normalized_features)