
# The file
read_file = None

# Opening and closing the file
open_file = open("2022\day 2\input.txt", 'r')
read_file = open_file.read().split('\n')
open_file.close()

# Value for the shape
shape_val = {"X": 1, "Y": 2, "Z": 3}

# Winning pairs
winning_pairs = ["C X", "B Z", "A Y"]

# Draw pairs
draw_pairs = ["A X", "B Y", "C Z"]

# Total value
grand_total = 0


# Problem 1
# for i in read_file:
#     if i in winning_pairs:
#         grand_total += shape_val.get(i.split(' ')[-1]) + 6
#     elif i in draw_pairs:
#         grand_total += shape_val.get(i.split(' ')[-1]) + 3
#     else:
#         grand_total += shape_val.get(i.split(' ')[-1]) + 0
# print(grand_total)


# Problem 2
# t = 0
# for line in read_file:
#     x, y = line.split()

#     x = ord(x) - 65

#     if y == "X":
#         t += (x - 1) % 3 + 1
#     elif y == "Y":
#         t += 3 + x + 1
#     else:
#         t += 6 + (x + 1) % 3 + 1

# print(t)

# --------Part 1-------- --------Part 2---------
# Day       Time   Rank  Score       Time    Rank  Score
# 2   01: 33: 41  20747    0       > 24h  156051    0

