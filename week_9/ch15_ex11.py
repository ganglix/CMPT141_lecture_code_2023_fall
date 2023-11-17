# Write a recursive function to find the smallest value in a list of
# numbers.


# 1 base case
# 2 recursive case (reduced problem, how to reduce)
# 3 relationship between the problem and the reduced problem

# def smallest(L):
#     # return the smallest item in a list
#     # base case
#     if len(L) == 0:
#         return None
#     elif len(L) == 1:
#         return L[0]
#     else:
#         # recursive case
#         # delegated task, reduced task, reduce the list L[1:]
#         small = smallest(L[1:])
#         # handle the relationship between the solution of the problem and the reduced one
#         if L[0] <= small:
#             return L[0]
#         else:
#             return small


def smallest(L):
    # return the smallest item in a list
    # base case
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    else:
        # recursive case:
        L_left = L[0: len(L)//2]
        L_right = L[len(L)//2:]

        small_left = smallest(L_left)
        small_right = smallest(L_right)

        #handle the relationship between the solution of the problem and the reduced one
        if small_left <= small_right:
            return small_left
        else:
            return small_right

print(smallest([3,2,1,4,5]))