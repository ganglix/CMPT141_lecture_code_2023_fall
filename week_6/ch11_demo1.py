# demo1
# Tower Name Location
# Tokyo Skytree Japan
# Canton Tower China
# CN Tower Canada

tower = {
    "Tokyo Skytree": "Japan",
    "CN Tower": "Canada",
    "Canton Tower": "China",
}

# Let’s modify the dictionary:
# (a) Remove the entry whose location is "Canada"
# tower.pop("CN Tower")

for key in tower.copy(): # tower.copy() is a clone of tower, so that we dont iter over a size-changing dict
    if tower[key] == "Canada":
        tower.pop(key)

print(tower)

# (b) Add a new entry with tower name "Eiffel Tower" and
# location "Paris"
tower['Eiffel Tower'] = "Paris"
print(tower)

# (c) Oops! Update the tower entry "Eiffel Tower" to have
# location "France"
tower["Eiffel Tower"] = "France"
print(tower)
