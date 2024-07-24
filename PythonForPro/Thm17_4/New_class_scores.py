with open("class_scores.txt") as fin, open("new_scores.txt", "w") as fout:
    lst = fin.readlines()
    newLst = []
    for i in lst:
        i = i.split()
        mark = i[1]
        mark = int(mark) + 5
        if mark > 100:
            mark = 100
        name = i[0]
        string = name + " " + str(mark) + "\n"
        newLst.append(string)

    fout.writelines(newLst)
