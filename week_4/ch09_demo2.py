# while vs. for
# In this demonstration, we’ll see a situation where using a
# while-loop is preferable to using a for-loop.

# password example

# initiate param
passcode = "cmpt141"
max_attempts = 3

# ask user to input passcode
user_input = input("please input your passcode:")
n_attempts = 1
while user_input != passcode and n_attempts < max_attempts:
    user_input = input("please input your passcode:")
    n_attempts += 1

# print message to user
# when while loop is done, there are two outcomes

if user_input == passcode:
    print(f"passcode is correct with {n_attempts} attempt(s))")
else:
    print(f"maximum number of attempts ({max_attempts}) reached, did you forget your passcode?")


