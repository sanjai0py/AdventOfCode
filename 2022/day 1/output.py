file = open("input.txt", "r")
data = file.read().split("\n")

# Storing the list of num
total_array = list()

# Getting the Highest val
highest_val = 0


count = 0
for i in data:
    if i == '':
        # total_array.append(count)

        count = 0
        continue
    count += int(i)


# Sort the list to find the highest num
total_array.sort()

# Getting the highest val
highest_calorie = total_array[-1]

# Getting the top three highest val
top_three_highest = total_array[-3:]

# Getting the last val as the list is sorted in ascending order
print(highest_calorie)

file.close()

