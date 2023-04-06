# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:56:07 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
data=pd.read_csv('product_sales_data.csv')
print(data.head())
print(data.describe())
X=data[['advertising_budget','num_promotions','store_location']]
y=data['sales']
X=pd.get_dummies(X,columns=['store_location'])
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
lasso=Lasso(alpha=0.1)
lasso.fit(X_train,y_train)
y_pred=lasso.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
print('Model Coefficients:',lasso.coef_)
print('Mean squared error:',mse)
