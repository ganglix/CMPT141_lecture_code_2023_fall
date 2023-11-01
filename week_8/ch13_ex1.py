# CMPT 141 - Arrays
# Topic(s): 1D Arrays


import numpy as np

# distances from current location to all coffee shop chain locations in city
coffee_shops = [5.5, 2.6, 12.5, 22.2, 0.45, 1.32, 3.3, 8.3, 6.2, 9.1]

# Part (a) Create a 1D array of the data items from coffee_shops in
# ascending order
a = np.array(coffee_shops)
a.sort()  # change values in-place
print(a)

# Part (b) Print the number of coffee shops

print("Number of coffee shops in the city:", a.size)

# Part (c) Print the distance to the farthest shop

print("The farthest coffee shop is ", a[-1])  # a was sorted
print("The farthest coffee shop is ", a.max())


# Part (d) Print the distances to the five closest shops
print("Distances to the five closest shops are ", a[0:5])
