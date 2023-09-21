# how to define a function
# creating functions: parameter, arguments, return
## things I want to mention: indentation, position, scope, calling function in a function  # Console I/O vs Function I/O
# in math
# f(x, y) = x + y
# f(1, 2) = 3

# def add_fun(num1, num2):
#     total = num1 + num2
#     print('total is', total)
#     return total
#
# result = add_fun(1,2)
# print(result)

"""
flowtrace
result = add_fun(1,2)
---------inside add_fun--------
num1 = 1
num2 = 2
total = 1 + 2
return 3
--------------------------------
result = 3
print(3)

"""


# demo
# types of functions
# no return value? How? When would we do this?
# def greeting(name):
#     print("hello", name)
#
# greeting('Gang')


# No parameters or return, How? when would we do this?
# def cat_says():
#     print("woof")
#
# cat_says()

def add_computing():
    num1 = float(input("type one number:"))
    num2 = float(input("type another number:"))
    return num1 + num2

# print( add_computing() )

def add_calculator():
    # num1 = float(input("type one number:"))
    # num2 = float(input("type another number:"))
    # print(num1 + num2)
    ans = add_computing()
    print(ans)

add_calculator()