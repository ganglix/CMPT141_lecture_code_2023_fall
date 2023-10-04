# Write Python code which asks a user to input a string from
# the console until it is identical to pre-defined string passcode.
# When this occurs, print the number of attempts made to
# enter the correct string. e.g. "3 attempt(s) made."

passcode = "cmpt141"
user_input = input("please input your passcode:")
count = 1
while user_input != passcode:
    user_input = input("please input your passcode:")
    count += 1

print(f"{count} attempt(s) made.")

# passcode = "cmpt141"
# count = 0
# # initiate a wrong input
# user_input = ""
# while user_input != passcode:
#     user_input = input("please input your passcode:")
#     count += 1
#
# print(f"{count} attempt(s) made.")




# Bonous: another option to stop a while loop [not covered in the textbook]

# # not best readability
# passcode = "cmpt141"
# count = 0
# while True:
#     user_input = input("please input your passcode:")
#     count += 1
#     if user_input == passcode:
#         break
#
# print(f"{count} attempt(s) made.")
