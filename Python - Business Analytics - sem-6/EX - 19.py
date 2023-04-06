# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 13:49:06 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
house=pd.read_csv('House.csv')
house_size =house['SIZE'].tolist()
house_price =house['PRICE'].tolist()
num_house=100
print("size of the house size array...",len(house_size))
print("price of the house price array...",len(house_price))
print("size of 100 houses...")
print(house_size)
print("price of 100 houses")
print(house_price)
train_data_num =math.floor(num_house*0.8)
train_house_size = np.asarray(house_size[:train_data_num])
train_house_price = np.asarray(house_price[:train_data_num])
test_house_size=np.asarray(house_size[train_data_num:])
test_house_price=np.asarray(house_price[train_data_num:])
print("number of data point in training data size",len(train_house_size))
print("number of data point in training data price",len(train_house_price))
print("training data for size")
print(train_house_size)
print("training data for price")
print(train_house_price)
print("number of data point in test data size",len(test_house_size))
print("number of data point in test data price",len(test_house_price))
print("test data for size")
print(test_house_size)
print("test data for price")
print(test_house_price)
plt.plot(train_house_size,train_house_price,'bo')
plt.plot(test_house_size,test_house_price,'ro')
plt.xlabel("price of the house")
plt.ylabel("size of the house")
plt.show()
np_model= poly.polyfit(train_house_size, train_house_price, 2)