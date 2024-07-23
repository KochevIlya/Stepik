lst = []
with open("numbers.txt") as file:
    lst = file.readlines()
    lst = list(map(lambda x: x.strip().split(), lst))
for i in lst:
    sum = 0
    for c in i:
        sum += int(c)
    print(sum)