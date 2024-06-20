m = int(input())
n = int(input())
set1 = set()
counter = 0
for i in range(n + m):
    str = input()
    if str in set1:
        counter += 1 
    else:
        set1.add(str)
print(len(set1) - counter) if len(set1) != counter else print("NO")