
# lists and tuples

# create a list
# lis = ['a', 1, [], len]  # list can contain a mix of datatypes

# tu = (1,'a')
# print(tu)
# print(list(range(6)))

# indexing and slicing, same as string, or other sequences
lis = ['a', 'b', 'c']
print(
    lis[0],
    lis[-1],
    lis[0:2],
    lis[1:],
    lis[1:100],
    # lis[100],
    sep='\n'
)

# methods
# add an item: .append(), +, .extend()
s = "computer"
new_s = s[1:4]
print(s)
print(new_s)

lis.append('d') # all the changes happened in-place
print(lis)
# lis.append(['e', 'f'])
# print(lis)
lis.extend(['e', 'f'])
print(lis)
new_lis = lis + ['e', 'f']  # is same as .extend()
print(new_lis)

# remove an item: .remove(), del, .pop()
lis.remove('a')
print(lis)
del lis[0]
print(lis)

returned_by_pop = lis.pop(0)   # by default it pops the last item
print(lis)
print(returned_by_pop)


# locating an item: index()
print(lis.index("e"))



# sorting: .sort()
lis.extend(['love', 'a'])
print(lis)
lis.sort(reverse=True)
print(lis)

# use a different way to sort
new_lis = sorted(lis)
print(new_lis)

# list is mutable ! more examples in flowtrace observations
a = 1
b = a
a = a + 1
print(a)
print(b)


a = [1]
b = a    # this step does not create a new list; it gives a name b to the [1]
a[0] = a[0] + 1
print(a)
print(b)


