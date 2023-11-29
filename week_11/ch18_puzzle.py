import numpy as np

# Create a signed 8-bit integer array
# with the single data item 10.
x = np.array([10]).astype('int8')   # int8  _ _ _ _ _ _ _ _

# x[0] starts at 10 and gets larger with each loop iteration.
# while x[0] > 0:
#     x[0] = x[0] + 1
#     # print(x[0])

print('if I show up, the loop is done')
print('the value of x[0] is ', x[0])

"""
_    _  _  _  _ _ _ _   8-bits
sign 64 32 16 8 4 2 1
      1  1  1  1 1 1 1
"""
print(sum([ 64, 32, 16, 8, 4, 2, 1]))

# if we add 1 to       1  1  1  1 1 1 1
#     1  0  0  0  0 0 0 0
# -0 ? it is not; it is -128


# we used a fixed-bits to represent a number
# 8 bits, 7 bits for magnitude and left-most one for sign (but not following the sign-magnitude rule)
# add 1 to the max value of a 7-bits binary -> overflow
# overflow happens, it becomes -128

# -128 + 127(max of 7bits) = -1

import matplotlib.pyplot as plt
for i in range(512):
    x[0] = x[0] + 1
    plt.scatter(i,x[0])

plt.show()
