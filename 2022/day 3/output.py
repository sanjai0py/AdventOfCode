# Ineffeicient alphabet object
alphabets = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
             'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38,
             'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44,  'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50,
             'Y': 51, 'Z': 52}

# Openening and closing the file
openedFile = open("2022\day 3\input.txt", "r")
readFile = openedFile.read().split('\n')
openedFile.close()

# This Stores the total val
globalVal = 0

# Problem 1

# for i in readFile:
#     lengthOfI = len(list(i))
#     mid = lengthOfI // 2

#     string1 = set(list(i[:mid]))
#     string2 = set(list(i[mid:]))

#     for i in string1:
#         if i in string2:
#             globalVal += alphabets.get(i)
# print(globalVal)


# Problem 2
# for fileVals in range(0, len(readFile), 3):
#     valIn3s = readFile[fileVals:fileVals+3]

#     for i in range(3):
#         valIn3s[i] = list(set(valIn3s[i]))
    
#     for i in valIn3s[0]:
#         if i in valIn3s[1] and i in valIn3s[2]:
#             globalVal += alphabets.get(i)
# print(globalVal)



