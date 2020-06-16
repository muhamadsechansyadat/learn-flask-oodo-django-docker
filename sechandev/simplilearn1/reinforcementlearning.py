# Importing libraries
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
# importing the dataset
data = pd.read_csv('sechan.csv')
print(data.shape)
data.head()

# Getting the values and plotting it

f1 = data['Temperature Difference'].values
f2 = data['Pressure Difference'].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='black', s=7)