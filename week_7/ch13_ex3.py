def is_valid_password(password):
    """
    determines if password meets these constraints:
    - 9-18 characters long
    - no Underscores or minus _,-
    password: string to check validity of
    return: True if password satisfies constraints
    """
    is_valid = True

    if len(password) < 9 or len(password) > 18:
        is_valid = False
    if "_" in password:
        is_valid = False
    if "-" in password:
        is_valid = False

    return is_valid


# Testing - white box
# white box reasoning: make sure every singe line of code get tested!

# for inputs, check the code, use white box reasoning
# for expected output, give "correct" answer as you learned from the docstring

"""
inputs:""
outputs_expected: False
reason: trigger line 11 if statement, condition is true

inputs:"1"* 19
outputs_expected: False
reason: trigger line 11 if statement, condition is true

inputs:"1"* 10
outputs_expected: True
reason: trigger line 11 if statement, condition is false

"""

"""
inputs:"_"
outputs_expected: False
reason: trigger line 11 if statement, trigger line 13 if statement, condition is True

inputs:"a"*10 + "_"
outputs_expected: False
reason: Only trigger line 13 if statement, condition is True
"""

"""
inputs:"-"
outputs_expected: False
reason: trigger line 15 if statement, trigger line 13 if statement, condition is True

inputs:"a"*10 + "-"
outputs_expected: False
reason: Only trigger line 15 if statement, condition is True
"""



# # an fancy way to organize your test cases using list of dictionaries
# test_suite =[
#     {"input": "a"*8,
#     "output": False,
#     "reason": "trigger line 11, length of the password is less than 9"
#      },
#
#     {"input": "a" * 19,
#      "output": False,
#      "reason": "trigger line 11"
#      },
#
#     {"input": "12_",
#      "output": False,
#      "reason": "trigger line 13 if statement"
#     }
# ]
# for test_case in test_suite:
#     res = is_valid_password( test_case["input"] )
#     if res != test_case["output"]:
#         print("fault found!", test_case['reason'])
#         print("    expected: ", test_case["output"])
#         print("    returned: ", res)
#         print()
#     else:
#         print("all tests passed!")


def is_divisible_by_7 (numbers):
    """
    This function returns true if the list numbers
    contains a number that is divisible by 7,
    and returns false otherwise .
    numbers : list of numbers to check
    return : if list contains a number divisible by 7
    """
    for i in numbers:
        if i % 7 == 0:
            return True
    return False

"""
inputs: [] (pick this input after you inspect the code)
outputs_expected: False (get this use your brain after you know the functionality of the function by reading the docstring
reason: run the for loop 0 times

inputs: [1]
reason: run the for loop 1 time

inputs: [1,2,3,4,7] (look at the code)
outputs_expected: True (dont look at the code)
reason: run max times (len(number)) of the loop 
"""

