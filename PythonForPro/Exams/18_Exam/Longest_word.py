with open("words.txt") as file:
    line = file.read()
    line = line.split()
    result = []
    length = 0
    for i in line:
        if length < len(i):
            result.clear()
            result.append(i)
            length = len(i)
        elif length == len(i):
            result.append(i)
    print(*result, sep = "\n")