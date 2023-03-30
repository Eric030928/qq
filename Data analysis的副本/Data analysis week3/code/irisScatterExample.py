import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("../data/iris.csv")
sns.set(style = "white",color_codes = False)
sns.stripplot(x = iris["Species"],y = iris["Petal.Length"],data = iris)
plt.show()