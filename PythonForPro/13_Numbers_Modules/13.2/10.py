from fractions import Fraction as F

n = int(input())
sum = 0
num = F(1, 1)
znam = 1
for i in range(n):
    sum += F(1, znam ** 2)
    znam += 1
print(sum)
