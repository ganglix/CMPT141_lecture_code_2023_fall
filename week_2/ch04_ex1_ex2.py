# Define a Python function called format_price that:
# (a) Has two integer parameters, indicating the cost in dollars
# and cents of an item
# (b) Returns a single string in the format "$D.C".
# (c) Example: if called with arguments 9 and 99, the function
# should return the string $9.99

def format_price(dollar, cent):
    """ format price as "$D.C." with the amount of dollar and cent and return the formatted string
    :param dollar: integer, dollar amount
    :param cent: integer, cent amount
    :return: str, formatted price
    """
    formatted = "$" + str(dollar) + "." + str(cent)
    print(formatted)
    return formatted


print("print outside of the function:", format_price(9, 99))