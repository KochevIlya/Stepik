import random
n = int(input())
lst = []
for i in range(n):
    lst.append(input())
friend = lst.copy()
random.shuffle(friend)
i = 0
while i != n:
    if friend[i] != lst[i]:
        i += 1
        continue
    else:
        random.shuffle(friend)
        i = 0

for i in range(n):
    print(lst[i], "-", friend[i])

