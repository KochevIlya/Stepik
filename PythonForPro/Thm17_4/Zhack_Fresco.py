with open("goats.txt") as fin, open("answer.txt", "w") as fout:
    line = fin.readline()
    line = fin.readline()
    colors = []
    while line != "GOATS\n":
        colors.append(line.split()[0])
        line = fin.readline()
    counts = [0] * len(colors)
    line = fin.readline()
    countAll = 0
    while line != "":
        index = colors.index(line.split()[0])
        counts[index] += 1
        countAll += 1
        line = fin.readline()
    sevenPers = countAll * 0.07
    for i in range(len(colors)):
        if counts[i] > sevenPers:
            fout.write(colors[i] + " goat\n")

        