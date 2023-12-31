# Daily variance of flu tests can be high. We often calculate the
# 7-day average instead: for each day, take the AVERAGE of
# the preceding 7 days (including itself)
# Using the flu_data list, create a new list where the values
# are the 7-day average for each day. Start from day 7
# Then, plot the data in the new list
# Hint: Slicing might be useful

flu_case = [13, 14, 9, 16, 10, 18, 22, 19, 16, 22,
             24, 48, 34, 25, 17, 29, 33, 35, 28, 43,
             59, 44, 55, 63, 61, 48, 68, 61, 70, 76,
             78, 74, 87, 101, 120, 128, 105, 109, 120, 124,
             111, 128, 120, 133, 134, 139, 127, 130, 141, 147,
             439, 236, 218, 209, 213, 244, 329, 197, 351, 325]

"""
index   0   1   2   3   4   5   6   7   ... len(flu_case)-1
day     1   2   3   4   5   6   7   8   ... len(flu_case)
"""

days = list(range(1, len(flu_case)+1))
days_starting_7 = days[7:]
window_size = 7

# # average day 1-7  and report for day 7
# day = 7
# average_7d = sum(flu_case[day-window_size:day])/ window_size
#
# # average day 2-8 for day 8, by moving forward by 1 day
# day = 8
# average_7d = sum(flu_case[day-window_size: day])/ window_size


# average for all days from day 7 onwards
flu_case_7d_average = []
for day in days_starting_7:
    average_7d = sum(flu_case[day-window_size:day])/ window_size
    flu_case_7d_average.append(average_7d)

# plot
import matplotlib.pyplot as plt
plt.plot(days, flu_case, marker="o", linestyle="", label = "daily")
plt.plot(days_starting_7, flu_case_7d_average, label = "7d average")
plt.legend()
plt.xlabel('day')
plt.ylabel('flu case')
plt.xticks(days[::3])
plt.show()





