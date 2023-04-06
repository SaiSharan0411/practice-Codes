# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:47:45 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
data=pd.read_csv("Currencies.csv")
x=data.iloc[:,2].values.reshape(-1,1)
y=data["USD"].values.reshape(-1,1)
linear_regressor=LinearRegression()
linear_regressor.fit(x,y)
y_pred=linear_regressor.predict(x)
plt.scatter(x,y)
plt.plot(x,y_pred,color='red')
plt.show()