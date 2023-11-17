"""
N   F(N)
0   1
1   3
2   5
3   7
4   9
5   11
----------------

F(5) = F(4) + 2
F(4) = F(3) + 2
F(3) = F(2) + 2
F(N) = F(N-1) + 2    # key relationship/ pattern used for your recursion function
..."""

def F(n):
    if n == 0:
        return 1
    else:
        return F(n-1) + 2

print(F(5))


