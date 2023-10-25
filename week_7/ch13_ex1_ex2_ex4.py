def is_valid_username(username):
    """
    determines if username meets these constraints:
    - 1-18 characters long
    - can be letters and/or numbers
    - underscore is allowed if it’s not the first character
    username: string to check validity of
    return: True if username satisfies constraints
    """

# Testing - black box
# black box reasoning

# - 1-18 characters long
"""
inputs: ""
outputs_expected: False
reason: empty string, length is out of range

inputs: "a" * 19
outputs_expected: False
reason: empty string, length is out of range 19 > 18

inputs: "abc" 
outputs_expected: True
reason: this a general valid case
"""

# - can be letters and/or numbers
"""
inputs: "1"
outputs_expected: True
reason: has number, length is one, no leading _, it is valid username

inputs: "a1"
outputs_expected: True
reason: has number and letter, length is 2, no leading _, it is valid username

inputs: "1a"
outputs_expected: True
reason: has number and letter, length is 2, no leading _, number goes first, it is valid username

inputs: " 1a"
outputs_expected: False
reason: has space, which is not allowed

inputs: "~~~a"
outputs_expected: False
reason: has other special character, which is not allowed

"""

# - underscore is allowed if it’s not the first character

"""
inputs: "_"
outputs_expected: False
reason: it has leading underscore, lengh is one, which is not valid

inputs: " _"
outputs_expected: False
reason: it has space, which is not valid

inputs: "a_"
outputs_expected: True
reason: underscore is not at the beginning; the username is valid

inputs: "a_b"
outputs_expected: True
reason: underscore is not at the beginning; it is in the middle; the username is valid
"""


# test driver example
inputs = "~~~a"
outputs_expected = False
reason = "This test case has other special characters, which are not allowed"

# test driver
# example for one of the test cases
result = is_valid_username(inputs)
if result != outputs_expected:  # no news is good news, no message if tests are passed
    print("Error found!",
          "input:", inputs,
          "return:", result,
          "expected return", outputs_expected,
          "test reason", reason)


# ~~~~~~~~~~~~~~~~ dictionary~~~~~~~~~~~~~~~~~~~~

# dictionary of test case suite to feed into test driver loop
test_suite = [
    # call for length -zero username (empty string)
    {"inputs": [""],
     "outputs": False,
     "reason": "length must be be 1-18 characters"},

    # call for length -one username of invalid character
    {"inputs": ["+"],
     "outputs": False,
     "reason": "username can only contain letters , numbers , underscores"},

    # call for length -one username of a letter
    {"inputs": ["a"],
     "outputs": True,
     "reason": "username is allowed to have letters"},

    # call for length -18 username of numbers only with trailing underscore
    {"inputs": ["0" * 17 + "_"],
     "outputs": True,
     "reason": "username is allowed to have numbers and trailing underscore"},

    # call for length -three username with letter , number , underscore
    {"inputs": ["a_0"],
     "outputs": True,
     "reason": "username is allowed to have letters , numbers , underscore"},

    # call for length -three username with letter , number , starting underscore
    {"inputs": ["_a0"],
     "outputs": False,
     "reason": "can’t start with underscore"},

    # call for length -18+ username of letters and numbers
    {"inputs": ["a0" * 18],
     "outputs": False,
     "reason": "can’t have more than 18 characters"}
]

# a generic loop for test drivers
# the inputs are in a list , so it has to be modified
for test in test_suite:  # test is a dict of a test case
    inputs = test["inputs"]
    result = is_valid_username(inputs[0])

    if result != test["outputs"]:
        print(f"Testing fault: is_valid_username () returned {result} on inputs {inputs}"
              f"\ntest reason: {test['reason']})\n")

