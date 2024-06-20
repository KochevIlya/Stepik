m = int(input())
n = int(input())
set1 = set()
for i in range(m):
    set1.add(input())
for i in range(n):
    print("NO" if input() not in set1 else "YES")