import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(1000) * 1000
y_data = np.random.random(1000) * 1000

plt.scatter(x=x_data,y=y_data,c='#064e3b')
plt.show()
