from matplotlib import pyplot as plt
import numpy as np

nums = [1, 2, 3, 4, 5, 6]
labels = ['Rent', 'Food', 'Kids', 'Home', 'Fitness', 'Beauty']
fig = plt.figure(figsize =(10,7))
plt.pie(nums, labels = labels)
plt.show()