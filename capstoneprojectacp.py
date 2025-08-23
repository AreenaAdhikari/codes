import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('abc.csv')
print(df.shape)
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.describe(include='all').T)
print(df.dtypes)
sns.pairplot(df)
plt.show()
numerical_cols = df.select_dtypes(include=[np.number]).columns
if len(numerical_cols) > 0:
    sns.swarmplot(y=df[numerical_cols[0]])
    plt.show()
