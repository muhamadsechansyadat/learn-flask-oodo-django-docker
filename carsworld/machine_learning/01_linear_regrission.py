import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

print(x.shape, y.shape)

model = LinearRegression()

model.fit(x, y)

r_sq = model.score(x, y)
print('Koefisien determinan', r_sq)