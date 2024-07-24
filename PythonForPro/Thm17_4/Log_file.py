with open("logfile.txt", encoding="utf-8") as fin, open("output.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        line = line.rstrip("\n").split(", ")
        if (lambda x, y: int(y.split(":")[0]) * 60 + int(y.split(":")[1]) - int(x.split(":")[0]) * 60 - int(x.split(":")[1]))(line[1], line[2]) >= 60:
            fout.write(line[0] + "\n")
