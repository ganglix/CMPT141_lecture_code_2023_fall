def print_descending(N):
    if N == 0:
        print(N)
    else:
        print(N)
        print_descending(N-1)
# print_descending(5)

# (a) What is the condition for the base case?
# (b) What is the condition for the recursive case?
# (c) What problem is being delegated?
# (d) How is the solution to the delegated problem used?
# (e) What does the function do?

def print_ascending(N):
    if N == 0:
        print(N)
    else:
        print_ascending(N-1)
        print(N)

print_ascending(2)

"""
print_ascending(2)
    N = 2
    print_ascending(1)
        N = 1
        print_ascending(0)
            N = 0
            print(0)
        print(1)
    print(2)
"""
