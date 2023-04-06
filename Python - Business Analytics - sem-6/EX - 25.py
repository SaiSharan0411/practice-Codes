print("20-UCA-016")
print("Sai Sharan")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('movie_tickets_new.csv')
data=data.dropna()
data.drop(['city','theatre_name','type','theatre_chain','lat','lon','source_of_information','notes'],axis=1,inplace=True)
X=data.drop('average_ticket_price',axis=1)
y=data['average_ticket_price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
r2_score(y_test,y_pred)
new_data=pd.DataFrame({
    'total_seats':[500],
    'no_screens':[4],
    'calculated_seats':[450],
    'calculated_ticket_prices':[12],
    'calculated_screens':[3],
    'average_2':[7.5]})
model.predict(new_data)
sns.lineplot(x=X_test['no_screens'],y=y_test,label='Actual')
sns.lineplot(x=X_test['no_screens'],y=y_test,label='Predicted')
plt.xlabel=('Numbers of screens')
plt.ylabel=('Average ticket price')
plt.show()# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:25:53 2023

@author: cat17
"""

