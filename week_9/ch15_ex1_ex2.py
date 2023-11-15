
# N! = N * (N-1)!
# 3! = 3 * 2 * 1
# 2! = 2 * 1
# 1! = 1 * 1
# 0! = 1

def factorial_a(N):
    # base case
    if N < 0:
        return None
    elif N == 0:
        return 1
    else:
        # recursive case
        # reduced problem being delegated is factorial_a(N - 1)
        return factorial_a(N - 1) * N


# print(factorial_a(3))


# (a) What is the condition for the base case?

# (b) What is the condition for the recursive case?

# (c) What problem is being delegated?

# (d) How is the solution to the delegated problem used?


def factorial_b(N):
    # recursive case
    if N > 0:
        return factorial_b(N - 1) * N
    else:
        # base case ( most reduced case )
        return 1

# print(factorial_b(3))
""" flowtrace (simple version)
factorial_b(2) 
N = 2 return factorial_b(2 - 1) * 2
             N = 1 return factorial_b(1 - 1) * 1
                          N = 0 return 1             

"""

# which one is better?

print("option_a: ", factorial_a(-1))  # error
# print("option_b: ", factorial_b(-1))  # no error, wrong result