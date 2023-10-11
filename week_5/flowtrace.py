L = [1, 2, 3, 4, 5, 6]
for value in L:
    L.remove(value)
print(L)

"""
L = [1, 2, 3, 4, 5, 6]
for value in [1, 2, 3, 4, 5, 6]:
    value = 1
    [1, 2, 3, 4, 5, 6].remove(1)
    value = 2 
    [2, 3, 4, 5, 6].remove(2)
    value = 3
    [3, 4, 5, 6].remove(3)
    ...
    value = 6
    [6].remove(6)
print([])
"""

"""
L = [1, 2, 3, 4, 5, 6]
for value in [1, 2, 3, 4, 5, 6]:
    value = 1   # value = L[0] first index
    [1, 2, 3, 4, 5, 6].remove(1)   # L is [2,3,4,5,6]
    value = 3   # value = L[1] second index, value skipped 2...
"""




# L = []
# for i in range(3):
#     L.append([])
# for char in "abc":
#     L[0].append(char)
# print(L)