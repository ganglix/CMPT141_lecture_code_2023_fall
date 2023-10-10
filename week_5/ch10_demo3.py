# Up until now, only immutable data types have been passed
# as arguments to functions. What happens when we pass
# mutable data?
# Let us observe the effect on an input variable before,
# during, and after a function call that changes the value.


def update_grades(grades):
    grades[0] = grades[0] + 2

classgrades = [48, 53, 95, 72]

new_grades = update_grades(classgrades)

print(classgrades)
print(new_grades)

# -----------------------------------------
# def update_grades_for_all(grades):






# -----------------------------------------
# # does this operation create a new list?

