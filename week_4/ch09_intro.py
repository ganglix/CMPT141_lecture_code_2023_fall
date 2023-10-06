# Control Flow: Repetition
# what is a computer good at?
# repeat till what? when?


# while loop starts and stops according to a condition
## things I want to mention: condition boolean, while/if, keep checking(eg.)

# counting example
# count from 1 to 3
count = 0
while count < 3:
    # keep doing the following block
    count = count + 1
    print(count)

# when the while loop is done
print("great, done")


# for : repeat over a sequence
## mention types of sequence: string, range, list, dict

# s = "cmpt 141"
# for char in s: # iterate item over c m p t   1 4 1
#     print(char)
#
# for i in range(0, 3, 1): #range(3):  # iterate i over 0 1 2     range(start, stop(exclusive), step)
#     print(i)
#     print("woof")

s = "cmpt 141"
end_index = len(s)-1
current_index = 0
while current_index <= end_index:
    print(s[current_index])
    current_index += 1  # current_index = current_index + 1

# flowtrace
i = 1
while i < 10:
    i = i * 2
print(i)

"""
i = 1
while 1 < 10:
i = 1 * 2
while 2 < 10:
i = 2 * 2
while 4 < 10:
i = 4 * 2
while 8 < 10:
i = 8 * 2
while 16 < 10:

print(16)
"""


# flowtrace
for c in "PIKA":
    print(c)
    print("hoorah !")

"""
for c in "PIKA":
c = "P"
print("P")
c = "I"
print("I")
...
c = "A"
print("A")
print("hoorah !")
"""

# flow trace - nested for loop

total = 0
for i in range(2):
    for j in range(2):
        total = total + 1
print(total)

""" write down the code that the computer would execute in sequence:
total = 0
for i in range(2):
i = 0
for j in range(2):
j = 0
total = 0 + 1
j = 1
total = 1 + 1
i = 1    
for j in range(2):
j = 0
total = 2 + 1
j = 1
total = 3 + 1
print(4)

"""