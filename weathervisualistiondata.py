import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
weather = pd.read_csv("Test.csv")

print(weather.head())
weather.info()
sns.jointplot(x="humidity",y="temperature",data=weather)
plt.show()
sns.jointplot(x="humidity",y="temperature",data=weather ,kind="hex")
plt.show()
sns.jointplot(x="humidity",y="temperature",data=weather ,kind="kde")
plt.show()