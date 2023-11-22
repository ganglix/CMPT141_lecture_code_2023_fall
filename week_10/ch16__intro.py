# Search algorithm


# search for a number from a list of numbers

# generate an array to work with

import numpy as np




# linear search
def linear_membership_search(c, target_key):
    """
    a linear membership search for the target key

    c:          a sequence of numbers or strings
    target_key: the target key for the search
    return: True if target key is in the collection
    """
    # base case
    if len(c) == 0:
        return False
    else:
        # recursive case c[1:]
        if c[0] == target_key:
            return True
        else:
            return linear_membership_search(c[1:], target_key)

# c = np.random.uniform(0,9, size=5).astype(int)
# print(c)
# print(linear_membership_search(c, 4))


# binary search

def binary_membership_search(c, target_key):
    """
    A binary membership search function
    :param c: list, collection of data, sorted by its search keys
    :param target_key: target key to search for
    :return: True if target key is in the collection
    """
    # base case
    if len(c) == 0:
        return False
    else:
        mid_idx = (len(c)-1) //2   # index at the middle (round down)
        if c[mid_idx] ==  target_key:
            return True
        elif c[mid_idx] > target_key:
            # check the left side
            return binary_membership_search(c[: mid_idx], target_key)
        else:
            # check the right side
            return binary_membership_search(c[mid_idx+1 :], target_key)


c = np.random.uniform(0,9, size=20).astype(int)
c.sort()    # to make binary search work, the list has to be SORTED
print(c)
print(binary_membership_search(c, 4))

