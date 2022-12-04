# .2345678.  2-8
# ..34567..  3-7
"""
if 2-8[0] <= 3-7[0] and 2-8[1] >= 3-7[1]:
    count + 1
"""

# .....6...  6-6
# ...456...  4-6
"""
if 6-6[0] >= 4-6[0] and 6-6[1] <= 4-6[1]:
    count + 1
"""

# ----------------------------------------------

# Opening the Input:
openInp = open("2022\day 4\input.txt")

# Reading the values
readInput = openInp.read().split("\n")

# Iteration to formate the input vals
for i, val in enumerate(readInput):
    readInput[i] = val.split(',')

globalCount = 0

# Problem 1:
# for i in readInput:
#     l0 = i[0].split('-')
#     l1 = i[1].split('-')

#     if int(l0[0]) <= int(l1[0]) and int(l0[1]) >= int(l1[1]):
#         globalCount += 1

#     elif int(l0[0]) >= int(l1[0]) and int(l0[1]) <= int(l1[1]):
#         globalCount += 1
#     else:
#         continue
# print(globalCount)


# Problem 2:
# for i in readInput:
#     split1 = i[0].split('-')
#     split2 = i[-1].split('-')

#     l0 = [y for y in range(int(split1[0]), int(split1[-1]) + 1)]
#     l1 = [y for y in range(int(split2[0]), int(split2[-1]) + 1)]

#     if set(l0) & set(l1):
#         globalCount += 1
#         continue
# print(globalCount)

#      --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
# 4   01: 58: 51  20651      0   03: 40: 16  28141      0
