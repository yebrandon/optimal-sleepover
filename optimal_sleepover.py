# Sleepover Calculation Algorithm
# Restrictions:
# Brandon and Zexi are available every day?
# Heshi is available Wednesday and Thursday this week
# Heshi is available Thursday to Monday next week
# Azhar is available Tuesday and Wednesday this week
# Azhar is not available next week
# Nathaniel is available every day this week?
# Nathaniel is not available next week
# Alex is available Thursday and Friday this week
# Alex is available every day next week?
# Leo is available Tuesday to Thursday this week
# Leo is availalbe Monday to Friday next week, except for Tuesday into Wednesday
# Leo must be available for the sleep over to happen
# Availabilities in the array start with Monday into Tuesday, then Tuesday into Wednesday, and so on

brandon_week_1 = [1, 1, 1, 1, 1, 1, 1]
brandon_week_2 = [1, 1, 1, 1, 1, 1, 1]

zexi_week_1 = [1, 1, 1, 1, 1, 1, 1]
zexi_week_2 = [1, 1, 1, 1, 1, 1, 1]

heshi_week_1 = [0, 0, 1, 1, 0, 0, 0]
heshi_week_2 = [0, 0, 0, 1, 1, 1, 1]

azhar_week_1 = [0, 1, 0, 0, 0, 0, 0]
azhar_week_2 = [0, 0, 0, 0, 0, 0, 0]

nath_week_1 = [0, 1, 1, 1, 1, 1, 1]
nath_week_2 = [0, 0, 0, 0, 0, 0, 0]

alex_week_1 = [0, 0, 0, 1, 1, 0, 0]
alex_week_2 = [1, 1, 1, 1, 1, 1, 1]

leo_week_1 = [0, 1, 1, 0, 0, 0, 0]
leo_week_2 = [1, 0, 1, 1, 0, 0, 0]

week_1_avails = [
    brandon_week_1,
    zexi_week_1,
    heshi_week_1,
    azhar_week_1,
    nath_week_1,
    alex_week_1,
    leo_week_1,
]
week_2_avails = [
    brandon_week_2,
    zexi_week_2,
    heshi_week_2,
    azhar_week_2,
    nath_week_2,
    alex_week_2,
    leo_week_2,
]

week_1_results = [0, 0, 0, 0, 0, 0, 0]
week_2_results = [0, 0, 0, 0, 0, 0, 0]


# Week 1
for avail in week_1_avails:
    for i in range(0, 6):
        week_1_results[i] += avail[i]

for avail in week_1_results:
    for i in range(0, 6):
        if leo_week_1[i] == 0:
            week_1_results[i] = 0

# Week 2
for avail in week_2_avails:
    for i in range(0, 6):
        week_2_results[i] += avail[i]

for avail in week_2_results:
    for i in range(0, 6):
        if leo_week_2[i] == 0:
            week_2_results[i] = 0

print(week_1_results)
print(week_2_results)