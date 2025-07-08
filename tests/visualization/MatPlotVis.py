import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [30, 32, 31, 29, 35]

plt.scatter(days, temperature)
plt.savefig("plot.png")
