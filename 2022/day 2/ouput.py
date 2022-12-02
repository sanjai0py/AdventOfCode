
# The file
read_file = None

# Opening and closing the file
open_file = open("day 2\input.txt", 'r')
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
for i in read_file:
    if i in winning_pairs:
        grand_total += shape_val.get(i.split(' ')[-1]) + 6
    elif i in draw_pairs:
        grand_total += shape_val.get(i.split(' ')[-1]) + 3
    else:
        grand_total += shape_val.get(i.split(' ')[-1]) + 0
print(grand_total)



# Problem 2
# COULDNT SOLVE




