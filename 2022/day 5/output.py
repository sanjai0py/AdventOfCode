# Opening and closing the file:
rawData = open("2022\day 5\input.txt")
formattedData = rawData.read().split('\n')
rawData.close()

startingStacks = {
    1: ['G', 'T', 'R', 'W'],
    2: ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'],
    3: ['C', 'L', 'T', 'S', 'G', 'M'],
    4: ['J', 'H', 'D', 'M', 'W', 'R', 'F'],
    5: ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'],
    6: ['P', 'J', 'D', 'N', 'F', 'M', 'S'],
    7: ['Z', 'B', 'D', 'F', 'G', ' C', 'S', 'J'],
    8: ['R', 'T', 'B'],
    9: ['H', 'N', 'W', 'L', 'C']
}

rearrangementProcedure = []

for i in formattedData:
    if i.startswith('move'):
        rearrangementProcedure.append(i)

for i in rearrangementProcedure:
    words = i.split()
    mvs = int(words[1])

    lstFrm = startingStacks.get(int(words[3]))
    lstTo = startingStacks.get(int(words[5]))

    if mvs == 1:
        pop = lstFrm.pop()
        lstTo.append(pop)
    elif mvs > 1:
        x = slice(-mvs, len(lstFrm))

        v = lstFrm[x]
        lstTo += v

        while mvs > 0:
            lstFrm.pop()
            mvs -= 1


outPut = []

for i in startingStacks:
    dic = startingStacks.get(i)

    val = dic.pop()
    outPut.append(val)

print(''.join(outPut))

#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#   5   03:47:32  27446      0   04:24:26  28962      0


# This is the most horrable code ive ever written!!!!