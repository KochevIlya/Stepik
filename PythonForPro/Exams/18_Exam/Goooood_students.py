with open("grades.txt") as file:
    counter = 0
    for line in file:
        lst = line.split()
        if int(lst[1]) >= 65 and int(lst[2]) >= 65 and int(lst[3]) >= 65:
            counter += 1
    print(counter)