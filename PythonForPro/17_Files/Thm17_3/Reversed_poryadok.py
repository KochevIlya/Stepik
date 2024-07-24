with open("data.txt") as file:
    lst = file.readlines()
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i][:-1])