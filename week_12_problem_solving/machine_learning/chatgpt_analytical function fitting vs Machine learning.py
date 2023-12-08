# # continuing learning and problem solving

# fit a curve to data  analytical function vs. machine learning

# analytical function curve fitting

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Define the true function
def true_func(x):
    return np.sin(x)

def calculate_r_squared(y_data, y_predicted_data):
    """
    chatgpt Prompt:
    Write a function to calculate the R-squared for goodness of fit,
    given two arrays: y_data and y_predicted_data
    """
    # Calculate the mean of the actual values (y_data)
    mean_y_data = np.mean(y_data)

    # Calculate the total sum of squares (TSS)
    tss = np.sum((y_data - mean_y_data) ** 2)

    # Calculate the residual sum of squares (RSS)
    rss = np.sum((y_data - y_predicted_data) ** 2)

    # Calculate R-squared (coefficient of determination)
    r_squared = 1 - (rss / tss)

    return r_squared

# Generate the data points with added noise
x_data = np.linspace(0, 5, 100)
np.random.seed(0)
y_data = true_func(x_data) + np.random.normal(scale=0.1, size=100)

# plt.plot(x_data, y_data, '.')
# plt.show()


# Define the function
def guessed_func(x, a, b, c):
    return  a + b * np.sin(x+c)


# Fit the data using curve_fit
result = curve_fit(guessed_func, x_data, y_data)
parameters = result[0]   # [ value of a , value of b]

# plt.plot(x_data, y_data, '.')
# plt.plot(x_data*3, guessed_func(x_data*3, *parameters) )  # *parameteres unpack it to a , b
# plt.show()
# print(calculate_r_squared(y_data, guessed_func(x_data, *parameters)))


# # machine learning to fit the data
"""
ChatGPT prompt:
fit the data (similar to sin(x)) using an artificial neural network with scikit-learn module.
use all data for fit/train the model, no test
"""

from sklearn.neural_network import MLPRegressor

# Generate the data points
x_data = x_data.reshape(-1, 1)
# y_data = y_data.reshape(-1, 1)  # y_data should be 1-D

# Define the neural network model
model = MLPRegressor(hidden_layer_sizes=(5, 5), activation='tanh', solver='lbfgs')

# Train the model on the data
model.fit(x_data, y_data)

# Generate the fitted curve
y_fit = model.predict(x_data)   # now the model has been already trained/ fitted

#
# # Plot the data and the fitted curve
plt.plot(x_data, y_data, 'o', label='data')
plt.plot(x_data, y_fit, '-', label='ML fit')
plt.plot(x_data, guessed_func(x_data, *parameters), label = 'analytical' )  # *parameteres unpack it to a , b


plt.legend()
plt.show()
print(calculate_r_squared(y_data, y_fit))



