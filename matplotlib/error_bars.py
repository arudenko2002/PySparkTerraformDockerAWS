import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
error = np.array([0.5, 0.7, 0.4, 0.6, 0.3])

# Plot with error bars
plt.errorbar(x, y, yerr=error, fmt='o', capsize=5, color='blue', ecolor='red')
plt.title("Data with Error Bars")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()