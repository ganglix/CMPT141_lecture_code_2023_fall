# Indexing and Slicing of !Sequences!
"computer science"
[1, 2, "whatever"]
(1, 2, 3)


# •What is indexing used for?
# •What does a positive index mean?
# •What does a negative index mean?

#    ________
#    87654321
#    01234567
s = "CMPT 141"

print( s[len(s)-1] )
print( s[-1])
# print T
print(s[3])
print(s[-5])
print(s[-len(s)])

# •What is slicing used for?
# •What are the meanings of the First, second, and third
# numbers in a slicing operation?
#    ________
#    87654321
#    01234567
s = "CMPT 141"

print(s[0: 3])  # T at index 3 is not included
# s[ start_index, end_index(exclusive)]
print(s[0: 3+1])




# I want to mention omitted value, index out of range, and range of slice
