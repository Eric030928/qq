import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def sinplot(flip = 2):
    x = np.linspace(0,20,100)
    for i in range(1,5):
        plt.plot(x,np.cos(x + i * 0.8) * (9-2*i) * flip)
if __name__ == "__main__":
    """sns.set_context("notebook")
    sns.set(style = "whitegrid",font_scale = 1.5)
    sinplot()
    plt.show()"""
    sns.set_context("notebook")
    with sns.axes_style("darkgrid"):
        plt.subplot(2,1,1)
        sinplot()

    plt.subplot(2,1,2)
    sinplot(-1)
    plt.show()
