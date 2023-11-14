"""
generation  ancestor
n   bees(n)
0   1
1   1
2   2
3   3
4   5
5   8
6   13
n
pattern
"""

# def







# time









# fix











# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def fastbees(L, N, this_level, next_level):
#     """
#     returns the number of ancestors a male bee has at its Nth generation
#     N: number of generations back to count ancestors for the bee
#     L: the current generation
#     this_level: the number of ancestors for generation L
#     next_level: the number of ancestors for generation L+1
#     return: number of male bee’s ancestors at generation N
#     """
#     if L == N:
#         return this_level
#     else:
#                         # L,   N,  this_level,     next_level
#         return fastbees(L + 1, N, next_level, this_level + next_level)
#                         # 1     3    1               2
#                         # 2     3    2               3
#                         # 3     3    3               5


# print(fastbees(0, 3, 1, 1))  # L, N, this_level, next_level
#
#
# def fastbees_iter(N):
#     """
#     returns the number of ancestors a male bee has at its Nth generation
#     N: number of generations back to count ancestors for the bee
#     return: number of male bee’s ancestors at generation N
#     """
#     # initialize
#     bee_list = [1, 1]
#     for i in range(2, N + 1):
#         bee_list.append(bee_list[-1] + bee_list[-2])
#     return bee_list[-1]


# print(fastbees_iter(60))
