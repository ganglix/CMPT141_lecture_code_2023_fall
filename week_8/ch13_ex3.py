# CMPT 141 - Arrays
# Topic(s): Operations on Arrays, relational operation, logical slicing


import numpy as np

A = np.array([10, 20, 30, 40, 50])
# What is the value of:

# A + [1 2 3 4 5]   # [1 2 3 4 5] is an array
print(A + np.array([1, 2, 3, 4, 5]))
# A > 25
print(A > 25)
# logical slicing
# print(A[ np.array([True, False, True, True, False]) ])

# mask = A > 25
# print( A[mask])

print(A[A > 25])  # prints all elements in A which are geater than 25

# how about > 10 and < 40
# print(A[A > 10 and A < 40])  # not working, "and" can not handle array of bools

print(A[np.logical_and(A > 10 , A < 40)])

