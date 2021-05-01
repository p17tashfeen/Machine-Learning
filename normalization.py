# -*- coding: utf-8 -*-
"""
Created on Fri May 15 03:43:46 2020

@author: Dr. Taimoor
"""

import pandas as pd
corpus = pd.read_csv('D:\\Dataset.csv')
print(corpus)

#Get features for scaling with normalization or min-max scaler
features = corpus.iloc[:, [2, 3, 4, 5]].values

#Manually handling missing value
features[0][2] = 0
print('\nFeatures\n')
print(features)

#normalize features using minmaxscaler
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
normalized_features = mms.fit_transform(features)

print('\nNormalized Features\n')
import numpy as np
np.set_printoptions(suppress = True)
print(normalized_features)