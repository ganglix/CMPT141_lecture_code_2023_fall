# Topic(s): Reading Files
# read file and create a list of dictionaries to store data
# looks like this:
# scientists = [{"name": "Isaac Newton",
#                "birth_year": 1643,
#                "death_year": 1727},
#               {"name": "Albert Einstein",
#                "birth_year": 1879,
#                "death_year": 1955}]

# ~~~~~~~~~~~~open~~~~~~~read~~~~~~close~~~~routine~~~~~~~~

# open file for reading
path = "./subfolder/scientists_data.txt"

f = open(path, "r")
scientists = []
# read in all scientist data and put in a list of records
for line in f:
    line = line.rstrip().split(",")
    # create scientist record
    record = {}
    record["name"] = line[0]
    record["birth_year"] = line[1]
    record["death_year"] = line[2]
    scientists.append(record)

print(scientists)

# done reading , close file
f.close()















# ~~~~~~~ use with statement~~~~~~~~~~~~~~~~~

