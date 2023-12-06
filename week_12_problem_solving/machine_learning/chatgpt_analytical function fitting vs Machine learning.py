# # continuing learning and problem solving

# fit a curve to data  analytical function vs. machine learning

# analytical function curve fitting

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Define the true function
def true_func(x):
    return np.sin(x)


# Generate the data points with added noise
x_data = np.linspace(0, 3, 100)
y_data = true_func(x_data) + np.random.normal(scale=0.1, size=100)

plt.plot(x_data, y_data, '.')
plt.show()

# Define the function
def guessed_func(x, a, b, c):
    return a * np.sin(b * x) + c


# Fit the data using curve_fit
parameters_initial_guess = [1, 1, 1]
popt, pcov = curve_fit(guessed_func, x_data, y_data, parameters_initial_guess)

plt.plot(x_data, y_data, 'o', label='data')
plt.plot(x_data, guessed_func(x_data, *popt), '-', label='function ift')
plt.title( f"a * np.sin(b * x) + c parameters \n (a, b, c) = {popt}")
plt.show()
print(pcov)

# # machine learning to fit the data
# """
# ChatGPT prompt:
# fit the data (similar to sin(x)) using an artificial neural network with scikit-learn module. use all data for fit/train the model, no test
#
# """
#
# from sklearn.neural_network import MLPRegressor
#
# def ml_fit(x_data, y_data):
#     # Generate the data points
#     x_data = x_data.reshape(-1, 1)
#     y_data = y_data.reshape(-1, 1)
#
#     # Define the neural network model
#     model = MLPRegressor(hidden_layer_sizes=(10, 10), activation='tanh', solver='lbfgs')
#
#     # Train the model on the data
#     model.fit(x_data, y_data)
#
#     # Generate the fitted curve
#     y_fit = model.predict(x_data)
#
#     return y_fit
#

# # Plot the data and the fitted curve
# plt.plot(x_data, y_data, 'o', label='data')
# plt.plot(x_data, function_fit(x_data, y_data, noisy_func), '-', label='function ift')
# # plt.plot(x_data, ml_fit(x_data, y_data), '-', label='ML fit')
#
# plt.legend()
# plt.show()