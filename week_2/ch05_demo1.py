# This demonstration shows you how to call methods on string objects.


# initialize some variables to play with
url = "www.engineering.usask.ca"

# # find the location of the first period in the url
# def find_dot(web_url):
#     # find the locations of all dots
#     # return the first location

print(url.find("."))
print(url.find("eng"))

# count the number of periods in the url
print('number of . =', url.count("."))

# remove white space
new_url = "  www.usask.ca  "
print( new_url.rstrip() )   # .rstrip() remove space, \n \r
print( new_url.lstrip() )
print( new_url.strip() )

wrong_url = "  www.us   ask.ca  "
print(wrong_url)
print(wrong_url.replace(" ", ""))

# count the number of characters in the url after removing "www."
# (!gotta be careful - don’t just assume a function does what you think!)

# print(  len(url.replace("www.", ""))  )
# print("use .lstrip():", url.lstrip("w."))

# help(url.lstrip)

# # # more methods:

# # .upper()
print(url.upper().lower())
# # .lower()
# user_input = input("please type y/n:" ).lower()
# # .replace()

# # immutable, they create a copy
old = "1234"
print(old)
print(old.replace("12", "100"))
print(old)


# # how do I know what kind of methods are out there? How do I know the syntax/usage?
from pprint import pprint
pprint(dir(url))
# help(url.isalnum)
print(url.isalnum.__doc__)