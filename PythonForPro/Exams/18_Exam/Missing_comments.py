file_name = input()
with open(file_name) as file:
    lst = []
    result = []

    for line in file:
        lst.append(line)

    for i in range(len(lst)):
        if lst[i][0:3] == "def" and (i == 0 or lst[i-1][0] != "#"):
            result.append(lst[i][4:lst[i].find("(")])
    print(*result, sep = "\n") if len(result) != 0 else print("Best Programming Team")

            
        