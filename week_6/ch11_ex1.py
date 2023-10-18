# Exercise 1

# Suppose you have a dictionary of survey responses:
# •keys are student names
# •values are favourite ice cream flavours (one of
# "chocolate", "vanilla", "strawberry")
# Write a function that takes a dictionary of survey responses
# and returns a new dictionary where:
# •keys are ice cream flavours
# •values are number of students with that favourite flavour

survey = {"Christopher": "vanilla",
          "Ty": "vanilla",
          "Muhammed": "chocolate",
          "Ani": "vanilla",
          "Gang": "strawberry"}

# def icecream_vote(survey):
#     """
#     Count the vote  for each ice cream flavour in a survey.
#     :param survey: dict, A dictionary representing the survey results with participant names as keys
#                    and their selected ice cream flavors as values.
#     :return: dict, A dictionary containing ice cream flavors as keys and the number of votes they received as values.
#     """
#     result = {}  # flavour: votes
#     for name in survey:
#         flavour = survey[name]
#         if flavour not in result:
#             result[flavour] = 1  # add 1 as value, when flavour is seen for the first time
#         else:
#             result[flavour] += 1
#
#     return result


def icecream_vote(survey):
    """
    Count the vote  for each ice cream flavour in a survey.
    :param survey: dict, A dictionary representing the survey results with participant names as keys
                   and their selected ice cream flavors as values.
    :return: dict, A dictionary containing ice cream flavors as keys and the number of votes they received as values.
    """
    result = {}  # flavour: votes
    for name in survey:
        flavour = survey[name]
        if flavour not in result:
            result[flavour] = 0  # initialize it as 0; make an entry so you can change later

        result[flavour] += 1  # anyways

    return result
print(icecream_vote(survey))