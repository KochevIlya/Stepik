n = int(input())
set1 = set()
for i in range(n):
    set1.add(input())
print("OK" if input() not in set1 else "REPEAT")