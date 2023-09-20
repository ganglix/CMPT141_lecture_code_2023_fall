# Write a docstring for the following function definition (abs()
# returns the absolute value of a number):

def print_smaller_absolute(num1, num2):
    """This function takes two numbers and
    return the absolute value of the smaller number and print this value
    :param num1: int or float, first number
    :param num2: int or float, second number
    :return: int or float, the absolute value of the smaller number
    """
    small_abs = abs(min(num1, num2))
    print("Absolute value of smaller number: ", small_abs)
    return small_abs

help(print_smaller_absolute)


# things not to do.
# afraid to lose marks
# example in an engineering software program?
# style, numpy, google


# help(max)
# print(max.__doc__)
# print(print_smaller_absolute.__doc__)


#~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention~~~~~~~~~~~~~~~~~~
# sphinx, __doc__, help, hover, pen and paper




