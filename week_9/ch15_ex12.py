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
n   bees(n) = bees(n-1) + bees(n-2)
pattern
"""

def bees(n):
    if n == 0 or n == 1:
        return 1
    else:
        return bees(n-1) + bees(n-2)

# print(bees(20))

# bees_list = []
# for i in range(20):
#     bees_list.append(bees(i))
#
# import matplotlib.pyplot as plt
# plt.plot(range(20), bees_list)
# plt.show()



# time
# import time
# start = time.time()
# bees(20)
# end = time.time()
# time_per_call = (end-start)/(2**20)
# # print(time_per_call)
# print("time for bees(60): ", time_per_call * 2**60 / 60 / 60 / 24 / 365)

# fix
bees_n_cache = {}   # to store the solved n : bees(n)
def bees_efficient(n):
    if n == 0 or n == 1:
        return 1
    else:
        # check if the solution has been previously solved
        if n in bees_n_cache:
            return bees_n_cache[n]
        else:
            bees_n_cache[n] = bees_efficient(n-1) + bees_efficient(n-2)
            return bees_n_cache[n]

print(bees_efficient(60))







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
