# Given variables:
nation = "Canada !!!"
nation_motto = "From Sea to Sea"

# Write expressions to:
# (a) Determine if nation has only alphabetic letters and digits
print(nation.isalnum())

# (b) Remove "!" characters and whitespace from nation
print( nation.replace("!", "").replace(" ", "") )

# (c) Find the location of the first "Sea" substring in nation_motto
print(nation_motto.find('Sea'))
help(nation_motto.find)
print(nation_motto.rfind('Sea'))

print(nation_motto.index("Sea"))

print('-'*20)
location_of_first_Sea = nation_motto.find('Sea')
print('-'*20)

print(
    nation_motto.find('Sea', location_of_first_Sea + 1, len(nation_motto))
)