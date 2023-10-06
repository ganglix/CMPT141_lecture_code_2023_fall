# Classify the loops in these Python excerpts as terminating
# (reaches an end) or infinite in nature:

# # (a)
# for x in range(100, 10, 10):
#     print(x * 5)

# (b)
# sum = 0
# i = 0
# while i < 10:
#     sum = sum + i


# (c)
# x = 5
# goal = 16
# while x != goal:
#     x = x + 2

# (d)
divisor = 2
dividend = 6793
while dividend % divisor != 0:
    divisor = divisor + 1
if divisor == dividend:
    print(f"{dividend} is a prime number")
else:
    print(f"{dividend} is NOT a prime number")
    print(f"it can be divided by {divisor}")

# # (e)
# low = -100
# high = 100
# msg = " Enter int between " + str(low) + " to " + str(high) + ":"
# num = int(input(msg))
# while num >= low or num <= high: # change or to and
#     num = int(input(msg))
# # when while loop is done
# print(f"number {num} is out of range")