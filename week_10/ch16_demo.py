# Topic: Timing comparison: linear search vs. binary search

import time as time
def linear_membership_search(c, target_key):
    """
    a linear membership search for the target key

    c:          a sequence of numbers or strings
    target_key: the target key for the search
    return: True if target key is in the collection
    """
    for i in c:
        if i == target_key:
            return True

    return False



def binary_membership_search(C, target_key, start, end):
    """
    a binary search for membership

    C:              a collection of data items ordered by their search keys
    target_key :    the target key
    start :         first offset of S to be searched
    end:            last offset of S to be searched
    return :        true if S contains an item whose search key
    matches the target , false otherwise
    """
    if end < start:
        return False
    if end == start and start >= len(C):
        return False
    mid = (start + end) // 2

    if C[mid] == target_key:
        return True
    elif C[mid] < target_key:
        return binary_membership_search(C, target_key, mid + 1, end)
    else:
        return binary_membership_search(C, target_key, start, mid - 1)


# search parameters
n_data = int(1e8)  # number of data items in array (default 100 Million)
targetKey = n_data//2-10   # target key to search for

# construct list of ints 0 to n_data-1 to search
t_start = time.time()
nums = list(range(0, n_data))  # ascending order
time_generate = time.time() - t_start
print("It took ", time_generate, 'seconds just to generate the data.')
print("nums = [" + ",".join([str(i) for i in nums[:3]]) + ", ..." + ",".join([str(i) for i in nums[-3:]])+"]")

# time linear membership search
time_start = time.time()
lin_result = linear_membership_search(nums, targetKey)
time_linear = time.time() - time_start

# time binary membership search
time_start = time.time()
bin_result = binary_membership_search(nums, targetKey, 0, len(nums))
time_binary = time.time() - time_start

# Display the results.
print("linear_membership_search for", targetKey, ":",
      "search result", ":", (lin_result),
      "time used", ":", time_linear, "(s)")

print("binary_member_search for", targetKey, ":",
      "search result", ":", (lin_result),
      "time used", ":", time_binary, "(s)")
print()
