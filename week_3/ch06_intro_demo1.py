# module, import, alias
import math as m
print(m.sin( m.radians(180) ))

print(m.sin(m.pi))

# help(math.sin)

# math module
# function
# constant

print( m.log( m.e) )   # in python log is by default with base of e : ln
print( m.pow(10 , 2))  # 10**2
print(
    m.sqrt(2),
    m.pow(2, 1/2)
)

# more real world examples (my experience in engineering)

# scientific computing
import numpy as np
arr = np.linspace(1, 10, 100) # 100 numbers from 1 to 10 with equal spaces
print(arr)
print(arr.mean())
print(arr.std())


# visualization plot
# import matplotlib.pyplot as plt
# plt.plot( arr, np.sin(arr))
# plt.show()
# plt.savefig("plot.tiff", dpi=1200)


# data science
# import pandas as pd
# df = pd.read_csv("../week_0/namelist.csv")
# print(df)


# things I want to mention
# many types of import

# import math as m
# from math import sin

# from math import *  # import all function names in math module # DONT use this one
#
# cos = 'passward'
#
# cos(pi)