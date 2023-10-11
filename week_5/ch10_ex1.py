# A given list called pkg_weights contains weights of parcels
# (in lbs) queued for shipping. Write Python code that:
# (a) Creates list light_pkgs of parcels that weigh less than 5
# lbs from pkg_weights
# (b) Removes parcels from pkg_weights that exceed 15 lbs
# (c) Print the:
# • contents of light_pkgs in ascending order
# • number of parcels in light_pkgs
# • number of parcels removed from pkg_weights

pkg_weights = [2, 6, 8, 34, 56, 67, 4, 2, 33]

# (a) Creates list light_pkgs of parcels that weigh less than 5 lbs
light_pkgs = []
for pkg in pkg_weights:
    if pkg < 5:
        light_pkgs.append(pkg)
print(light_pkgs)

# (b) Removes parcels from pkg_weights that exceed 15 lbs
# for pkg in pkg_weights: # big mistake: looping through a size-chaning list
#     if pkg > 15:
#         pkg_weights.remove(pkg)
#         print(pkg_weights)

# use a clone! (advanced!)
# create a clone of the original list
# pkg_weights_copy = pkg_weights.copy() # pkg_weights[:] also creates a copy
# for pkg in pkg_weights_copy:
#     if pkg > 15:
#         pkg_weights.remove(pkg)
# print(pkg_weights)

# not using a clone
heavy_pkgs = []
for pkg in pkg_weights:
    if pkg > 15:
        heavy_pkgs.append(pkg)

for pkg in heavy_pkgs:
    pkg_weights.remove(pkg)
print(pkg_weights)

# (c) Print the:
# • contents of light_pkgs in ascending order
# • number of parcels in light_pkgs
# • number of parcels removed from pkg_weights

# light_pkgs.sort()
# print(light_pkgs)
print(sorted(light_pkgs))

print("number of parcels in light_pkgs:", len(light_pkgs))
print("number of parcels removed from pkg_weights:", len(heavy_pkgs))






# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention
# Modifying list while iterating DO NOT DO IT
# don't change list if possible
# use a clone





