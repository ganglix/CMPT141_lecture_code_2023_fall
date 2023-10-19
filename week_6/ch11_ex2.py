# Exercise 2

# Suppose we have dictionary availability:
# keys: friend’s name
# values: list of days they are available to play a game
# (a) Write a function that accepts an availability dictionary and returns a new dictionary mapping days to
# friends who can play that day.
# (b) Using the function from a):
# Find the day most friends can attend to play the game
# List who can and can not attend the session that day

availability = {"Neo": ["Monday"],
                "Morpheus": ["Sunday"],
                "Smith": ["Monday", "Tuesday"]}


def reverse_dict(avail_dict):
    week_schedule = {}   # day : [names]
    for name in avail_dict:
        day_list = avail_dict[name]
        for day in day_list:
            if day not in week_schedule:
                week_schedule[day] = []   # initialize a []
            week_schedule[day].append(name)

    return week_schedule

schedule = reverse_dict(availability) # day: [names]
most_number_of_friends = 0
most_avail_day = ""

for day in schedule:
    if len(schedule[day]) > most_number_of_friends:
        most_number_of_friends = len(schedule[day])
        most_avail_day = day

print(f"{most_number_of_friends} are available on {most_avail_day}")
