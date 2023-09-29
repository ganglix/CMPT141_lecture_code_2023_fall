# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

def check_char(s):
    """
    prints whether the string has an even or odd amount of characters
    :param s: string, a string to be checked
    :return: None
    """
    if len(s.strip()) % 2 == 0:
        # even
        checked = "even"
    else:
        # odd
        checked = "odd"
    print(f"{s} has an {checked} number of chars")

check_char(' Cat')