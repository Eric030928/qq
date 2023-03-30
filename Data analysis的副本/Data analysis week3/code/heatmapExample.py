import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
flight = pd.read_csv("../data/flights.csv")
print(flight.head(2))
flight = flight.pivot("month","year","passengers")
print(flight.head(2))
sns.heatmap(flight,alpha = 0.9)
plt.show()