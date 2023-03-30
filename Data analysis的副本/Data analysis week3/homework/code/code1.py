import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("../data/dataset.csv")
print(iris.shape)
print(iris.head(1000))
print(iris.tail(1000))
sns.set(color_codes = "True")
sns.histplot(iris["Area"])
sns.distplot(iris["SS"],kde = True)
plt.show()