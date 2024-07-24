lst = [input() for i in range(int(input()))]
result = []

with open("output.txt", "w") as fout:
    fout.write("")

with open("output.txt", "a") as fout:
    for i in lst:
        with open(i) as fin:
            for line in fin:
                fout.write(line)