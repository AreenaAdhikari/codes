import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("USA_Housing.csv")
print("\n_____First 5 rows _____")
print(df.head())
print("\n_____Data info_____")
print(df.info())
print("\n_____Statistical Summary_____")
print(df.describe)
sns.pairplot(df)
plt.show()
plt.figure(figuresize=(10,6))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
plt.show()
X = df.drop(['Price','Address'],axis=1)
y = df['Price']
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.3,random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_absolute_error(y_test,y_pred))
print("RMSE:",np.squrt(mean_absolute_error(y_test,y_pred)))
print("R2 score:",r2_score(y_test,y_pred))