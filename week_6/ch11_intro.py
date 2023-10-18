# dictionary : hash map in python

# Store and look up data
phone_list = ['306123456', '3068888888']
name_list = ['Mark', 'Gang']

# idx = name_list.index("Gang")
# print(phone_list[idx])

phone_book = { "Mark" : "306123456",
               "Gang" : "3068888888" }

print(phone_book["Mark"])

# add, remove, a key-value pair
phone_book["Adam"] = "911"
print(phone_book)

# del phone_book["Adam"]
# phone_book.pop("Adam")

print(phone_book)

# KEYS  # use consistent key
# any immutable data type: int, float, string, tuple,


# VALUES
# any data type
contacts = { "Mark": {"number" : "3061234567",
                      "email": "mark.usask.ca"},
             "Gang": "3068888888" }

print("mark email  " , contacts["Mark"]["email"])

# dictionary methods
# for something in phone_book:
#     print("something", something, phone_book[something])

# print(
#     phone_book.keys(),
#     phone_book.values(),
#     phone_book.items(),
#     sep='\n')

# No key found?
# use unique keys
d = {'mark_0': 98, 'mark_1':99}
print(d.get('mark_2', 'key is not existing!'))

# things I want to mention: mutable, no order, key is the key
# note since python 3.7 dictionary items are ordered