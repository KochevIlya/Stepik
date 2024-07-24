from fractions import Fraction as F
n = int(input())
l = set()
for i in range(2, n + 1):
    for j in range(1, i):
        l.add(F(j, i))
print(*sorted(l), sep = "\n")

