# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:26:18 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("prices.csv")
print(df)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
fuelList=['Price of Petrol','Price of Diesel']
rowIndex=1
columnIndex=2
def plot_data(df,yLabel,x_test,y_test,y_pred,rowIndex,columnIndex,subPlotIndex):
    plt.subplot(rowIndex,columnIndex,subPlotIndex)
    plt.scatter(x_test, y_test, color='blue', label='Actual')
    plt.scatter(x_test, y_pred, color='red', label='Predicted')
    plt.xlabel('Year')
    plt.ylabel("{} in Rupees".format(yLabel))
    plt.legend(loc='upper Left')
    plt.title("{} Prediction".format(yLabel),loc='left')
df=pd.read_csv("prices.csv")
x=df['Year']
for i in range(0,2):
    y=df[fuelList[i]]
    print("Y Value:",y)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    knn=KNeighborsRegressor(n_neighbors=5)
    knn.fit(x_train.values.reshape(-1,1),y_train)
    y_pred=knn.predict(x_test.values.reshape(-1,1))
    mse=mean_squared_error(y_test,y_pred)
    print('Mean Squared Error for',df.iloc[0,i+1],':-\n',mse)
    print("y_pred=",y_pred,"y_test=",y_test)
    plot_data(df,fuelList[i],x_test,y_test,y_pred,rowIndex,columnIndex,i+1)
plt.show()
