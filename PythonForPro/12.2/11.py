import random
matr = []
allsubSeq = set()
for i in range(5):
    length = len(allsubSeq)
    subSeq = []
    for j in range(5):
        temp = random.randint(1, 75)
        allsubSeq.add(temp)
        while length == len(allsubSeq):
            temp = random.randint(1, 75)
            allsubSeq.add(temp)
        subSeq.append(temp)
        length += 1
    matr.append(subSeq)
matr[2][2] = 0
for i in range(5):
    for j in range(5):
        print(str.ljust(str(matr[i][j]), 3), end = "")
    print()