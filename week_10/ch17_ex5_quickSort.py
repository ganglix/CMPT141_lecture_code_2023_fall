# Algorithm quickSort(S)
# # sorts sequence S using quick sort
# pivot = any item of S # e.g. the last item of S
# L = items in S smaller than pivot
# G = items in S larger than pivot
# E = items in S equal to the pivot
#
# # recursively solve the sub -problems of sorting L and G
# quickSort(L)
# quickSort(G)
#
# S = L + E + G # (where + represents concatenation)
# return S


def quick_sort(S):
    """
    quick sort a list and return it
    :param S: a list to be sorted
    :return: sorted list
    """
    if len(S) <= 1:
        return S
    else:
        # recursive case
        pivot = S[-1] # e.g. the last item of S
        # L = items in S smaller than pivot
        # G = items in S larger than pivot
        # E = items in S equal to the pivot
        L = []
        G = []
        E = []
        for item in S:
            if item > pivot:
                G.append(item)
            elif item == pivot:
                E.append(item)
            else:
                L.append(item)

        # recursively solve the sub -problems of sorting L and G
        L_sorted = quick_sort(L)
        G_sorted = quick_sort(G)

        S = L_sorted + E + G_sorted # (where + represents concatenation)
    return S

print(quick_sort( [ 2, 1, 3, 4]))





#  https://www.toptal.com/developers/sorting-algorithms