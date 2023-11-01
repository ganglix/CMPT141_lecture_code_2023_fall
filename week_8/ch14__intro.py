# beyond basic python - course requirement and continuing learning

# create an array
## numpy array

import numpy as np

# create 1-D array from a list (similar? different?)
L = [1, 2, 3] #"trick"]
print(L*2)
arr = np.array(L)   # array can only has one data type
print(L)
arr = arr.astype(float)
print(arr)
arr[0] = 10
print(arr)
print(np.append(arr, 0.1)) # created a new array; the arr was not affected
# array: same datatype, method often creates a new array, size does not change, mutable (change the value in-place)


# create 2-D array from list of lists
lol = [   [1,2,3],  [4,5,6]   ]
print("-"*20)
print(lol)
lol_a = np.array(lol)
print(lol_a)
print(lol_a[0, 1])  # first row, second column


# create n-D array from list of lists of lists of...
# lolol = [ [  [1], [2]  ]  ,  [ [3] , [4] ]   ]
# print(np.array(lolol))


# create some useful arrays, 1-D, 2-D
print("~~"*10)
print(np.ones(3))
print(np.ones((3,4)) * 2)
print(np.zeros(9))  # useful for initialize an empty array to store information later
print(np.arange(0, 9, 0.5))  # start, stop(exclusive), step

# attributes and methods
print(lol_a.shape)
print(lol_a.size)
print(lol_a.ndim)
a = np.arange(0, 9, 0.5)
print(a.mean(), a.max(), a.std())


# indexing and slicing
print(
lol[0][0],
lol_a[0, 0])  # array[row, col]  array[row_range, col_range]


# array relations and relational slicing
aa = np.linspace(0, 5, 6)  # start, stop(INCLUDED), number of numbers
print(aa)
mask = aa > 3 # an array with bool values T/F about the >
b = aa[mask] # creates a new array
# b[0] = b[0]+10
# print(aa)

# Arithmetic operation.
# # arrays with the same size: element-wise
x = np.ones(3)
y = np.ones(3) * 10
print(x)
print(y)
print(x*y)


# # arrays with the different size: # super power! broadcasting!
x = np.ones(3)
y = np.ones((4, 3))*10
print('~'*20)
print(x)
print(y)
print(x+y)


# can go "wrong", "unwanted" broadcasting
x = np.ones(3)
y = np.ones((4, 1))*10
print('~'*20)
print(x)
print(y)
print(x+y)



#---------beyond textbook------------

# numpy functions vs. math functions

import math
# print(math.sin(arr))    # math.sin can only handle one number

print(np.sin(arr))        # np.sin can handle the array






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

a = np.array([1,2,3])
# b = a[:]  # does not create a clone/copy. it creates a slice view of the array
b = a.copy()  # this one create a copy
b[0] += 100
print(a)
print(b)