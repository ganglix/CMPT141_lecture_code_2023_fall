"""
N   F(N)
0   1
1   2
2   4
3   7
4   11
5   16     F(5) = F(4) + 5

F(N) = F(N-1) + N
"""

def F(n):
    if n == 0:
        return 1
    else:
        return F(n-1) + n

print(F(5))




