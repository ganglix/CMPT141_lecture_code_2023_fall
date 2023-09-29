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
#   [                           ]
#    ________
#    87654321
#    01234567
s = "CMPT 141"

print(s[0: 3])  # T at index 3 is not included
# s[ start_index: stop_index(exclusive)]
print(s[0: 3+1])
print(s[0: len(s) + 100])
print(s[:])
# s[ start_index: stop_index(exclusive): step]
print(s[0:5:2])  #0, 2, 4,
print(s[5:0:-1]) #5, 4, 3, 2, 1
print("check this:", len(s[0:5:-1])) # if the slice does not make sense, you get a ""


# I want to mention omitted value, index out of range, and range of slice
