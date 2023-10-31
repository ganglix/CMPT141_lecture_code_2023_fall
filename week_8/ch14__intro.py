# beyond basic python - course requirement and continuing learning

# create an array
## numpy array

import numpy as np

# create 1-D array from a list (similar? different?)



# create 2-D array from list of lists




# create n-D array from list of lists of lists of...




# create some useful arrays, 1-D, 2-D




# attributes and methods





# indexing and slicing




# array relations and relational slicing



# Arithmetic operation.
# # arrays with the same size: element-wise




# # arrays with the different size: # super power! broadcasting!




# can go "wrong", "unwanted" broadcasting






#---------beyond textbook------------

# numpy functions vs. math functions






## clone with [:] or .copy()?
# a = [1,2,3]
# b = a
# b[0] += 100
# print(a)
# print(b)

# a = [1,2,3]
# b = a[:]   # b is a clone of a
# b[0] += 100
# print(a)
# print(b)

# a = np.array([1,2,3])
# b = a[:]
# # b = a.copy()
# b[0] += 100
# print(a)
# print(b)