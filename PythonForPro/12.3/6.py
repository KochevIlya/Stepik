import random

s = 16
n = 10**6   
k = 0
for i in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
        k += 1
print(float(k) / float(n) * s)