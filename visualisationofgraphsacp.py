import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
weather = pd.read_csv("Test.csv")

print(weather.head())
weather.info()
sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
plt.show()
sns.stripplot(weather['weather_type'], weather['temperature'])
plt.show()
sns.stripplot(weather['weather_type'], weather['temperature'], jitter = True)
plt.show()
sns.swarmplot(weather['humidity'], weather['temperature'])
plt.show()
sns.boxplot(weather['humidity'], weather['temperature'], hue=weather['weather_type'])
plt.show()