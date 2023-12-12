import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]

weights = [1,5,6,7,8,9,22,33,44,55,6,66,23,22,11,11]

plt.plot(years,weights)
plt.show()