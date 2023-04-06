# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:26:10 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
data=pd.read_csv('book1.csv')
data
print(data.head())
plt.scatter(data['b'],data['c'])
plt.show()
x=data.iloc[:,1:3]
x
print(x)
kmeans=KMeans(3)
kmeans.fit(x)
identified_clusters=kmeans.fit_predict(x)
identified_custers
print(identified_clusters)
data_with_clusters=data.copy()
data_with_clusters['clusters']=identified_clusters
plt.scatter(data_with_clusters['b'],data_with_clusters['c'],c=data_with_clusters['clusters'],cmap='rainbow' )