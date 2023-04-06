print("20-UCA-014")
print("Tharunvikraman")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df=pd.read_csv('movie_tickets_new.csv')
df=df.drop(['theatre_chain','calculated_seats','calculated_ticket_prices','calculated_screens','average_2','source_of_information','notes'],axis=1)
df=pd.get_dummies(df,columns=['city','theatre_name','type'])
df.fillna(df.mean(),inplace=True)
X_train,X_test,y_train,y_test=train_test_split(df.drop('average_ticket_price',axis=1),df['average_ticket_price'],test_size=0.2,random_state=42)
rf_model=RandomForestRegressor(n_estimators=100,random_state=42)
rf_model.fit(X_train,y_train)
def predict_ticket_price(theatre_name):
    columns=X_train.columns.tolist()
    if 'theatre_name' in columns:
        columns.remove('theatre_name')
        data=pd.DataFrame(np.zeros((1,len(columns))),columns=columns)
        data['theatre_name_'+theatre_name]=1
        return rf_model.predict(data)[0]
    
theatre_name='PVR: Velachery,Chennai'
predicted_price=predict_ticket_price(theatre_name)
print('Predicted ticket price for theatre "{}"'.format(theatre_name, predicted_price))
y_pred=rf_model.predict(X_test)
plt.plot(y_test.values,label='Actual Ticket Price')
plt.plot(y_pred,label='Predicted Ticket Price')
plt.xlabel=('Observation')
plt.ylabel=('Ticket price')
plt.title('Mobile brands market share prediction')

plt.show()

