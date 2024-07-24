import random

n = int(input())

for i in range(n):
    rand = random.randint(0, 1)
    print("Орёл" if rand == 0 else "Решка")