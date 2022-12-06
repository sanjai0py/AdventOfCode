# Open and close the file
rawData = open("2022\day 6\input.txt")
fmtdData = list(rawData.read())
rawData.close()


# Problem 1

# Itreate fmtdData
# for i in range(len(fmtdData)):
#     # jus like sliding-window technique
#     trimS = slice(i, i+4)
#     window = fmtdData[trimS]

#     if len(set(window)) == 4:
#         print(i+4)
#         break
#     continue

# Problem 2

# for i in range(len(fmtdData)):
#     # jus like sliding-window technique
#     trimS = slice(i, i+14)
#     window = fmtdData[trimS]

#     if len(set(window)) == 14:
#         print(i+14)
#         break


#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#   6   02:21:27  28384      0   02:29:55  28387      0