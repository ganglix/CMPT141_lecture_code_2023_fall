# Write a Python program that uses a for-loop to print all
# integers between 300 and 600 (inclusive) that are divisible
# by both 3 and 5. Print how many of these numbers were
# found

for number in range(300, 600+1):
    if number % 3 == 0 and number % 5 == 0:
    # if number % 15 == 0:  # not readable, and misleading
        print(number)
