# Flowtrac with function
# scope

status = "Healthy"
def set_status(s):
    status = s

set_status("Poisoned")
print(status)









# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(reminder: scope, return, dangerous thing to do, inplace)


# # inplace update with class/object  (advanced, not covered in cmpt141)

# class Pokemon:
#     def __init__(self, status):
#         self.status = status
#
#     def set_status(self, new_status):
#         self.status = new_status
#
# pikachu = Pokemon("healthy")
# print(f"before poisoned: {pikachu.status}")
#
# pikachu.set_status("poisoned")
# print("after poisoned:", pikachu.status)




# spaceship game
# http://www.codeskulptor.org/#user43_7zb1ohzfMl_35.py