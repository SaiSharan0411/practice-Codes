# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:01:43 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib','inline')

df=pd.read_csv('train_loanPrediction.csv')
df.head(5)
df.describe()
df.count(axis=0)
print(df['Property_Area'].value_counts())
print(df['Gender'].value_counts())
df['ApplicantIncome'].hist(bins=50)
df.boxplot(column='ApplicantIncome',by='Gender')
df.plot.box(grid='True')
t1=pd.crosstab(df['Education'],df['Loan_Status'])
t1.plot(kind='bar',stacked='True',color=['red','blue'],grid=False)
df.apply(lambda x:sum(x.isnull()),axis=0)
df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)

print(df['LoanAmount'].count())
df['LoanAmount'].median()
df.groupby('ApplicantIncome').mean()[:5]
df.groupby('Married').get_group('Yes')[:5]

print("mean is: ",df['ApplicantIncome'].mean())
print("median is: ",df['ApplicantIncome'].median())
print("mode is: ",df['ApplicantIncome'].mode())

print("standard deviation is:",df['ApplicantIncome'].std())
print("variance is: ",df['ApplicantIncome'].var())
print("skewness is: ",df['ApplicantIncome'].skew())
df['ApplicantIncome'].hist(bins=50)
x=df['ApplicantIncome']
bins=50
mu=df['ApplicantIncome'].mean()
print("mean is",mu)
sigma=df['ApplicantIncome'].std()
print("standard deviation is: ",sigma)

plt.plot(x,1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2)),linewidth=3,color='y')
plt.show()

stats.ttest_ind(df['ApplicantIncome'],df['CoapplicantIncome'])
df.corr()
print(stats.chisquare(df['Education'].value_counts()))
print(stats.chisquare(df['Loan_Status'].value_counts()))
cont=pd.crosstab(df['Education'],df['Loan_Status'])
stats.chi2_contingency(cont)
df['Education'].value_counts()
from sklearn.linear_model import LinearRegression
X=np.array(df['ApplicantIncome']).reshape(-1,1)
Y=np.array(df['CoapplicantIncome']).reshape(-1,1)
linear_regressor=LinearRegression()
linear_regressor.fit(X,Y)
Y_pred=linear_regressor.predict(X)
print(Y_pred[:5])
plt.scatter(X,Y)
plt.plot(X,Y_pred,color='red')
plt.show()
