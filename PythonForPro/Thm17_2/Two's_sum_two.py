file = open("nums.txt")
lst = []
line = file.readline()
while line != "":
    line = line.strip()
    if line == "":
        line = file.readline()
        continue
    else:
        lst.append(int(line.strip()))
        line = file.readline()
print(sum(lst))
file.close()