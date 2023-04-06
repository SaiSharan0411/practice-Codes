# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:05:06 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
def most_common(lst):
    return (max(set(lst), key = lst.count))
def euclidean(point, data):         
    return np.sqrt(np.sum((point - data) ** 2, axis = 1))
class KNeighborsRegressor:
    def __init__(self, k = 5, dist_metric = euclidean):
        self.k = k
        self.dist_metric = dist_metric
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    def predict(self, X_test):   
      neighbors = []
      for x in X_test:
            distances = self.dist_metric(x, self.X_train)
            y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
            neighbors.append(y_sorted[:self.k])
            return np.mean(neighbors, axis = 1)
    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        ssre = sum((y_pred - y_test) ** 2)
        return ssre
housing = pd.read_csv('california_new.csv')
X = housing.iloc[0:500, 0:7]
y = housing.iloc[0:500, 8]
print(housing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
ss = StandardScaler().fit(X_train)
X_train, X_test = ss.transform(X_train), ss.transform(X_test)
accuracies = []
ks = range(1, 30)
for k in ks:
    knn = KNeighborsRegressor(k = k)
    knn.fit(X_train, y_train)
    accuracy = knn.evaluate(X_test, y_test)
    accuracies.append(accuracy)
fig, ax = plt.subplots()
ax.plot(ks, accuracies)
ax.set(xlabel = "k", ylabel = "SSRE", title = "Performance of knn")
plt.show()
