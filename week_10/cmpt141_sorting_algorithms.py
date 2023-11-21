# CMPT 141 - Sorting Algorithms
# contains implementations of sorting algorithms from the readings:
#  - insertion sort
#  - merge sort
#  - quick sort


#########################
# INSERTION SORT
#########################

def insertion_sort(U):
    """
    creates new sequence containing sorted data of U where
    data is sorted using insertion sort
    U: sequence to sort
    return: new sequence where U is sorted
    """

    # create an empty sequences for S
    S = []

    # insert each item in U into S
    for item in U:
        i = 0

        # search for the offset at which to insert the
        # item into S.
        while i < len(S) and item >= S[i]:
            i = i + 1

        # insert the item immediately before the item at offset i.
        # this also shifts the items at offset i and higher
        # to the right to make space for the new item.
        S.insert(i, item)

    return S


#########################
# MERGE SORT
#########################
def merge(S1, S2):
    """
    combines two sorted sequences into single sorted sequence
    S1: sorted sequence to combine
    S2: other sorted sequence to combine
    return: single sorted sequence of S1, S2 combined
    """
    # let S be an empty sequence
    S = []
    # repeatedly move the smallest item to S
    while len(S1) > 0 and len(S2) > 0:
        if S1[0] < S2[0]:
            S.append(S1[0])
            del S1[0]
        else:
            S.append(S2[0])
            del S2[0]
    # once one of S1 or S2 is empty, append the remaining
    # non-empty sequence to S.
    if len(S1) > 0:
        S.extend(S1)
    else:
        S.extend(S2)
    return S



def merge_sort(S):
    """
    merge sort a list in ascending order and return it
    :param S: a list to be sorted
    :return: sorted list
    """
    # base case
    if len(S) <= 1:
        return S
    else:
        # divide step
        left = S[0 : len(S)//2]
        right = S[len(S)//2 : ]

        # recursive solving
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

        # conquer step
        return merge(left_sorted, right_sorted)




#########################
# QUICK SORT
#########################

def quick_sort(S):
    """
    quick sort a list and return it
    :param S: a list to be sorted
    :return: sorted list
    """
    if len(S) <= 1:
        return S
    else:
        # pivot = any item of S # e.g. the last item of S
        pivot = S[-1]
        L = []
        G = []
        E = []
        # L = items in S smaller than pivot
        # G = items in S larger than pivot
        # E = items in S equal to the pivot
        for item in S:
            if item < pivot:
                L.append(item)
            elif item == pivot:
                E.append(item)
            else:
                G.append(item)
        # recursively solve the sub -problems of sorting L and G
        L_sorted = quick_sort(L)
        G_sorted = quick_sort(G)

    return L_sorted + E + G_sorted  # (where + represents concatenation)