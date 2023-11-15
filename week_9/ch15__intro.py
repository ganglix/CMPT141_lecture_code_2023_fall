# recursion
# "the family chain of new phones"


# problem solving - delegation metaphor
# 1 find the base case (easy)
# 2 find a way to reduce the problem (not easy): reduce steps of procedure, quantity of a number, size of a list

def is_even(n):
    """ returns True if n is an even number, otherwise return False.
    """
    # base case
    if n == 0:
        return True
    else:
        # recursive case
        # the previous number: n-1
        is_previous_number_even = is_even(n-1) # need to figure out  if n-1 is even  # delegated task(reduced version of the problem)
        is_this_number_even = not is_previous_number_even  # how the solution of the problem is related to the solution of the reduced problem
    return is_this_number_even

print(is_even(2))

"""
is_even(2)
n = 2
is_previous_number_even = is_even(2-1)
                          n = 1
                          is_previous_number_even = is_even(1-1)
                                                    n = 0
                                                    return True
                          is_this_number_even = not True
                          return False
                          
is_this_number_even = not False
return True

"""



# recursion depth
for i in range(10000):
    try:
        is_even(i)
    except:
        print(f"max recursion number reached: {i}")
        break
