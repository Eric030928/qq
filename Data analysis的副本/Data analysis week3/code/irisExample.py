import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("../data/iris.csv")
print(iris.shape)
print(iris.head(3))
print(iris.tail(3))
sns.set(color_codes = "True")
sns.histplot(iris["Petal.Width"])
sns.distplot(iris["Petal.Width"],bins = 20 ,kde = True)
plt.show()