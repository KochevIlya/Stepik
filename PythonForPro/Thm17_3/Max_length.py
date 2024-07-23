lst = []
with open("lines.txt") as file:
    lst = file.readlines()
max = len(lst[0])
for i in lst:
    i = i.strip()
    if len(i) > max:
        max = len(i)
for i in lst:
    i = i.strip()
    if len(i) == max:
        print(i)
