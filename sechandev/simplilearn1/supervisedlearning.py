# importing Numpy, Matplotliband sklearnlibraries
import matplotlib.pyplot as plt
import numpy as np
# importing datasets from scikit-learn
from sklearn import datasets, linear_model
# load the dataset
house_price = [245, 312, 279, 308, 199, 219, 405, 324, 319, 225]
# house_price2 = np.array(house_price).reshape((-1, 1))
# print(house_price2)
size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
print(size)
# Reshape the input to your regression
size2 = np.array(size).reshape((-1, 1))
print(size2)
# By using fit module in linear regression, user can fit the data frequently and quickly
regr = linear_model.LinearRegression()
regr.fit(size2, house_price)
print("Coefficients: \n", regr.coef_)
print("Intercept: \n", regr.intercept_)

size_new = 1400
price = (size_new * regr.coef_) + regr.intercept_
print(price)
print(regr.predict([[size_new]]))
# Formula obtained for the trained model
def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
# Plotting the prediction line
graph('regr.coef_* x + regr.intercept_', range(1000, 2700))
plt.scatter(size, house_price, color='black')
plt.ylabel('house_price')
plt.xlabel('size of house')
plt.show()